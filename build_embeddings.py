import pandas as pd
import numpy as np
import faiss
import pickle
from PIL import Image
from sentence_transformers import SentenceTransformer
from transformers import CLIPProcessor, CLIPModel
from sklearn.preprocessing import normalize

df = pd.read_csv("dataset/lost_found_dataset.csv")

print("Generating text embeddings...")

text_model = SentenceTransformer("all-MiniLM-L6-v2")

text_embeddings = text_model.encode(
    df["lost_description"].tolist(),
    normalize_embeddings=True
)

print("Generating image embeddings...")

clip_model = CLIPModel.from_pretrained("openai/clip-vit-base-patch32")
clip_processor = CLIPProcessor.from_pretrained("openai/clip-vit-base-patch32")

image_embeddings = []

for path in df["image_path"]:

    image = Image.open(path).convert("RGB")

    inputs = clip_processor(images=image, return_tensors="pt")

    outputs = clip_model.get_image_features(**inputs)

    image_embeddings.append(outputs.detach().numpy()[0])

image_embeddings = np.array(image_embeddings)

image_embeddings = normalize(image_embeddings)

combined_embeddings = np.hstack((text_embeddings, image_embeddings))
combined_embeddings = normalize(combined_embeddings)

dimension = combined_embeddings.shape[1]

print("Creating FAISS index...")

index = faiss.IndexFlatIP(dimension)

index.add(combined_embeddings)

faiss.write_index(index, "vector.index")

pickle.dump(df, open("data.pkl", "wb"))

print("Embeddings + Vector DB created!")
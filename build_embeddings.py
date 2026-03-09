import pandas as pd
import numpy as np
import faiss
import pickle
from PIL import Image
from sentence_transformers import SentenceTransformer
from transformers import CLIPProcessor, CLIPModel
from sklearn.preprocessing import normalize

# Load dataset
df = pd.read_csv("dataset/lost_found_dataset.csv")

# TEXT EMBEDDINGS
print("Generating text embeddings...")

text_model = SentenceTransformer("all-MiniLM-L6-v2")

text_embeddings = text_model.encode(
    df["lost_description"].tolist(),
    normalize_embeddings=True
)

# IMAGE EMBEDDINGS
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

# Normalize image embeddings
image_embeddings = normalize(image_embeddings)

# COMBINE TEXT + IMAGE EMBEDDINGS
combined_embeddings = np.hstack((text_embeddings, image_embeddings))

# Normalize combined embeddings
combined_embeddings = normalize(combined_embeddings)

dimension = combined_embeddings.shape[1]

# CREATE VECTOR DATABASE (COSINE SIMILARITY)
print("Creating FAISS index...")

index = faiss.IndexFlatIP(dimension)

index.add(combined_embeddings)

faiss.write_index(index, "vector.index")

# Save dataset
pickle.dump(df, open("data.pkl", "wb"))

print("Embeddings + Vector DB created successfully!")
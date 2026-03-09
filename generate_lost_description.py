import pandas as pd
import ollama

# Load scraped dataset
df = pd.read_csv("dataset/scraped_products.csv")

descriptions = []

for item in df["product_name"]:

    prompt = f"""
A student lost an item on campus.

The product is: {item}

Write a short realistic lost item report like a student would say.

Example:
"Lost my copy of Atomic Habits near the library reading area. It has a blue cover and my name written inside."

Keep it 1-2 sentences.
"""

    response = ollama.chat(
        model="llama3",
        messages=[{"role": "user", "content": prompt}]
    )

    descriptions.append(response["message"]["content"].strip())

# Add descriptions to dataset
df["lost_description"] = descriptions

# Save final dataset
df.to_csv("dataset/lost_found_dataset.csv", index=False)

print("Lost item descriptions generated successfully!")
import pandas as pd
import ollama

df = pd.read_csv("dataset/scraped_products.csv")

descriptions = []

for item in df["product_name"]:

    prompt = f"""
A student lost an item on campus.

The product is: {item}

Write a short realistic lost item description.

Example:
Lost my copy of Atomic Habits near the library reading area. It has a blue cover and my name written inside.

Keep it 1-2 sentences.
"""

    response = ollama.chat(
        model="llama3",
        messages=[{"role": "user", "content": prompt}]
    )

    descriptions.append(response["message"]["content"].strip())

df["lost_description"] = descriptions

df.to_csv("dataset/lost_found_dataset.csv", index=False)

print("Lost item descriptions generated!")
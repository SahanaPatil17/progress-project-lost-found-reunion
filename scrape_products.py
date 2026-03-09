import requests
from bs4 import BeautifulSoup
import pandas as pd
import os

url = "https://books.toscrape.com/"

response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")

items = []

os.makedirs("dataset/images", exist_ok=True)

books = soup.select(".product_pod")

for i, book in enumerate(books):

    title = book.h3.a["title"]

    img_url = book.img["src"]

    img_url = "https://books.toscrape.com/" + img_url

    img_data = requests.get(img_url).content

    img_path = f"dataset/images/item_{i}.jpg"

    with open(img_path, "wb") as f:
        f.write(img_data)

    items.append({
        "product_name": title,
        "image_path": img_path
    })

df = pd.DataFrame(items)

df.to_csv("dataset/scraped_products.csv", index=False)

print("Scraping complete")
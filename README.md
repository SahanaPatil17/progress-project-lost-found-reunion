# 🔍 Lost & Found Reunion – Multi-Modal Semantic Search Engine

A semantic search system that helps match lost items with items stored in a lost-and-found database using **AI embeddings, vector databases, and LLM explanations**.

Traditional lost-and-found systems rely on **manual keyword matching**, which often fails when item descriptions are vague or inconsistent.
This project solves the problem using **semantic search and multi-modal embeddings**.

---

# 📌 Problem

Lost & Found offices often store hundreds of items with vague descriptions such as:

* "Black bag"
* "Electronics item"
* "Found near canteen"

Students searching for items may describe them differently:

```
wireless headphones
earbuds
AirPods
```

Even though they refer to the **same object**, keyword search cannot match them effectively.

This project implements a **semantic search engine** that understands the meaning of descriptions using AI models.

---

# 🧠 System Architecture

```
Web Scraping
      ↓
Dataset Creation
      ↓
LLM Generated Lost Descriptions
      ↓
Text Embeddings (Sentence Transformers)
      ↓
Image Embeddings (CLIP)
      ↓
Vector Database (FAISS)
      ↓
Semantic Search
      ↓
LLM Explanation
      ↓
Streamlit UI
```

---

# ⚙️ Project Workflow

## 1️⃣ Data Collection (Web Scraping)

Product information was scraped using **BeautifulSoup**.

Data collected:

* Product name
* Product images

Images were downloaded locally and stored in the dataset folder.

Output file:

```
dataset/scraped_products.csv
```

---

## 2️⃣ Synthetic Lost Item Descriptions

Real lost-item reports are usually vague and inconsistent.
To simulate realistic data, **Llama3 via Ollama** was used to generate lost item descriptions.

Example prompt:

```
Create a realistic lost item description for:
Sapiens: A Brief History of Humankind
```

Example output:

```
Lost my copy of Sapiens near the library study area.
It has a yellow cover and some notes written in the margins.
```

Output dataset:

```
dataset/lost_found_dataset.csv
```

Each entry contains:

* product_name
* lost_description
* image_path

---

## 3️⃣ Embedding Generation

To enable **semantic understanding**, text and images are converted into vector embeddings.

### Text Embeddings

Model used:

```
SentenceTransformer
all-MiniLM-L6-v2
```

This model converts descriptions into vectors representing their meaning.

Example:

```
lost book near library
misplaced study book
```

These produce **similar embeddings** even though the words differ.

---

### Image Embeddings

Images are encoded using the **CLIP model**.

Model used:

```
openai/clip-vit-base-patch32
```

CLIP allows the system to understand **visual features of objects**.

---

## 4️⃣ Vector Database

All embeddings are stored in a **FAISS vector database**.

FAISS allows fast similarity search across high-dimensional embeddings.

Stored files:

```
vector.index
data.pkl
```

The combined embeddings allow **multi-modal search (text + image)**.

---

## 5️⃣ Semantic Search

When a user enters a query, the system:

1. Converts the query into an embedding
2. Searches the FAISS vector index
3. Retrieves the most similar items
4. Calculates a similarity score (confidence score)

Example query:

```
lost paperback book with notes in the margins
```

---

## 6️⃣ AI Explanation

To make results understandable, **Llama3 (via Ollama)** generates explanations describing why an item might match.

Example explanation:

```
Both descriptions mention a paperback book with notes written in the margins.
This similarity suggests the items could refer to the same object.
```

---

## 7️⃣ User Interface

The application uses **Streamlit** to provide a simple UI.

Features:

* Natural language search
* Display item images
* Show item description
* Show similarity confidence score
* Generate AI explanation

Example UI workflow:

1. User enters a description of the lost item
2. System retrieves most similar items
3. Results are displayed with explanations

---

# 📂 Project Structure

```
lost-found-reunion-progress-project
│
├── scrape_products.py
├── generate_lost_descriptions.py
├── build_embeddings.py
├── search_engine.py
├── app.py
│
├── dataset
│   ├── scraped_products.csv
│   ├── lost_found_dataset.csv
│   └── images/
│
├── vector.index
├── data.pkl
├── requirements.txt
└── README.md
```

---

# 🚀 How to Run the Project

Follow these steps to run the project from scratch.

---

## 1️⃣ Clone the Repository

```bash
git clone https://github.com/SahanaPatil17/progress-project-lost-found-reunion.git
cd progress-project-lost-found-reunion
```

---

## 2️⃣ Install Dependencies

Install all required Python libraries.

```bash
pip install -r requirements.txt
```

---

## 3️⃣ Start the Local LLM (Ollama)

The project uses **Llama3 via Ollama** to generate descriptions and explanations.

Start the model:

```bash
ollama run llama3
```

Keep this terminal **running** while using the project.

---

# ⚙️ Data Pipeline (Run Once)

The following scripts build the dataset and vector database.

Run them **in this order**.

---

## 4️⃣ Scrape Product Data

This script scrapes product names and images from a sample website and saves them locally.

```bash
python scrape_products.py
```

Output created:

```
dataset/scraped_products.csv
dataset/images/
```

---

## 5️⃣ Generate Lost Item Descriptions

This script uses **Llama3** to generate realistic lost item descriptions based on product names.

```bash
python generate_lost_descriptions.py
```

Output created:

```
dataset/lost_found_dataset.csv
```

Each record now contains:

* product_name
* lost_description
* image_path

---

## 6️⃣ Build Embeddings and Vector Database

This script generates:

* **Text embeddings** using Sentence Transformers
* **Image embeddings** using CLIP
* **FAISS vector database** for semantic search

```bash
python build_embeddings.py
```

Output created:

```
vector.index
data.pkl
```

---

# 🖥 Running the Search Application

After building the dataset and embeddings, start the UI.

---

## 7️⃣ Launch the Streamlit Application

```bash
python -m streamlit run app.py
```

Open in your browser:

```
http://localhost:8501
```

You can now search for lost items using natural language.

---

# 🌍 Optional: Remote Access with ngrok

To allow external users to access the application:

```bash
ngrok http 8501
```

Example output:

```
https://abcd1234.ngrok-free.app
```

Share this link to access the application remotely.

---

# 🔎 Example Queries

Try searching with:

```
lost paperback book with notes
lost poetry book near library
lost study book with bookmark
```

The system will return:

* matching item images
* descriptions
* confidence scores
* AI explanations

---

# 🛠 Technologies Used

Python
BeautifulSoup
Pandas
Sentence Transformers
CLIP (Transformers)
FAISS Vector Database
Ollama (Llama3)
Streamlit
ngrok

---

# 🔮 Future Improvements

If more time were available, the following improvements could be added:

* Allow **image upload search** for visual matching
* Increase dataset size with **hundreds or thousands of items**
* Combine **keyword search with vector search**
* Deploy system on **cloud infrastructure**
* Improve ranking with hybrid search models
* Build a **mobile-friendly interface**

---

# 📚 Key Learning Outcomes

* Building semantic search systems
* Working with embedding models
* Implementing vector databases
* Using LLMs for reasoning and explanations
* Designing end-to-end AI pipelines

---


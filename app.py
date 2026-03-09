import streamlit as st
from search_engine import search, search_by_image, explain_match

st.title("🔍 Lost & Found Reunion")

st.write("Search for your lost item using text or by uploading an image.")

query = st.text_input("Describe your lost item")

uploaded_image = st.file_uploader(
    "Upload an image of the lost item",
    type=["jpg", "jpeg", "png"]
)

if st.button("Search"):

    if uploaded_image is not None:

        st.write("Searching using image...")

        results = search_by_image(uploaded_image)

    else:

        results = search(query)

    for _, row in results.iterrows():

        st.image(row["image_path"], width=200)

        st.write("**Item:**", row["product_name"])
        st.write("**Description:**", row["lost_description"])
        st.write("**Confidence Score:**", round(row["confidence"], 2))

        explanation = explain_match(query, row["lost_description"])

        st.write("🤖 **AI Explanation:**")
        st.write(explanation)

        st.divider()
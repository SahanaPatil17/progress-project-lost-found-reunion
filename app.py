import streamlit as st
from search_engine import search, explain_match

st.title("🔍 Lost & Found Reunion")

st.write("Search for your lost item using natural language.")

st.write("Example queries:")
st.code("lost paperback book with notes")
st.code("lost poetry book near library")

query = st.text_input("Describe your lost item")

if st.button("Search"):

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
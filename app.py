#http://localhost:8501
#streamlit run app.py
import streamlit as st
import joblib
import numpy as np
from sentence_transformers import SentenceTransformer

# Load ML model & vectorizer
model = joblib.load("skill_categorization_model.pkl")
vectorizer = joblib.load("tfidf_vectorizer.pkl")

# Load LLM for clustering unknown skills
llm = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")

# Function to predict skill category
def predict_category(skill):
    skill_vector = vectorizer.transform([skill])
    predicted_category = model.predict(skill_vector)[0]
    return predicted_category

# Function to cluster unknown skills using LLM
def cluster_unrecognized_skill(skill):
    embedding = llm.encode([skill])
    return f"Cluster {hash(tuple(embedding[0])) % 100}"  # Simple hash-based clustering

# Streamlit UI
st.title("Skill Categorization App")
st.write("Enter a skill to predict its category")

skill_input = st.text_input("Enter Skill:", "")

if st.button("Categorize"):
    if skill_input.strip():
        try:
            category = predict_category(skill_input)
            st.success(f"**Predicted Category:** {category}")
        except:
            new_category = cluster_unrecognized_skill(skill_input)
            st.warning(f"Unrecognized skill. **Assigned to Cluster:** {new_category}")
    else:
        st.error("Please enter a valid skill.")

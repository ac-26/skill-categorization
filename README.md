# **Skill Categorization NLP with FastAPI**

## **Overview**

This project aims to classify various skills into predefined categories using Natural Language Processing (NLP) techniques. The model is deployed using **FastAPI**, making it accessible through a RESTful API endpoint for real-time skill categorization. 

---

## **Table of Contents**

- [Overview](#overview)
- [Technologies Used](#technologies-used)
- [Data](#data)
- [Model](#model)
- [Installation](#installation)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [Running the Application](#running-the-application)
- [License](#license)

---

## **Technologies Used**

- **Python** (v3.8+)
- **FastAPI** – Framework for building the API.
- **Uvicorn** – ASGI server for running FastAPI.
- **Scikit-learn** – For machine learning models.
- **Pickle** – For saving and loading the trained model.
- **TF-IDF Vectorizer** – For text feature extraction.
- **Jupyter Notebook** – For model development and experimentation.
- **requests** – For testing the API endpoints locally.

---

## **Data**

The dataset used for training the model consists of a list of skills labeled into categories. The key columns in the dataset include:

- **Skill**: The skill name (e.g., Python, Data Science, Project Management).
- **Category**: The skill's corresponding category (e.g., **Technical Skills**, **Data & AI Skills**, etc.).

The dataset was preprocessed by removing unwanted characters, tokenizing the text, and converting the skills into numerical vectors using the **TF-IDF Vectorizer**.

---

## **Model**

Several machine learning models were evaluated for this task:

1. **Logistic Regression**
2. **Random Forest**
3. **Support Vector Machine (SVM)**

The **SVM model** provided the best performance, and this is the model used in production. The model was trained using the preprocessed dataset and saved using **Pickle** (`model.pkl`).

---

## 💻 **Installation & Usage**  
### ** Running the code**
Option 1: Google Colab:
Upload the notebook skill_categorization.ipynb to Google Drive and execute all cells by going to Runtime -> Run all in Google Collab

Option 2: Jupyter Notebook
Open the file in Jupyter Notebook and run all cells.

In the skill_categorizazion file there is a section that i have highlighted as "Try the code here". You may change the skills according to your wish and evaluate.




# skill-categorization
Overview

This project aims to classify various skills into predefined categories using Natural Language Processing (NLP) techniques. The model is deployed using FastAPI, making it accessible through a RESTful API endpoint for real-time skill categorization. It is designed for use in applications like job matching, skill gap analysis, and talent management.

Table of Contents

Overview
Technologies Used
Data
Model
Installation
Usage
API Endpoints
Running the Application
License
Technologies Used

Python (v3.8+)
FastAPI – Framework for building the API.
Uvicorn – ASGI server for running FastAPI.
Scikit-learn – For machine learning models.
Pickle – For saving and loading the trained model.
TF-IDF Vectorizer – For text feature extraction.
Jupyter Notebook – For model development and experimentation.
requests – For testing the API endpoints locally.
Data

The dataset used for training the model consists of a list of skills labeled into categories. The key columns in the dataset include:

Skill: The skill name (e.g., Python, Data Science, Project Management).
Category: The skill's corresponding category (e.g., Technical Skills, Data & AI Skills, etc.).
The dataset was preprocessed by removing unwanted characters, tokenizing the text, and converting the skills into numerical vectors using the TF-IDF Vectorizer.

Model

Several machine learning models were evaluated for this task:

Logistic Regression
Random Forest
Support Vector Machine (SVM)
The SVM model provided the best performance, and this is the model used in production. The model was trained using the preprocessed dataset and saved using Pickle (model.pkl).

Installation

Follow these steps to get the project up and running:

Clone this repository:
git clone https://github.com/your-username/skill-categorization-nlp.git
Navigate to the project directory:
cd skill-categorization-nlp
Create a virtual environment:
python3 -m venv venv
Activate the virtual environment:
On macOS/Linux:
source venv/bin/activate
On Windows:
venv\Scripts\activate
Install the required dependencies:
pip install -r requirements.txt
Usage

After setting up, run the FastAPI server using Uvicorn:
uvicorn app:app --reload
Visit http://127.0.0.1:8000/docs to access the Swagger UI where you can interact with the model by providing a skill to be categorized.
Alternatively, you can test the API using the requests library from Python:
Example:

import requests
response = requests.post("http://127.0.0.1:8000/predict", json={"skill": "Machine Learning"})
print(response.json())
API Endpoints

POST /predict
This endpoint accepts a JSON object containing a skill and returns the predicted category.

Example Request:

{
  "skill": "Data Science"
}
Example Response:

{
  "category": "Data & AI Skills"
}
Running the Application

To run the FastAPI application, use the following command:

uvicorn app:app --reload
The app will be accessible at http://127.0.0.1:8000.

License

This project is licensed under the MIT License – see the LICENSE file for details.

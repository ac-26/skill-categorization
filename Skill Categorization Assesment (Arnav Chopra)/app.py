import pickle
from fastapi import FastAPI
from pydantic import BaseModel
from sklearn.preprocessing import LabelEncoder

# Load the model
with open("skill_model.pkl", "rb") as model_file:
    svm_model = pickle.load(model_file)

# Load the vectorizer
with open("vectorizer.pkl", "rb") as vectorizer_file:
    vectorizer = pickle.load(vectorizer_file)

print("Model and Vectorizer loaded successfully!")


with open("label_encoder.pkl", "rb") as encoder_file:
    label_encoder = pickle.load(encoder_file)

# Initializing FastAPI app
app = FastAPI()

class SkillInput(BaseModel):
    skills: list

@app.post("/predict/")
def predict_category(skill_input: SkillInput):

    skill_vectors = vectorizer.transform(skill_input.skills)

    predicted_labels = svm_model.predict(skill_vectors)

    predicted_categories = label_encoder.inverse_transform(predicted_labels)

    return {"predictions": predicted_categories.tolist()}

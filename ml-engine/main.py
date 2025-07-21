from fastapi import FastAPI
from pydantic import BaseModel
import pickle
import os

app = FastAPI()

# Load saved model and vectorizer
try:
    model_path = 'model.pkl'
    vec_path = 'vectorizer.pkl'
    
    assert os.path.exists(model_path), "Model file not found."
    assert os.path.exists(vec_path), "Vectorizer file not found."
    
    print("Loading model and vectorizer...")
    model = pickle.load(open(model_path, 'rb'))
    vec = pickle.load(open(vec_path, 'rb'))
    print("Model and vectorizer loaded successfully.")
except Exception as e:
    print("Error loading model/vectorizer:", e)
    model = None
    vec = None

class Skills(BaseModel):
    skills: str

@app.post("/predict")
def predict(skills: Skills):
    if not model or not vec:
        return {"error": "Model or vectorizer not loaded."}

    try:
        # Vectorize the input skills
        vect_input = vec.transform([skills.skills])
        # Make prediction
        prediction = model.predict(vect_input)
        print("Prediction made:", prediction[0])
        return {"role": prediction[0]}
    except Exception as e:
        print("Error during prediction:", e)
        return {"error": "Prediction failed.", "details": str(e)}

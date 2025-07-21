# SkillMatch – Job Role Recommendation Engine

SkillMatch is a full-stack AI-powered web application designed to recommend suitable job roles for users based on their current skill set. 
It combines a Machine Learning model, Python FastAPI for ML inference, a .NET backend API, and a simple HTML/JavaScript frontend to deliver intelligent job suggestions in real-time.

---

## 🚀 Features

- 🔍 Smart job role recommendations based on user-entered skills
- 🧠 Trained machine learning model (Scikit-learn) for classification
- ⚡ FastAPI backend for lightweight and efficient inference
- 🌐 Simple and responsive web interface
- 🧩 .NET API layer for integration and future scalability

---

## 📂 Project Structure

SkillMatch/
├── frontend/ # HTML/JS frontend
│ └── index.html
├── backend-dotnet/ # .NET Web API project
│ ├── SkillMatchAPI/
│ └── SkillMatch.sln
├── ml-engine/ # Python ML engine with FastAPI
│ ├── main.py
│ ├── ml_model.py
│ ├── model.pkl
│ ├── vectorizer.pkl
│ └── requirements.txt
└── README.md # Project overview and setup guide


---

## 🛠️ Tech Stack

| Layer        | Technology        |
|--------------|-------------------|
| Frontend     | HTML, CSS, JavaScript |
| Backend API  | .NET (C#)         |
| ML Engine    | Python, FastAPI   |
| ML Model     | Scikit-learn      |
| Deployment   | GitHub (in progress) |

---

## ✅ How It Works

1. The user visits the website and inputs their skill set.
2. The frontend sends this data to the .NET backend API.
3. The API forwards the request to the FastAPI ML engine.
4. The ML engine processes the input using the trained model.
5. Recommended job roles are sent back and displayed to the user.

---

## 🧪 Local Setup Guide

> Run each component independently for development.

### 🔹 Python ML Engine

```bash
cd ml-engine
pip install -r requirements.txt
uvicorn main:app --reload


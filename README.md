# 🎬 Movie Recommendation System

A Netflix-style movie recommendation system built using machine learning and a modern ML engineering architecture.

The system recommends movies similar to a given movie using collaborative filtering based on user ratings from the MovieLens dataset.

---

## 🚀 Features

- Movie recommendation using collaborative filtering
- Cosine similarity model
- FastAPI backend for ML model serving
- Streamlit frontend interface
- Real MovieLens dataset
- End-to-end ML pipeline (training → API → UI)

---

## 🧠 System Architecture

User → Streamlit UI → FastAPI Backend → ML Model → Movie Dataset

---

## 📂 Project Structure

movie-recommendation-system

data  
- u.data  
- u.item  

training  
- preprocess.py  
- train_model.py  

models  
- similarity.pkl  

api  
- main.py  

app  
- streamlit_app.py  

requirements.txt  
README.md  

---

## 📊 Dataset

This project uses the MovieLens 100K dataset.

- 100,000 ratings  
- 943 users  
- 1,682 movies  

Dataset source:

https://grouplens.org/datasets/movielens/

---

## ⚙️ Installation

Clone the repository

git clone https://github.com/YOUR_USERNAME/movie-recommendation-system.git  
cd movie-recommendation-system  

Create virtual environment

python3 -m venv ai-env  
source ai-env/bin/activate  

Install dependencies

pip install -r requirements.txt  

---

## 🧠 Train the Model

cd training  
python preprocess.py  
python train_model.py  

---

## 🚀 Run the Backend API

uvicorn api.main:app --reload  

Open API documentation:

http://127.0.0.1:8000/docs  

---

## 🎬 Run the Frontend UI

streamlit run app/streamlit_app.py  

Open the UI:

http://localhost:8501  

---

## 💡 Example Recommendation

Input:

Toy Story (1995)

Output:

Star Wars (1977)  
Return of the Jedi (1983)  
Independence Day (1996)  
Rock, The (1996)  
Mission: Impossible (1996)  

---

## 🛠 Technologies Used

Python  
Pandas  
Scikit-learn  
FastAPI  
Streamlit  
MovieLens Dataset  

---

## 📈 Future Improvements

- Movie poster integration (TMDB API)
- Hybrid recommender system
- Autocomplete search
- Cloud deployment

---

## 👨‍💻 Author

C R Ravikumar  
Machine Learning Engineer
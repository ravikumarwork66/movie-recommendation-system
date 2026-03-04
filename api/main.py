import os
import pickle
import pandas as pd
from fastapi import FastAPI

app = FastAPI()

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

model_path = os.path.join(BASE_DIR, "models", "similarity.pkl")
data_path = os.path.join(BASE_DIR, "data", "pivot_table.csv")

similarity = pickle.load(open(model_path, "rb"))
movies = pd.read_csv(data_path, index_col=0)

movie_list = list(movies.index)

@app.get("/recommend/{movie}")
def recommend(movie: str):

    idx = movie_list.index(movie)

    scores = list(enumerate(similarity[idx]))
    scores = sorted(scores, key=lambda x: x[1], reverse=True)[1:6]

    recommendations = [movie_list[i[0]] for i in scores]

    return {"recommendations": recommendations}
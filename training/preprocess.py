import pandas as pd

# ratings dataset
ratings = pd.read_csv(
    "../data/u.data",
    sep="\t",
    names=["userId", "movieId", "rating", "timestamp"]
)

# movie titles
movies = pd.read_csv(
    "../data/u.item",
    sep="|",
    encoding="latin-1",
    header=None,
    usecols=[0,1],
    names=["movieId", "title"]
)

data = pd.merge(ratings, movies, on="movieId")

pivot = data.pivot_table(
    index="title",
    columns="userId",
    values="rating"
).fillna(0)

pivot.to_csv("../data/pivot_table.csv")

print("Preprocessing done")
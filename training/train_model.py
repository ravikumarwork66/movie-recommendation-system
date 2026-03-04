import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
import pickle
import os

print("🚀 Starting model training...")

# Load data
print("📂 Loading pivot table...")
pivot = pd.read_csv("../data/pivot_table.csv", index_col=0)

print(f"✅ Data loaded: {pivot.shape[0]} movies, {pivot.shape[1]} users")

# Compute similarity
print("🧠 Computing cosine similarity matrix...")
similarity = cosine_similarity(pivot)

print("✅ Similarity matrix computed")

# Create models folder if it doesn't exist
os.makedirs("../models", exist_ok=True)

# Save model
print("💾 Saving model...")
with open("../models/similarity.pkl", "wb") as f:
    pickle.dump(similarity, f)

print("🎉 Model training complete!")
print(f"📁 Model saved at: ../models/similarity.pkl")
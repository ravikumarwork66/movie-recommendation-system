import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000"

st.set_page_config(page_title="Movie Recommender", layout="wide")

st.title("🎬 Movie Recommendation System")

st.write("Enter a movie name to get similar recommendations")

movie = st.text_input("Movie name")

if st.button("Recommend"):

    if movie == "":
        st.warning("Please enter a movie name")
    else:

        try:
            response = requests.get(f"{API_URL}/recommend/{movie}")

            if response.status_code == 200:

                data = response.json()

                st.subheader("Recommended Movies")

                for m in data["recommendations"]:
                    st.write("⭐", m)

            else:
                st.error("Movie not found")

        except:
            st.error("API server not running")
import streamlit as st
from core.loader import load_json

troops = load_json("troops.json")

st.title("⚔️ Troop Database")

st.metric("Troops Loaded", len(troops["troops"]))

st.info("Database currently empty.")
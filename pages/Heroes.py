import streamlit as st
from core.loader import load_json

heroes = load_json("heroes.json")

st.title("🦸 Hero Database")

st.metric("Heroes Loaded", len(heroes["heroes"]))

st.info("Database currently empty.")
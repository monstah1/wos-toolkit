import streamlit as st
from core.loader import load_json

heroes = load_json("heroes.json")

hero_list = heroes.get("heroes", [])

st.title("🦸 Hero Database")

st.metric("Heroes Loaded", len(hero_list))

st.info("Database currently empty.")
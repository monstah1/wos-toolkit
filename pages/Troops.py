import streamlit as st
from core.loader import load_json

troops = load_json("troops.json")

troop_list = troops.get("troops", [])

st.title("⚔️ Troop Database")

st.metric("Troops Loaded", len(troop_list))

st.info("Database currently empty.")
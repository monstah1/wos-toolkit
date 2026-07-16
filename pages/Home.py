import streamlit as st

from core.database import Database

st.title("❄️ Whiteout Survival Toolkit")

@st.cache_resource
def get_database():
    return Database()

db = get_database()

hero_count = len(db.heroes)
troop_count = len(db.troops)
gear_count = len(db.gear)
pet_count = len(db.pets)

hero_count = len(heroes.get("heroes", []))
troop_count = len(troops.get("troops", []))
gear_count = len(gear.get("gear", []))
pet_count = len(pets.get("pets", []))

col1, col2 = st.columns(2)

with col1:
    st.metric("🦸 Heroes Loaded", hero_count)
    st.metric("⚔️ Troops Loaded", troop_count)

with col2:
    st.metric("🛡️ Gear Loaded", gear_count)
    st.metric("🐺 Pets Loaded", pet_count)

st.divider()

st.subheader("Roadmap")

st.checkbox("Project Created", value=True, disabled=True)
st.checkbox("GitHub Connected", value=True, disabled=True)
st.checkbox("Streamlit Online", value=True, disabled=True)
st.checkbox("Database Engine", value=True, disabled=True)
st.checkbox("Hero Database", value=False, disabled=True)
st.checkbox("Bear Calculator", value=False, disabled=True)

st.divider()

st.caption("Version 0.2")
import streamlit as st

st.title("🐻 Bear Hunt Calculator")

st.write("### Troop Tier")

tier = st.radio(
    "Select troop tier",
    ["T11", "T12"],
    horizontal=True,
)

st.divider()

st.subheader("Infantry")

inf_troops = st.number_input(
    "Infantry Troops",
    min_value=0,
    value=0,
    step=1000,
)

inf_attack = st.number_input(
    "Infantry Attack %",
    value=1000.0,
)

inf_lethality = st.number_input(
    "Infantry Lethality %",
    value=1000.0,
)

st.divider()

st.subheader("Lancers")

lan_troops = st.number_input(
    "Lancer Troops",
    min_value=0,
    value=0,
    step=1000,
)

lan_attack = st.number_input(
    "Lancer Attack %",
    value=1000.0,
)

lan_lethality = st.number_input(
    "Lancer Lethality %",
    value=1000.0,
)

st.divider()

st.subheader("Marksmen")

mar_troops = st.number_input(
    "Marksman Troops",
    min_value=0,
    value=0,
    step=1000,
)

mar_attack = st.number_input(
    "Marksman Attack %",
    value=1000.0,
)

mar_lethality = st.number_input(
    "Marksman Lethality %",
    value=1000.0,
)

st.divider()

if st.button("Calculate"):
    st.success("Calculator engine coming next!")
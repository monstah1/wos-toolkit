import streamlit as st

st.title("🐻 Bear Hunt")

left, right = st.columns(2)

with left:

    infantry = st.number_input(
        "Infantry",
        value=0,
        step=1000
    )

    cavalry = st.number_input(
        "Lancers",
        value=0,
        step=1000
    )

with right:

    marksman = st.number_input(
        "Marksman",
        value=0,
        step=1000
    )

st.divider()

if st.button("Calculate Damage", use_container_width=True):
    st.warning("Damage engine coming next.")
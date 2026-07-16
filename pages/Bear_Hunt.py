import streamlit as st

st.title("🐻 Bear Hunt")

left, right = st.columns(2)

with left:

<<<<<<< HEAD
    infantry = st.number_input(
        "Infantry",
        value=0,
        step=1000
    )
=======
st.number_input("Lancers Attack")
>>>>>>> a55124adf1503d4e43346bab9a3c5a1f771fc4e5

    cavalry = st.number_input(
        "Lancers",
        value=0,
        step=1000
    )

<<<<<<< HEAD
with right:

    marksman = st.number_input(
        "Marksman",
        value=0,
        step=1000
    )

st.divider()

if st.button("Calculate Damage", use_container_width=True):
    st.warning("Damage engine coming next.")
=======
st.button("Calculate")
>>>>>>> a55124adf1503d4e43346bab9a3c5a1f771fc4e5

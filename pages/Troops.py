import streamlit as st

from core.database import Database


db = Database()


st.title("⚔️ Troop Database")


st.write(
    f"Troops Loaded: {len(db.troops)}"
)


st.divider()


if db.troops:

    for troop in db.troops:

        with st.expander(
            f"{troop['tier']} {troop['type']}"
        ):

            st.write(
                f"Power: {troop['power']}"
            )

            st.write(
                f"Attack: {troop['attack']}"
            )

            st.write(
                f"Defense: {troop['defense']}"
            )

            st.write(
                f"Health: {troop['health']}"
            )

            st.write(
                f"Lethality: {troop['lethality']}"
            )

            st.write(
                f"Speed: {troop['speed']}"
            )

            st.write(
                f"Load: {troop['load']}"
            )

            st.write(
                "✅ Verified"
                if troop["verified"]
                else "⚠️ Unverified"
            )

else:

    st.info("Database currently empty.")
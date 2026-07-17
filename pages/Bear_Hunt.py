import streamlit as st

from core.database import Database
from core.bear import bear_troop_damage


db = Database()


st.title("🐻 Bear Hunt Calculator")


st.write("### Troop Tier")

tier = st.radio(
    "Select troop tier",
    ["T11", "T12"],
    horizontal=True,
)


# Load troop data from database
infantry = db.get_troop(tier, "Infantry")
lancer = db.get_troop(tier, "Lancer")
marksman = db.get_troop(tier, "Marksman")


st.divider()


st.subheader("Infantry")

inf_troops = st.number_input(
    "Infantry Troops",
    min_value=0,
    value=0,
    step=1000,
)

inf_attack_bonus = st.number_input(
    "Infantry Bonus Attack %",
    value=0.0,
)

inf_lethality_bonus = st.number_input(
    "Infantry Bonus Lethality %",
    value=0.0,
)


st.divider()


st.subheader("Lancers")

lan_troops = st.number_input(
    "Lancer Troops",
    min_value=0,
    value=0,
    step=1000,
)

lan_attack_bonus = st.number_input(
    "Lancer Bonus Attack %",
    value=0.0,
)

lan_lethality_bonus = st.number_input(
    "Lancer Bonus Lethality %",
    value=0.0,
)


st.divider()


st.subheader("Marksmen")

mar_troops = st.number_input(
    "Marksman Troops",
    min_value=0,
    value=0,
    step=1000,
)

mar_attack_bonus = st.number_input(
    "Marksman Bonus Attack %",
    value=0.0,
)

mar_lethality_bonus = st.number_input(
    "Marksman Bonus Lethality %",
    value=0.0,
)


st.divider()


if st.button("Calculate"):

    infantry_damage = bear_troop_damage(
        "Infantry",
        inf_troops,
        infantry["attack"],
        inf_attack_bonus,
        inf_lethality_bonus,
    )


    lancer_damage = bear_troop_damage(
        "Lancer",
        lan_troops,
        lancer["attack"],
        lan_attack_bonus,
        lan_lethality_bonus,
    )


    marksman_damage = bear_troop_damage(
        "Marksman",
        mar_troops,
        marksman["attack"],
        mar_attack_bonus,
        mar_lethality_bonus,
    )


    total_damage = (
        infantry_damage
        + lancer_damage
        + marksman_damage
    )


    st.success(
        f"Estimated Bear Damage: {total_damage:,.0f}"
    )


    st.write("### Breakdown")

    st.write(
        f"Infantry: {infantry_damage:,.0f}"
    )

    st.write(
        f"Lancers: {lancer_damage:,.0f}"
    )

    st.write(
        f"Marksmen: {marksman_damage:,.0f}"
    )
import streamlit as st

st.title("❄️ Whiteout Survival Toolkit")

st.markdown("## Welcome")

left, right = st.columns(2)

with left:

    st.success("Toolkit Status")

    st.write("✅ Project Created")

    st.write("✅ GitHub Connected")

    st.write("✅ Streamlit Online")

with right:

    st.info("Roadmap")

    st.write("🐻 Bear Calculator")

    st.write("👥 Rally Optimizer")

    st.write("🦸 Hero Database")

    st.write("⚔️ Troop Database")

st.divider()

st.caption("Version 0.1")
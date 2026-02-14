import streamlit as st

if "value" not in st.session_state:
    st.session_state.value = 0

def add_100():
    st.session_state.value += 100

st.number_input("Test Number", key="value")

st.button("Add 100", on_click=add_100)

st.write("Current session_state value:", st.session_state.value)

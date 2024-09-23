import streamlit as st

st.title("Streamlit Demo by Amit A")

st.header("Heading of streamlit")

st.subheader("Sub - Heading of streamlit")

st.text("This is an Example text")

st.success("Success")
st.warning("Warning")
st.info("Info")
st.error("Error")

#Check box from user
if st.checkbox("Select/Unselect"):
    st.text("User selected checkbox")
else:
    st.text("User has not selected checkbox")

state = st.radio("What is your fav color?", ("Red","Green","Blue"))

if state == "Green":
    st.success("My fav color as well")

occupation = st.selectbox("What do you do?", ["student","teacher","engineer"])

st.text(f"Selected option is {occupation}")

if st.button("Example Button"):
    st.error("You Clicked it")

st.sidebar.header("Heading of sidebar")
st.sidebar.text("By Amit")
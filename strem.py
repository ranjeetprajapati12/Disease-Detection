import streamlit as st 
from PIL import Image

st.title("Welcome to Vlog with ranjeet")

st.sidebar.success("Select The page from here")
state=st.sidebar.selectbox("State",["Delhi","Bengaluru","Hydrabad","Jharkhand"])

if state=="Delhi":
    image=Image.open(r"D:\Langchain_tutorial\img\Delhi_map.png")
    col1, col2, col3 = st.columns([1, 5, 1])
    with col2:
        st.image(image, use_container_width=True)

if state=="Hydrabad":
    image=Image.open(r"D:\Langchain_tutorial\img\telangana.png")
    col1, col2, col3 = st.columns([1, 5, 1])
    with col2:
        st.image(image, use_container_width=True)

if state=="Jharkhand":
    image=Image.open(r"D:\Langchain_tutorial\img\New_Jharkhand_in_jharkhand_map.png")
    col1, col2, col3 = st.columns([1, 5, 1])
    with col2:
        st.image(image, use_container_width=True)

if state=="Bengaluru":
    image=Image.open(r"D:\Langchain_tutorial\img\bengaluru-map-slide3.png")
    col1, col2, col3 = st.columns([1, 5, 1])
    with col2:
        st.image(image, use_container_width=True)
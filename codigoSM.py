import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.markdown("""
<style>
    [data-testid=stSidebar] {
        background-color: #10609d;
    }
</style>
""", unsafe_allow_html=True)

with st.sidebar:
    st.markdown('<h1 style="color: white;">Este es un texto rojo</h1>', unsafe_allow_html=True)

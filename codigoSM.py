import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("Salud mental en trabajo remoto")
st.markdown("""
<style>
    [data-testid=stSidebar] {background-color: #10609d;}
</style>
""", unsafe_allow_html=True)

with st.sidebar:
    st.markdown("<h1 style='color: white'>Este es un texto rojo</h1>", unsafe_allow_html=True)
    boton1 = st.button("¿Cual es la relacion de nivel de  estres y modo de trabajo?")
    if boton1:
        st.write("alo")
    casil1= st.checkbox("Hola")
    if casil1:
        st.write("Casilla presionada")
        casil2 = st.checkbox("subcasilla")
        if casil2:
            casil3 = st.checkbox("Otramas")

def grafico_barra(x,y):
    x = Eje_X
    y = Eje_Y
    fig,ax = plt.subplots()
    ax.bar([Eje_X, Eje_Y], [cant_Eje_X, cant_Eje_Y], color ="#26B6A7" )
    ax.set_xlabel("Eje X")
    ax.set_ylabel("Eje Y")
    ax.set_title('Titulo')
    st.pyplot(fig)

    

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv("Impact_of_Remote_Work_on_Mental_Health.csv")
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

# Lista de columnas numéricas que podrían ser usadas para el eje Y
columnas_numericas = ["Age", "Years_of_Experience", "Hours_Worked_Per_Week", "Number_of_Virtual_Meetings", 
                      "Work_Life_Balance_Rating", "Stress_Level", "Productivity_Change", 
                      "Social_Isolation_Rating", "Satisfaction_with_Remote_Work"]

# Lista de columnas categóricas que podrían ser usadas para el eje X
columnas_categoricas = ["Gender", "Job_Role", "Work_Location", "Mental_Health_Condition", 
                        "Access_to_Mental_Health_Resources", "Company_Support_for_Remote_Work", 
                        "Physical_Activity", "Sleep_Quality"]

# Seleccionar columna para el eje X
columna_x = st.selectbox("Selecciona la columna para el eje X:", columnas_categoricas)

# Seleccionar columna para el eje Y
columna_y = st.selectbox("Selecciona la columna para el eje Y:", columnas_numericas)

# Crear el gráfico de barras
st.bar(df, x=columna_x, y=columna_y)

def grafico_barra(x,y):
    x = Eje_X
    y = Eje_Y
    fig,ax = plt.subplots()
    ax.bar([Eje_X, Eje_Y], [cant_Eje_X, cant_Eje_Y], color ="#26B6A7" )
    ax.set_xlabel("Eje X")
    ax.set_ylabel("Eje Y")
    ax.set_title('Titulo')
    st.pyplot(fig)

# Desplegamos un histograma con los datos del eje X
figg, axx = plt.subplots(figsize=(8, 5))  
axx.hist(df["Fertilizer_Used(tons)"], bins=20, color="#078385", edgecolor="#B77D26")
axx.set_xlabel("Toneladas")
axx.set_ylabel("Frecuencia")
axx.set_title("Histograma")
st.pyplot(figg)

if st.button("Cambiar eje X"):
    # Si se presiona el botón, cambia el eje X
    st.bar_chart(df, x="Age", y="Job_Role")
else:
    # Si no se presiona el botón, muestra el gráfico original
    st.bar_chart(df, x="Age", y="Work_Location")


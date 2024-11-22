import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import streamlit.components.v1 as components

df = pd.read_csv("Impact_of_Remote_Work_on_Mental_Health.csv")
st.title("Salud mental en trabajo remoto")
st.markdown("""
<style>
    [data-testid=stSidebar] {background-color: #10609d;}
</style>
""", unsafe_allow_html=True)

with st.sidebar:
    st.markdown("<h1 style='color: white'>Opciones de color</h1>", unsafe_allow_html=True)
    st.title('Reproductor Musical desde YouTube')
    
    playlist_url = "https://www.youtube.com/playlist?list=PLHLua7lnY9X-uAKqwp0T23h3A4d-ZajTO"
    playlist_id = playlist_url.split('list=')[-1]
    components.iframe(f"https://www.youtube.com/embed/videoseries?list={playlist_id}", width=300, height=200) 
    
    color_grafico = st.color_picker('Selecciona un color para el grafico','#007bff')    
    
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
st.bar_chart(df, x=columna_x, y=columna_y, color=color_grafico)


columna_trastorno = ["Depresion","Ansiedad","Burnout"]
st.selectbox("Selecciona uno de estos trastornos para saber mas de ellos",columna_trastorno)
#if columna_trastorno == "Depresión":

    # Leer el archivo PDF local
#    with open("sobre la depresi.pdf", r) as f:
 #       pdf_data = f.read()
    
    # Crear el botón de descarga para el archivo PDF local
  #  st.download_button(
  #      label="Pulsa aqui para descargar un PDF acerca de la depresion",
   #     data=,
    #    file_name="archivo_local.pdf",
  #      mime="application/pdf"
  #  )
###


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


#Variables de columnas
Edad = df["Age"]
Genero = df["Gender"]
Rol_trabajo = df["Job_Role"]
Anos_de_experiencia = df["Years_of_Experience"]
Lugar_trabajo = df["Work_Location"]
Horas_por_semana = df["Hours_Worked_Per_Week"]
Numero_reu_vir = df["Number_of_Virtual_Meetings"]
Clasi_hora_trabajo = df["Work_Life_Balance_Rating"]
Nivel_estres = df["Stress_Level"]
Condi_salud_mental = df["Mental_Health_Condition"]
acc_a_recursos_mental = df["Access_to_Mental_Health_Resources"]
Cambio_productividad = df["Productivity_Change"]
Clasi_aislam_social = df["Social_Isolation_Rating"]
Satis_trabajo_remo = df["Satisfaction_with_Remote_Work"]
apoyo_compania_trabrem= df["Company_Support_for_Remote_Work"]
acti_fisica = df["Physical_Activity"]
calidad_sueno = df["Sleep_Quality"]

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

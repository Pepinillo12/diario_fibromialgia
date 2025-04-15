import streamlit as st
import pandas as pd
from datetime import datetime

st.set_page_config(page_title="Diario de Síntomas", page_icon="📝")

st.title("📝 Diario de Síntomas - Fibromialgia")

st.markdown("Registra cómo te sientes hoy de forma rápida y sencilla.")

# Formulario
with st.form("registro_sintomas"):
    st.subheader("Selecciona cómo te sientes hoy:")

    dolor = st.slider("Nivel de Dolor", 0, 10, 5)
    cansancio = st.slider("Nivel de Cansancio", 0, 10, 5)
    animo = st.slider("Nivel de Ánimo", 0, 10, 5)

    sueño = st.radio("¿Cómo dormiste?", ["Bien", "Regular", "Mal"])
    niebla = st.radio("¿Tuviste niebla mental?", ["Sí", "No"])
    otros = st.radio("¿Tuviste otros síntomas importantes?", ["Sí", "No"])

    sintomas_extra = st.text_input("Si tuviste otros síntomas, descríbelos aquí:")
    comentarios = st.text_area("Comentarios adicionales (opcional):")

    enviado = st.form_submit_button("Guardar Registro")

# Guardar los datos
if enviado:
    fecha = datetime.now().strftime("%Y-%m-%d %H:%M")
    nuevo_registro = pd.DataFrame([{
        "Fecha": fecha,
        "Dolor": dolor,
        "Cansancio": cansancio,
        "Ánimo": animo,
        "Sueño": sueño,
        "Niebla Mental": niebla,
        "Otros Síntomas": otros,
        "Descripción de Otros Síntomas": sintomas_extra,
        "Comentarios": comentarios
    }])

    try:
        df_existente = pd.read_csv("registro_sintomas.csv")
        df_actualizado = pd.concat([df_existente, nuevo_registro], ignore_index=True)
    except FileNotFoundError:
        df_actualizado = nuevo_registro

    df_actualizado.to_csv("registro_sintomas.csv", index=False)
    st.success("✅ Registro guardado exitosamente.")

    with st.expander("Ver el registro más reciente"):
        st.dataframe(nuevo_registro)



import streamlit as st
from PIL import Image

st.title("SEGUNDA PARTE: CÁLCULO DE ABSORTIVIDAD MOLAR")
st.video("https://www.youtube.com/watch?v=zuUvQN8KXOk")

img = Image.open("espectrofotometro.png")

def medir_absorbancia(longitud, concentracion, tipo):
    datos = {
        "acida": {
            520: {0.000005: 0.12023, 0.00001: 0.19076, 0.000015: 0.26129},
            435: {0.000005: 0.051318, 0.00001: 0.059935, 0.000015: 0.068553}
        },
        "basica": {
            520: {0.000005: 0.044421, 0.00001: 0.055642, 0.000015: 0.066863},
            435: {0.000005: 0.132345, 0.00001: 0.24599, 0.000015: 0.359635}
        }
    }
    return datos[tipo].get(longitud, {}).get(concentracion, "Datos no disponibles")

if st.button("Preparar disoluciones ácidas"):
    conc = st.number_input("Coloque la concentración (en mol/L):", format="%.8f")
    st.image(img)
    if st.button("Medir (ácida)"):
        longitud = st.number_input("Ingrese la longitud de onda (nm):", step=1)
        if longitud in [435, 520]:
            conc2 = st.number_input("Ingrese la concentración para medir absorbancia:", format="%.8f", key="conc_acida")
            resultado = medir_absorbancia(longitud, conc2, "acida")
            st.write(f"Absorbancia: {resultado}")

if st.button("Preparar disoluciones básicas"):
    st.image(img)
    if st.button("Medir (básica)"):
        longitud = st.number_input("Ingrese la longitud de onda (nm):", step=1, key="long_bas")
        if longitud in [435, 520]:
            conc3 = st.number_input("Ingrese la concentración para medir absorbancia:", format="%.8f", key="conc_basica")
            resultado = medir_absorbancia(longitud, conc3, "basica")
            st.write(f"Absorbancia: {resultado}")

if st.button("Preparar buffers"):
    resp = st.text_input("¿Con qué preparás tu buffer?")
    if st.button("Verificar respuesta"):
        if resp.lower() in ["ácido acético y acetato de sodio", "acido acetico y acetato de sodio"]:
            st.success("Correcto")
            if st.button("Medir pH y absorbancia"):
                st.write("### Tabla de datos:")
                st.table({
                    "Solution": [7, 8, 9, 10],
                    "pH": [6.29, 5.97, 5.68, 5.3],
                    "λHMR": [0.204, 0.27, 0.773, 0.296],
                    "λMR-": [0.948, 0.776, 0.969, 0.279]
                })
        else:
            st.error("Respuesta incorrecta. Intenta de nuevo.")

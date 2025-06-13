
import streamlit as st
from PIL import Image
import base64

st.set_page_config(page_title="Segunda Parte - Simulador", layout="centered")

# Mostrar título y video
st.title("SEGUNDA PARTE: CÁLCULO DE ABSORTIVIDAD MOLAR")
st.video("https://www.youtube.com/watch?v=zuUvQN8KXOk")

# Cargar imagen GIF como base64
def mostrar_gif(ruta):
    file_ = open(ruta, "rb")
    contents = file_.read()
    data_url = base64.b64encode(contents).decode("utf-8")
    file_.close()
    st.markdown(f'<img src="data:image/gif;base64,{data_url}" width="400">', unsafe_allow_html=True)

# Función para mostrar absorbancia
def obtener_absorbancia(tipo, longitud, concentracion):
    data = {
        "acido": {
            520: {0.000005: 0.12023, 0.00001: 0.19076, 0.000015: 0.26129},
            435: {0.000005: 0.051318, 0.00001: 0.059935, 0.000015: 0.068553},
        },
        "basico": {
            520: {0.000005: 0.044421, 0.00001: 0.055642, 0.000015: 0.066863},
            435: {0.000005: 0.132345, 0.00001: 0.24599, 0.000015: 0.359635},
        }
    }
    return data.get(tipo, {}).get(longitud, {}).get(concentracion, "Valor no disponible")

# Botón 1: Disoluciones ácidas
with st.expander("Preparar disoluciones ácidas"):
    conc = st.number_input("Ingrese la concentración (mol/L)", format="%.8f", key="acido_conc")
    longitud = st.number_input("Ingrese la longitud de onda (nm)", step=1, key="acido_long")
    if st.button("Medir disolución ácida"):
        mostrar_gif("espectrofotometro.gif")
        if longitud in [520, 435] and conc in [0.000005, 0.00001, 0.000015]:
            absorbancia = obtener_absorbancia("acido", longitud, conc)
            st.success(f"Absorbancia: {absorbancia}")
        else:
            st.error("Datos no reconocidos. Use concentraciones: 5e-6, 1e-5, 1.5e-5 y longitudes 520 o 435 nm.")

# Botón 2: Disoluciones básicas
with st.expander("Preparar disoluciones básicas"):
    conc_b = st.number_input("Ingrese la concentración (mol/L)", format="%.8f", key="basico_conc")
    longitud_b = st.number_input("Ingrese la longitud de onda (nm)", step=1, key="basico_long")
    if st.button("Medir disolución básica"):
        mostrar_gif("espectrofotometro.gif")
        if longitud_b in [520, 435] and conc_b in [0.000005, 0.00001, 0.000015]:
            absorbancia = obtener_absorbancia("basico", longitud_b, conc_b)
            st.success(f"Absorbancia: {absorbancia}")
        else:
            st.error("Datos no reconocidos. Use concentraciones: 5e-6, 1e-5, 1.5e-5 y longitudes 520 o 435 nm.")

# Botón 3: Preparar buffers
with st.expander("Preparar Buffers"):
    st.write("¿Con qué preparás tu buffer?")
    respuesta = st.text_input("Escriba su respuesta:")
    if st.button("Verificar respuesta"):
        if "acético" in respuesta.lower() and "acetato" in respuesta.lower():
            st.success("¡Correcto!")
            if st.button("Medir pH y Absorbancia"):
                st.write("### Tabla de datos:")
                st.table({
                    "Solution": ["7", "8", "9", "10"],
                    "pH": [6.29, 5.97, 5.68, 5.30],
                    "λHMR": [0.204, 0.270, 0.773, 0.296],
                    "λMR⁻": [0.948, 0.776, 0.969, 0.279]
                })
        else:
            st.error("Respuesta incorrecta. Intente con ácido acético y acetato de sodio.")

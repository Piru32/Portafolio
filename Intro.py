from pathlib import Path

import streamlit as st


st.set_page_config(
    page_title="Portafolio | Juan José Zapata Mosquera",
    page_icon="💻",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.markdown(
    """
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@400;500;600;700&display=swap');

        html, body, h1, h2, h3, p, a, button,
        div[data-testid="stMarkdownContainer"] {
            font-family: 'Montserrat', sans-serif !important;
        }

        [data-testid="stAppViewContainer"] {
            background: #08192d;
        }

        [data-testid="stHeader"] {
            background: rgba(8, 25, 45, 0.95);
        }

        [data-testid="stSidebar"] {
            background: linear-gradient(160deg, #12345a 0%, #0a1e35 100%);
            border-right: 1px solid #294d75;
        }

        [data-testid="stSidebar"] * {
            color: #eaf3ff;
        }

        h1, h2, h3 {
            color: #f3f8ff !important;
        }

        [data-testid="stVerticalBlockBorderWrapper"] {
            background: #112943;
            border-color: #254565 !important;
            border-radius: 14px;
        }

        .stLinkButton a {
            background: #2563eb !important;
            color: #ffffff !important;
            border: 1px solid #3b82f6 !important;
            border-radius: 8px !important;
        }

        .stLinkButton a:hover {
            background: #1d4ed8 !important;
            border-color: #93c5fd !important;
        }

        [data-testid="stImage"] img {
            border-radius: 10px;
        }

        .imagen-pendiente {
            height: 170px;
            display: flex;
            justify-content: center;
            align-items: center;
            text-align: center;
            border: 1px dashed #52749e;
            border-radius: 10px;
            color: #a9c4e8;
            background: #0d223b;
            margin: 8px 0 16px;
            font-size: 0.92rem;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

# Todas las imágenes deben subirse a la misma carpeta que Intro.py.
PROYECTOS = [
    {
        "titulo": "Geometría",
        "descripcion": "Aplicación interactiva para explorar conceptos y ejercicios de geometría.",
        "url": "https://geometric-bgm7ner6du3dcqgxhduhzc.streamlit.app/",
        "imagen": "01_geometria.jpg",
    },
    {
        "titulo": "Cálculo y Gradiente",
        "descripcion": "Práctica de optimización matemática mediante el método de descenso del gradiente.",
        "url": "https://gradiente-xkdpncjc8wph6jfldsmkmg.streamlit.app/",
        "imagen": "02_gradiente_descendente.jpg",
    },
    {
        "titulo": "Computación Paralela",
        "descripcion": "Ejercicios relacionados con la ejecución de procesos y tareas en paralelo.",
        "url": "https://computacionparalela-2s8yomcfsgpfrfuxd8wf9v.streamlit.app/",
        "imagen": "03_computacion_paralela.jpg",
    },
    {
        "titulo": "Detector de Anomalías",
        "descripcion": "Herramienta orientada a detectar comportamientos atípicos dentro de los datos.",
        "url": "https://detectordeanomalias-nwhsmf2mqw6zdbnkttnwcj.streamlit.app/",
        "imagen": "04_deteccion_anomalias.jpg",
    },
    {
        "titulo": "Clasificación de Frutas",
        "descripcion": "Ejemplo de clasificación de frutas a partir de sus características.",
        "url": "https://clasfruta1-lkbwlksmhay79cptiaody8.streamlit.app/",
        "imagen": "05_clasificacion_frutas.jpg",
    },
    {
        "titulo": "Regresión Lineal",
        "descripcion": "Aplicación para analizar relaciones entre variables usando regresión lineal.",
        "url": "https://regresionlineal-xvbeqbpgtmjvenwwikq8zk.streamlit.app/",
        "imagen": "06_regresion_lineal.jpg",
    },
    {
        "titulo": "Series de Tiempo",
        "descripcion": "Exploración de datos temporales y de modelos para analizar su evolución.",
        "url": "https://seriedetiempo-287tyvgcg4dzopx5e6apwh.streamlit.app/",
        "imagen": "07_series_tiempo.jpg",
    },
    {
        "titulo": "Calidad del Aire",
        "descripcion": "Análisis y estimaciones relacionados con indicadores de calidad del aire.",
        "url": "https://calidadaire-vgbs8a5ewzxyh63btbvsxw.streamlit.app/",
        "imagen": "08_calidad_aire.jpg",
    },
    {
        "titulo": "Regresión de Lluvia",
        "descripcion": "Estimación de la probabilidad de lluvia a partir de temperatura, humedad y viento.",
        "url": "https://regresion-vecel.vercel.app/",
        "imagen": "09_regresion_lluvia.jpg",
    },
    {
        "titulo": "Regresión Logística",
        "descripcion": "Ejercicio de clasificación de datos basado en un modelo de regresión logística.",
        "url": "https://regresionlogistica-jwrhd7gsgvd29hqfbte5pa.streamlit.app/",
        "imagen": "10_regresion_logistica.jpg",
    },
    {
        "titulo": "Clasificación de Fertilidad",
        "descripcion": "Aplicación de clasificación enfocada en el análisis de la fertilidad del suelo.",
        "url": "https://clasificacionfertilidad-bvanclerv45vwdb8egrl5m.streamlit.app/",
        "imagen": "11_fertilidad_suelos.jpg",
    },
    {
        "titulo": "Regresión de Vivienda",
        "descripcion": "Estimador del valor de viviendas con regresión lineal y datos de California.",
        "url": "https://vivienda-one.vercel.app/",
        "imagen": "12_regresion_vivienda.jpg",
    },
]


with st.sidebar:
    st.title("Juan José Zapata Mosquera")
    st.subheader("Portafolio de aplicaciones")
    st.write(
        "Este espacio reúne trabajos prácticos de programación, análisis de datos "
        "y modelos matemáticos desarrollados en aplicaciones interactivas."
    )
    st.divider()
    st.write(f"**Proyectos disponibles:** {len(PROYECTOS)}")
    st.caption("Python · Streamlit · Análisis de datos")

st.title("Portafolio de proyectos")
st.write(
    "**Juan José Zapata Mosquera** | Una recopilación de aplicaciones y ejercicios "
    "para explorar distintos enfoques de programación, modelado y análisis de datos."
)
st.divider()
st.subheader("Explora los trabajos")
st.caption("Selecciona «Abrir aplicación» para visitar el proyecto correspondiente.")

columnas = st.columns(3, gap="medium")
carpeta = Path(__file__).resolve().parent

for numero, proyecto in enumerate(PROYECTOS, start=1):
    with columnas[(numero - 1) % 3]:
        with st.container(border=True):
            st.markdown(f"#### {numero}. {proyecto['titulo']}")
            ruta_imagen = carpeta / proyecto["imagen"]
            if ruta_imagen.is_file():
                st.image(str(ruta_imagen), use_container_width=True)
            else:
                st.markdown(
                    '<div class="imagen-pendiente">Imagen del proyecto pendiente</div>',
                    unsafe_allow_html=True,
                )
            st.write(proyecto["descripcion"])
            st.link_button("Abrir aplicación", proyecto["url"], use_container_width=True)

st.divider()
st.caption("Portafolio de Juan José Zapata Mosquera · Aplicaciones y proyectos académicos")

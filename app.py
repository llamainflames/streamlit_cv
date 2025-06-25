from pathlib import Path

import streamlit as st
from PIL import Image

# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "cv.pdf"
profile_pic = current_dir / "assets" / "pfp.jpg"
portfolio_images = list((current_dir / "assets" / "portfolio").glob("*.jpg"))
video_files = [current_dir / "assets" / "video1.mp4", current_dir / "assets" / "video2.mp4"]


# --- GENERAL SETTINGS ---
PAGE_TITLE = "Portafolio | Claudia Huacasi"
PAGE_ICON = "🎥"
NAME = "Claudia Huacasi"
DESCRIPTION = """
Soy una estudiante de Comunicación Audiovisual responsable, dedicada y resiliente. Mis áreas de interés son la escritura, la fotografía, la dirección de arte y el trabajo de iluminación.
"""
EMAIL = "claudiahuacasi@gmail.com"
SOCIAL_MEDIA = {
    "YouTube": "https://www.youtube.com/channel/UCBj_V-kMzKtXY_5UxsogCNQ",
    "LinkedIn": "https://www.linkedin.com/in/claudia-huacasi-66604a29a/",
    "Instagram": "https://www.instagram.com/claudisaster1782/",
    "Twitter": "https://twitter.com",
}


st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON, layout="wide")

with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)

# --- RETRACTABLE SIDEBAR ---
# Ruta a la imagen
image_path = current_dir / "assets" / "portfolio" / "eye.jpg"
eye_image = Image.open(image_path)

# Mostrar imagen en la barra lateral
st.sidebar.image(eye_image, use_container_width=True)

st.sidebar.title("Navegación")
st.sidebar.markdown("[Inicio](#claudia-huacasi)")
st.sidebar.markdown("[Habilidades](#habilidades)")
st.sidebar.markdown("[Experiencia](#experiencia)")
st.sidebar.markdown("[Portafolio](#portafolio)")
st.sidebar.markdown("[Animaciones cortas](#animaciones-cortas)")

# --- LOAD FILES ---
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)

# --- HERO SECTION ---
col1, col2 = st.columns([1, 3], gap="large")
with col1:
    st.image(profile_pic, width=250)

with col2:
    st.markdown(f"<h1 class='page-title'>{NAME}</h1>", unsafe_allow_html=True)
    st.write(DESCRIPTION)
    
    # Botón con estilo personalizado
    st.markdown("<div class='custom-button'>", unsafe_allow_html=True)
    st.download_button(
        label=" 📄 Descargar CV",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )
    st.markdown("</div>", unsafe_allow_html=True)

    st.write("📫", EMAIL)

# --- SOCIAL LINKS ---
st.write('\n')
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")

# --- EXPERIENCE & QUALIFICATIONS ---
st.write('\n')
st.markdown("<h2 class='section-title'>Habilidades</h2>", unsafe_allow_html=True)
st.markdown("""
<p style='line-height: 1.8;'>
🎭 Habilidades performativas, con 6 meses de formación y una obra presentada<br>
✒️ Manejo de programas de edición como Adobe Illustrator/Inkscape, Photoshop/Gimp, Lightroom, Premiere Pro, Audacity<br>
📊 Word avanzado y Excel intermedio<br>
🌐 Idiomas: Español, inglés, francés, portugués y Python básico
</p>
""", unsafe_allow_html=True)

# --- SKILLS ---
st.write('\n')
st.markdown("<h2 class='section-title'>Experiencia</h2>", unsafe_allow_html=True)
st.markdown("""
<p style='line-height: 1.8;'>
😴 Vamos a Mimir Bien: trabajo voluntario en el área creativa y producción de contenido<br>
ℹ️ Becas Lucet: trabajo voluntario como mentora de estudiantes en su primer ciclo académico<br>
🏞️ Asesora de turismo, independiente: guía, planificación y gestión de problemas de un grupo de turistas
</p>
""", unsafe_allow_html=True)

# --- PORTFOLIO ---
st.write('\n')
st.markdown("<h2 class='section-title'>Portafolio</h2>", unsafe_allow_html=True)
st.write("---")

cols = st.columns(3)
for i, image_path in enumerate(portfolio_images):
    with cols[i % 3]:
        st.image(image_path, use_container_width=True)

# --- Video ---
st.write('\n')
st.markdown("<h2 class='section-title'>Animaciones cortas</h2>", unsafe_allow_html=True)
st.write("---")

for video in video_files:
    with open(video, 'rb') as f:
        video_bytes = f.read()
        st.video(video_bytes)
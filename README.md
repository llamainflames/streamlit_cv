# Streamlit CV

Este repositorio contiene una aplicación web interactiva desarrollada con [Streamlit](https://streamlit.io/) para mostrar un currículum vitae digital, portafolio y recursos multimedia.

## Características
- Visualización de currículum en PDF.
- Galería de imágenes de portafolio.
- Reproducción de videos.
- Foto de perfil.
- Estilos personalizados con CSS.

## Estructura del repositorio
- `app.py`: Código principal de la aplicación Streamlit.
- `requirements.txt`: Dependencias necesarias para ejecutar la app.
- `assets/`: Recursos multimedia (PDF, imágenes, videos).
  - `cv.pdf`: Currículum en PDF.
  - `pfp.JPG`: Foto de perfil.
  - `video1.mp4`, `video2.mp4`: Videos de presentación o proyectos.
  - `portfolio/`: Imágenes del portafolio.
- `styles/main.css`: Estilos personalizados para la app.

## Instalación
1. Clona este repositorio:
   ```bash
   git clone https://github.com/tu_usuario/streamlit_cv.git
   cd streamlit_cv
   ```
2. Instala las dependencias:
   ```bash
   pip install -r requirements.txt
   ```

## Uso
Ejecuta la aplicación con:
```bash
streamlit run app.py
```

Abre el navegador en la URL que aparece en la terminal para ver la aplicación.

## Personalización
- Cambia los archivos en `assets/` para actualizar tu CV, foto, videos o imágenes del portafolio.
- Modifica `styles/main.css` para ajustar los estilos visuales.

## Licencia
Este proyecto está bajo la licencia MIT.
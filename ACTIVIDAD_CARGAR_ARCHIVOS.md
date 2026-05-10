# Actividad: Carga de archivos y captura de foto de perfil

## Importante
- El video de entrega debe realizarse en ingles.
- Debes trabajar desde la rama: `feature/actividad-cargar-archivos`.
- Duracion maxima del video: 5 minutos.

## Apoyo con IA (opcional)
Pueden usar IA para apoyarse durante la implementacion, siempre que entiendan y puedan explicar su codigo.

Herramientas sugeridas:
- Antigravity (tiene nivel gratuito).
- Cursor.
- Claude Code.
- Extension GitHub Copilot en VS Code o en cualquier IDE compatible para programar con ayuda de IA.

Recomendacion academica:
- No copien sin entender.
- Validen que la solucion funcione realmente en su proyecto.
- Deben poder explicar las decisiones tecnicas en su propio video.

## Contexto de la funcionalidad
En esta actividad trabajaran sobre una funcionalidad real de una aplicacion de autoescuela.
La feature permite asociar una foto de perfil a un estudiante desde dos fuentes:
- Imagen seleccionada desde el computador.
- Captura tomada con webcam.

La solucion completa ya existia, pero fue convertida a una version guiada con partes pendientes para que ustedes la finalicen.

## Objetivos de aprendizaje
- Entender el flujo completo de carga de archivos entre frontend y backend.
- Implementar envio de archivos con `FormData` y `multipart/form-data`.
- Consumir un action endpoint de Django REST Framework desde React.
- Integrar una captura de webcam en la UI.
- Manejar estados de modal, errores y actualizacion visual de datos.
- Aplicar validaciones basicas de archivos en cliente y servidor.

## Descripcion general de la feature
1. En el listado de estudiantes existe una accion para abrir una modal de foto.
2. En la modal se puede:
- Seleccionar una imagen local.
- Abrir la camara y capturar una foto.
3. El archivo (seleccionado o capturado) se envia al backend.
4. El backend recibe el archivo y lo asocia al estudiante.
5. El frontend actualiza la interfaz para mostrar la nueva foto.

## Tecnologias utilizadas
- Backend: Django, Django REST Framework.
- Frontend: Next.js (React), Axios.
- Manejo de archivos: `FormData`, `multipart/form-data`.
- Captura webcam: `navigator.mediaDevices.getUserMedia`, `canvas.toBlob`.

## Que partes ya estan hechas
- Modelo de estudiante con campo `profile_picture`.
- Ruta/action endpoint para `upload-picture` (expuesta en DRF).
- Estructura base de servicio en frontend para subir imagen.
- Modal con estructura visual y botones para seleccionar archivo y usar camara.
- Flujo general de navegacion en dashboard de estudiantes.

## Que deben completar en backend
1. Completar la logica del endpoint `upload_picture` en el ViewSet de estudiantes.
2. Validar presencia del archivo `profile_picture`.
3. Agregar validaciones basicas (tipo y tamano) antes de guardar.
4. Usar correctamente `StudentPictureSerializer` para persistir el archivo.
5. Retornar la respuesta esperada con el estudiante actualizado.
6. Manejar errores simples con codigos HTTP adecuados.

## Que deben completar en frontend
1. Construir correctamente `FormData` para enviar `profile_picture`.
2. Completar el llamado al action endpoint de DRF desde el servicio.
3. Finalizar la captura desde webcam (crear `File` desde `Blob`).
4. Mejorar manejo de estados en modal:
- inicio/cierre de camara,
- carga,
- error,
- archivo seleccionado.
5. Agregar validaciones basicas del archivo en cliente (tipo y tamano).
6. Actualizar visualmente la imagen del estudiante luego del guardado exitoso.
7. Integrar correctamente el resultado del modal con el listado de estudiantes.

## Archivos clave de la actividad
- `backend/academy/views.py`
- `backend/academy/serializers.py`
- `frontend/src/services/students.service.js`
- `frontend/src/components/students/UploadPictureModal.jsx`
- `frontend/src/app/dashboard/students/page.jsx`

## Como correr backend y frontend
### Backend
1. Ir a carpeta `backend/`.
2. Activar entorno virtual.
3. Instalar dependencias: `pip install -r requirements.txt`.
4. Ejecutar migraciones: `python manage.py migrate`.
5. Levantar servidor: `python manage.py runserver`.

### Frontend
1. Ir a carpeta `frontend/`.
2. Instalar dependencias: `npm install`.
3. Configurar `.env` con `NEXT_PUBLIC_API_URL=http://localhost:8000/api`.
4. Levantar frontend: `npm run dev`.

## Como probar la funcionalidad
1. Abrir `http://localhost:3000/dashboard/students`.
2. Crear o seleccionar un estudiante existente.
3. Abrir la modal de foto.
4. Probar seleccion de archivo local.
5. Probar apertura de webcam y captura.
6. Guardar y verificar que el backend reciba el archivo.
7. Confirmar que la imagen se refleje en la interfaz.

## Requisitos minimos
- La app debe compilar y levantar (backend y frontend).
- Debe ser posible subir imagen desde archivo local.
- Debe ser posible capturar imagen desde webcam.
- Debe enviarse correctamente `multipart/form-data`.
- Debe actualizarse la foto del estudiante en la UI.
- Debe existir manejo basico de errores y validaciones.

## Que deben entregar
1. Enlace a su repositorio con la solucion completa.
2. Enlace a su video en YouTube.

El video puede estar en modo:
- No listado.
- Publico.

Tambien pueden compartirlo de forma accesible solo por enlace.

## Criterios de evaluacion
- Correctitud tecnica del flujo frontend-backend.
- Implementacion de captura webcam y carga de archivo.
- Calidad del manejo de estado en React.
- Uso correcto de `FormData` y endpoint DRF.
- Validaciones basicas y manejo de errores.
- Claridad del codigo y de los TODO completados.
- Calidad de la explicacion tecnica en el video (en ingles).

## Instrucciones del video en ingles
- Deben grabar un video explicando tecnicamente la solucion en ingles.
- Deben mostrar codigo y demostracion funcional.
- Deben subir el video a YouTube y compartir el enlace.
- Duracion maxima: 5 minutos.

Formato del video:
- Opcion A (recomendada): mostrar la feature funcionando y su rostro en un recuadro durante la explicacion.
- Opcion B (alternativa): mostrar brevemente la feature funcionando y luego grabarse mostrando su rostro para la explicacion final.

Guia rapida para hacerlo facil en Windows:
1. Usar OBS Studio (gratis) para grabar pantalla + webcam en recuadro:
- Agregar una fuente de Captura de pantalla.
- Agregar una fuente de Dispositivo de captura de video (webcam).
- Redimensionar la webcam y moverla a una esquina.
- Grabar y exportar.
2. Alternativa sencilla con Clipchamp (Windows):
- Grabar pantalla.
- Agregar clip de camara.
- Colocar la camara como overlay (picture-in-picture).
3. Si prefieren Opcion B:
- Grabar primero la demo funcional.
- Grabar despues un clip corto con su rostro explicando resultados, retos y decisiones.

## Contenido obligatorio del video
En el video (en ingles) deben explicar como minimo:
1. Que hace la feature.
2. Como funciona la modal.
3. Como React maneja el estado.
4. Como se selecciona una imagen desde el computador.
5. Como se activa la webcam.
6. Como se toma la captura.
7. Como se construye el `FormData`.
8. Como React consume el endpoint de Django REST Framework.
9. Como Django recibe el archivo.
10. Como se guarda la imagen.
11. Como se actualiza la interfaz.
12. Demostracion funcional completa.
13. Que fue lo mas dificil o interesante de implementar.
14. Debe verse su rostro en recuadro durante la demo o en un segmento posterior del mismo video.

## Flujo de trabajo obligatorio
1. Trabajar desde la rama `feature/actividad-cargar-archivos`.
2. Completar la funcionalidad pendiente.
3. Subir cambios a su propio repositorio.
4. Grabar video tecnico en ingles.
5. Subir video a YouTube.
6. Entregar enlace de repositorio + enlace de video.

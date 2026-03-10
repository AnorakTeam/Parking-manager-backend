# Parking backend
Realizado para la actividad #1 del curso de Desarrollo de aplicaciones basadas en microservicios 2026-I.

Estudiantes:
- José Manuel Pérez Rodríguez - 1152375
- Erika Alejandra Sánchez Soto - 1152208
- Yarley Gilmar Guillen Rico - 1152180
- Nefer Sneyder Rojas Porras - 1152307

Se encarga de la lógica del manejo de un parking. 

El parking consiste de 3 líneas con 10 slots cada una, donde se aparcan vehículos en general.

## Modo de uso (sin autenticación)

Este backend corre en **modo single-user**: no existe login, registro ni usuarios. El frontend abre directamente el panel (`frontend/dashboard.html`) y consume el API público:

- `GET /api/parking/slots/`
- `POST /api/parking/slots/<id>/occupy/`
- `POST /api/parking/slots/<id>/free/`

Enlace a los recursos en drive:

https://drive.google.com/drive/folders/1iXF6Y5r_CcFYJcO7W62of209Db2CnXis
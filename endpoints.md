## Authentication

This service runs in **single-user mode** and does **not** require authentication.


## Parking API (`/api/parking/`)

- **GET `/api/parking/slots/`**  
  List parking slots.  
  **Query params (optional):** `line` (1, 2, or 3)  
  **Body:** none

- **GET `/api/parking/slots/<id>/`**  
  Get a single parking slot.  
  **Body:** none

- **POST `/api/parking/slots/<id>/free/`**  
  Mark slot as free.  
  **Body:** none

- **POST `/api/parking/slots/<id>/occupy/`**  
  Occupy a parking slot.  
  **Body (JSON):**  
  - `start_date` (optional, ISO datetime)  
  - `finish_date` (optional, ISO datetime; if omitted, defaults to `start_date + 24h`)

- **PATCH `/api/parking/slots/<id>/status/`**  
  Update slot fields.  
  **Body (JSON, all optional):**  
  - `status`  
  - `start_date`  
  - `finish_date`


## Admin

Not exposed in single-user mode.
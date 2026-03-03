## Authentication (Django built-in — `/accounts/`)

- **GET `/accounts/login/`**  
  Show login form.  
  **Body:** none

- **POST `/accounts/login/`**  
  Log in user.  
  **Body (form):** `username`, `password`, optional `next` (redirect URL)

- **GET `/accounts/logout/`**  
  Log out (redirect).  
  **Body:** none

- **POST `/accounts/logout/`**  
  Log out via POST (CSRF-protected).  
  **Body:** none

- **GET `/accounts/password_change/`**  
  Show change-password form.  
  **Body:** none

- **POST `/accounts/password_change/`**  
  Change password.  
  **Body (form):** `old_password`, `new_password1`, `new_password2`

- **GET `/accounts/password_change/done/`**  
  Password changed confirmation page.  
  **Body:** none

- **GET `/accounts/password_reset/`**  
  Show “forgot password” form.  
  **Body:** none

- **POST `/accounts/password_reset/`**  
  Request password reset email.  
  **Body (form):** `email`

- **GET `/accounts/password_reset/done/`**  
  “Check your email” page.  
  **Body:** none

- **GET `/accounts/reset/<uidb64>/<token>/`**  
  Show form to set new password (from email link).  
  **Body:** none

- **POST `/accounts/reset/<uidb64>/<token>/`**  
  Set new password.  
  **Body (form):** `new_password1`, `new_password2`

- **GET `/accounts/reset/done/`**  
  Password reset complete page.  
  **Body:** none


## Custom API Authentication

- **GET `/api/auth/csrf/`**  
  Return CSRF token.  
  **Body:** none  
  **Notes:** Use with credentials so the CSRF cookie is sent.

- **POST `/api/auth/register/`**  
  Register and log in user.  
  **Body (JSON):**  
  - `username` (required)  
  - `password` (required, min 8 characters)  
  - `email` (optional)


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
  **Auth:** required  
  **Body:** none

- **POST `/api/parking/slots/<id>/occupy/`**  
  Occupy a parking slot.  
  **Auth:** required  
  **Body (JSON):**  
  - `vehicle_model` (required)  
  - `start_date` (optional, ISO datetime)  
  - `finish_date` (optional, ISO datetime; if omitted, defaults to `start_date + 24h`)

- **PATCH `/api/parking/slots/<id>/status/`**  
  Update slot fields.  
  **Body (JSON, all optional):**  
  - `status`  
  - `vehicle_model`  
  - `start_date`  
  - `finish_date`


## Admin

- **GET `/admin/`**  
  Good old django admin, yep
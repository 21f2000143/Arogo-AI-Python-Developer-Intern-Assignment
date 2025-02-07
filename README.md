# Clinic360

## Setup & Run

### Stack Requirements
- **Backend Framework:** Django with Django Rest Framework(DRF)
- **Database:** PostgreSQL 16
- **Asynchronous Processing:** Celery
- **Message Broker:** Redis
- **Task Monitoring:** Flower
- **PDF Generation:** Reportlab
- **Package Management:** Poetry
- **Containerization:** Docker Compose

### Steps to Run

1. **Clone the repository**
   ```sh
   https://github.com/21f2000143/Arogo-AI-Python-Developer-Intern-Assignment.git
   cd Arogo-AI-Python-Developer-Intern-Assignment
   ```

2. **Setup and Start Docker Desktop on your machine**
[https://docs.docker.com/](https://docs.docker.com/)

3. **Run the application**
   ```sh
   docker-compose up --build
   ```

4. **Base URL of the API**
   [http://localhost:8000](http://localhost:8000)

5. **Access the flower monitor**
   Open your web browser and navigate to [http://localhost:5555](http://localhost:5555)

6. **Stop the application**
   ```sh
   docker-compose down
   ```
7. **To start the application if you have already build it**
   ```sh
   docker-compose up
   ```

## Endpoints

## API Endpoints

### User Management

- **List Users**
  - **URL:** `/user/`
  - **Method:** `GET`
  - **Description:** Retrieve a list of all users.

### Medical Records

- **Create Medical Record**
  - **URL:** `/create-record/`
  - **Method:** `POST`
  - **Description:** Create a new medical record.

- **View Patient Records**
  - **URL:** `/view-records/<patient_id>/`
  - **Method:** `GET`
  - **Description:** Retrieve medical records for a specific patient.

- **Update Medical Record**
  - **URL:** `/update-record/<pk>/`
  - **Method:** `PUT`
  - **Description:** Update a specific medical record.

- **Delete Medical Record**
  - **URL:** `/delete-record/<pk>/`
  - **Method:** `DELETE`
  - **Description:** Delete a specific medical record.

### Appointments

- **Create Appointment**
  - **URL:** `/create-appointment/`
  - **Method:** `POST`
  - **Description:** Create a new appointment.

- **View Patient Appointments**
  - **URL:** `/view-appointments/<patient_id>/`
  - **Method:** `GET`
  - **Description:** View all appointments for a specific patient.

- **View Doctor Appointments**
  - **URL:** `/view-doctor-appointments/<doctor_id>/`
  - **Method:** `GET`
  - **Description:** View all appointments for a specific doctor.

- **Update Appointment**
  - **URL:** `/update-appointment/<pk>/`
  - **Method:** `PUT`
  - **Description:** Update a specific appointment.

- **Delete Appointment**
  - **URL:** `/delete-appointment/<pk>/`
  - **Method:** `DELETE`
  - **Description:** Delete a specific appointment.

### Doctor Slots

- **Create Slot**
  - **URL:** `/create-slot/`
  - **Method:** `POST`
  - **Description:** Create a new available slot for a doctor.

- **View Doctor Slots**
  - **URL:** `/view-slots/<doctor_id>/`
  - **Method:** `GET`
  - **Description:** View all available slots for a specific doctor.

- **Update Slot**
  - **URL:** `/update-slot/<pk>/`
  - **Method:** `PUT`
  - **Description:** Update a specific doctor's slot.

- **Delete Slot**
  - **URL:** `/delete-slot/<pk>/`
  - **Method:** `DELETE`
  - **Description:** Delete a specific doctor's slot.

### Patient Registration

- **Register Patient**
  - **URL:** `/register-patient/`
  - **Method:** `POST`
  - **Description:** Register a new patient.

- **Update Patient**
  - **URL:** `/update-patient/<pk>/`
  - **Method:** `PUT`
  - **Description:** Update patient details.

- **Delete Patient**
  - **URL:** `/delete-patient/<pk>/`
  - **Method:** `DELETE`
  - **Description:** Delete a patient record.

### Doctor Registration

- **Register Doctor**
  - **URL:** `/register-doctor/`
  - **Method:** `POST`
  - **Description:** Register a new doctor.

- **Update Doctor**
  - **URL:** `/update-doctor/<pk>/`
  - **Method:** `PUT`
  - **Description:** Update doctor details.

- **Delete Doctor**
  - **URL:** `/delete-doctor/<pk>/`
  - **Method:** `DELETE`
  - **Description:** Delete a doctor record.

---



const API_BASE = 'http://127.0.0.1:8000';

function getHeader() {
  return {
    'Content-Type': 'application/json',
    'Authorization': `Bearer ${localStorage.getItem('jwt')}`
  };
}

async function fetchMedicalRecords() {
  return await fetch(`${API_BASE}/create-record/`, {
    method: 'GET',
    credentials: 'include',
    headers: getHeader()
  }).then(handleResponse);
}

async function fetchDoctorSlots() {
  return await fetch(`${API_BASE}/create-slot/`, {
    method: 'GET',
    credentials: 'include',
    headers: getHeader()
  }).then(handleResponse);
}

async function fetchAppointments() {
  return await fetch(`${API_BASE}/create-appointment/`, {
    method: 'GET',
    credentials: 'include',
    headers: getHeader()
  }).then(handleResponse);
}

async function fetchNotifications() {
  return await fetch(`${API_BASE}/notifications/`, {
    method: 'GET',
    credentials: 'include',
    headers: getHeader()
  }).then(handleResponse);
}

async function fetchPatientProfile() {
  return await fetch(`${API_BASE}/register-patient/`, {
    method: 'GET',
    credentials: 'include',
    headers: getHeader()
  }).then(handleResponse);
}

async function fetchDoctorProfile() {
  return await fetch(`${API_BASE}/register-doctor/`, {
    method: 'GET',
    credentials: 'include',
    headers: getHeader()
  }).then(handleResponse);
}

async function updateMedicalRecord(id, data) {
  return await fetch(`${API_BASE}/update-record/${id}/`, {
    method: 'PUT',
    credentials: 'include',
    headers: getHeader(),
    body: JSON.stringify(data)
  }).then(handleResponse);
}

async function updateDoctorSlot(id, data) {
  return await fetch(`${API_BASE}/update-slot/${id}/`, {
    method: 'PUT',
    credentials: 'include',
    headers: getHeader(),
    body: JSON.stringify(data)
  }).then(handleResponse);
}

async function updateAppointment(id, data) {
  return await fetch(`${API_BASE}/update-appointment/${id}/`, {
    method: 'PUT',
    credentials: 'include',
    headers: getHeader(),
    body: JSON.stringify(data)
  }).then(handleResponse);
}

async function updateNotification(id, data) {
  return await fetch(`${API_BASE}/update-notification/${id}/`, {
    method: 'PUT',
    credentials: 'include',
    headers: getHeader(),
    body: JSON.stringify(data)
  }).then(handleResponse);
}

async function updatePatientProfile(id, data) {
  return await fetch(`${API_BASE}/update-patient/${id}/`, {
    method: 'PUT',
    credentials: 'include',
    headers: getHeader(),
    body: JSON.stringify(data)
  }).then(handleResponse);
}

async function updateDoctorProfile(id, data) {
  return await fetch(`${API_BASE}/update-doctor/${id}/`, {
    method: 'PUT',
    credentials: 'include',
    headers: getHeader(),
    body: JSON.stringify(data)
  }).then(handleResponse);
}

async function deleteMedicalRecord(id) {
  return await fetch(`${API_BASE}/delete-record/${id}/`, {
    method: 'DELETE',
    credentials: 'include',
    headers: getHeader()
  }).then(handleResponse);
}

async function deleteDoctorSlot(id) {
  return await fetch(`${API_BASE}/delete-slot/${id}/`, {
    method: 'DELETE',
    credentials: 'include',
    headers: getHeader()
  }).then(handleResponse);
}

async function deleteAppointment(id) {
  return await fetch(`${API_BASE}/delete-appointment/${id}/`, {
    method: 'DELETE',
    credentials: 'include',
    headers: getHeader()
  }).then(handleResponse);
}

async function deleteNotification(id) {
  return await fetch(`${API_BASE}/delete-notification/${id}/`, {
    method: 'DELETE',
    credentials: 'include',
    headers: getHeader()
  }).then(handleResponse);
}

function handleResponse(response) {
  if (!response.ok) {
    return response.json().then(err => { throw new Error(err.msg); });
  }
  return response.json();
}

export {
  fetchMedicalRecords,
  fetchDoctorSlots,
  fetchAppointments,
  fetchNotifications,
  fetchPatientProfile,
  fetchDoctorProfile,
  updateMedicalRecord,
  updateDoctorSlot,
  updateAppointment,
  updateNotification,
  updatePatientProfile,
  updateDoctorProfile
};


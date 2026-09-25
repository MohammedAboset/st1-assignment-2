# Patient Class

class Patient:
    def __init__(self, patient_id: str, name: str):
        if not patient_id.strip():
            raise ValueError("Patient ID cannot be empty")

        if not name.strip():
            raise ValueError("Patient name cannot be empty")

        self.patient_id = patient_id
        self.name = name

    def request_appointment(self):
        pass

    def cancel_appointment(self):
        pass


# Practitioner Class

class Practitioner:
    def __init__(self, practitioner_id: str, name: str, specialty: str):
        if not practitioner_id.strip():
            raise ValueError("Practitioner ID cannot be empty")

        if not name.strip():
            raise ValueError("Practitioner name cannot be empty")

        if not specialty.strip():
            raise ValueError("Specialty cannot be empty")

        self.practitioner_id = practitioner_id
        self.name = name
        self.specialty = specialty

    def view_appointments(self):
        pass

    def manage_availability(self):
        pass


# Appointment Class

from datetime import datetime
from enum import Enum


class AppointmentStatus(Enum):
    SCHEDULED = "Scheduled"
    CANCELLED = "Cancelled"


class Appointment:
    def __init__(self, appointment_id: str, appointment_time: datetime):
        self.appointment_id = appointment_id
        self.appointment_time = appointment_time
        self._status = AppointmentStatus.SCHEDULED

    @property
    def status(self) -> AppointmentStatus:
        return self._status

    def update_appointment(self, appointment_time: datetime) -> None:
        if self._status == AppointmentStatus.CANCELLED:
            raise ValueError("Cancelled appointments cannot be updated")

        self.appointment_time = appointment_time

    def cancel_appointment(self) -> None:
        if self._status == AppointmentStatus.CANCELLED:
            raise ValueError("Appointment is already cancelled")

        self._status = AppointmentStatus.CANCELLED


# Manual Behaviour Checks

patient = Patient("P001", "John Smith")
practitioner = Practitioner("PR001", "Dr Brown", "Cardiology")
appointment = Appointment("A001", datetime(2026, 9, 23, 10, 0))

print(patient.name)
print(practitioner.name)
print(appointment.status)


appointment.cancel_appointment()
print(appointment.status)



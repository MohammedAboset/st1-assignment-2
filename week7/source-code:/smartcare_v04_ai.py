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



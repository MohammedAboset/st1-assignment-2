# Patient Class

class Patient:
    def __init__(self, patient_id, name):
        self.patient_id = patient_id
        self.name = name

    def request_appointment(self):
        pass

    def cancel_appointment(self):
        pass


# Practitioner Class

class Practitioner:
    def __init__(self, practitioner_id, name):
        self.practitioner_id = practitioner_id
        self.name = name

    def view_appointments(self):
        pass

    def manage_availability(self):
        pass


# Appointment Class

class Appointment:
    def __init__(self, appointment_id, appointment_time, status):
        self.appointment_id = appointment_id
        self.appointment_time = appointment_time
        self.status = status

    def create_appointment(self):
        pass

    def update_appointment(self):
        pass

    def cancel_appointment(self):
        pass
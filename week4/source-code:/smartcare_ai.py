appointments = []

def book_appointment(patient_name, practitioner_name, appointment_time):
    appointment = {
        "patient": patient_name,
        "practitioner": practitioner_name,
        "time": appointment_time
    }

    appointments.append(appointment)
    print("Appointment booked successfully!")

# Example usage
book_appointment("Alice Smith", "Dr. John Doe", "20 July 2024, 10:00 AM")

print(appointments)
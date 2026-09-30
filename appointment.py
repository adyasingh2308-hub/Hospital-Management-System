def view_patients():
    patients = load_data(PATIENTS_FILE)
    if not patients:
        print("No patients registered yet.")
        return

    print("\n--- Registered Patients ---")
    for p in patients:
        print(
            f"ID: {p.get('patient_id', 'N/A')} | "
            f"Name: {p.get('name', 'N/A')} | "
            f"Age: {p.get('age', 'N/A')} | "
            f"Gender: {p.get('gender', 'N/A')} | "
            f"Phone: {p.get('phone', 'N/A')}"
        )


def search_patient():
    patients = load_data(PATIENTS_FILE)
    patient_id = get_non_empty("Enter Patient ID to search: ")
    for p in patients:
        if p.get("patient_id", "").casefold() == patient_id.casefold():
            print("\nPatient found:")
            print(f"ID: {p.get('patient_id')}")
            print(f"Name: {p.get('name')}")
            print(f"Age: {p.get('age')}")
            print(f"Gender: {p.get('gender')}")
            print(f"Phone: {p.get('phone')}")
            return
    print("Patient ID not found.")


def update_patient():
    patients = load_data(PATIENTS_FILE)
    patient_id = get_non_empty("Enter Patient ID to update: ")

    for patient in patients:
        if patient.get("patient_id", "").casefold() == patient_id.casefold():
            print("Patient found. Press Enter to keep an existing value.")

            name = input(f"New name [{patient.get('name', '')}]: ").strip()
            age_text = input(f"New age [{patient.get('age', '')}]: ").strip()
            gender = input(f"New gender [{patient.get('gender', '')}]: ").strip()
            phone = input(f"New phone [{patient.get('phone', '')}]: ").strip()

            if name:
                patient["name"] = name

            if age_text:
                try:
                    age = int(age_text)
                    if not 0 <= age <= 120:
                        print("Age must be between 0 and 120. No changes saved.")
                        return
                    patient["age"] = age
                except ValueError:
                    print("Age must be a whole number. No changes saved.")
                    return

            if gender:
                patient["gender"] = gender

            if phone:
                if not phone.isdigit() or len(phone) != 10:
                    print("Phone number must contain exactly 10 digits. No changes saved.")
                    return
                patient["phone"] = phone

            save_data(PATIENTS_FILE, patients)
            print("Patient updated successfully!")
            return

    print("Patient ID not found.")


def delete_patient():
    patients = load_data(PATIENTS_FILE)
    patient_id = get_non_empty("Enter Patient ID to delete: ")

    for index, patient in enumerate(patients):
        if patient.get("patient_id", "").casefold() == patient_id.casefold():
            confirm = input(
                f"Delete patient {patient.get('name', '')}? Enter Y to confirm: "
            ).strip().upper()
            if confirm == "Y":
                patients.pop(index)
                save_data(PATIENTS_FILE, patients)
                print("Patient deleted successfully.")
            else:
                print("Deletion cancelled.")
            return

    print("Patient ID not found.")
from storage import load_data, save_data
from validation import get_non_empty, get_date

PATIENTS_FILE = "patients.json"
APPOINTMENTS_FILE = "appointments.json"


def book_appointment():
    patients = load_data(PATIENTS_FILE)
    if not patients:
        print("Register a patient before booking an appointment.")
        return

    patient_id = get_non_empty("Enter Patient ID: ")
    patient = next(
        (p for p in patients if p.get("patient_id", "").casefold() == patient_id.casefold()),
        None,
    )
    if patient is None:
        print("Patient ID not found. Please register the patient first.")
        return

    doctor = get_non_empty("Enter doctor name: ")
    date = get_date()
    time = get_non_empty("Enter appointment time (example 10:30 AM): ")

    appointments = load_data(APPOINTMENTS_FILE)
    number = 1
    existing_ids = {a.get("appointment_id") for a in appointments}
    while f"A{number:03d}" in existing_ids:
        number += 1

    appointment = {
        "appointment_id": f"A{number:03d}",
        "patient_id": patient["patient_id"],
        "patient_name": patient.get("name", ""),
        "doctor": doctor,
        "date": date,
        "time": time,
    }
    appointments.append(appointment)
    save_data(APPOINTMENTS_FILE, appointments)
    print(f"Appointment booked successfully! Appointment ID: {appointment['appointment_id']}")

def view_appointments():
    appointments = load_data(APPOINTMENTS_FILE)
    if not appointments:
        print("No appointments booked yet.")
        return

    print("\n--- Appointments ---")
    for appointment in appointments:
        print(
            f"Appointment ID: {appointment.get('appointment_id', 'N/A')} | "
            f"Patient: {appointment.get('patient_name', 'N/A')} "
            f"({appointment.get('patient_id', 'N/A')}) | "
            f"Doctor: {appointment.get('doctor', 'N/A')} | "
            f"Date: {appointment.get('date', 'N/A')} | "
            f"Time: {appointment.get('time', 'N/A')}"
        )
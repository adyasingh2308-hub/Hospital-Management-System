# Hospital Management System
import os
patients = {}
appointments = []


def register_patient():
    patient_id = input("Enter Patient Registration ID: ").strip()

    if patient_id in patients:
        print("Patient ID already registered!")
        return

    name = input("Enter patient name: ").strip()
    age = input("Enter patient age: ").strip()
    disease = input("Enter disease: ").strip()

    if not patient_id or not name or not age or not disease:
        print("All fields are required!")
        return

    patients[patient_id] = {
        "name": name,
        "age": age,
        "disease": disease
    }
    with open("patients.txt","a")as file:
        file.write(f"{patient_id},{name},{age},{disease}\n")

    print("Patient registered successfully!")


def view_patients():
    if not patients:
        print("No patients registered yet.")
        return


    print("\n--- Registered Patients ---")

    for patient_id, details in patients.items():
        print("Patient ID:", patient_id)
        print("Name:", details["name"])
        print("Age:", details["age"])
        print("Disease:", details["disease"])
        print("------------------------")


def search_patient():
    patient_id = input("Enter Patient ID to search: ").strip()

    if patient_id in patients:
        details = patients[patient_id]
        print("Patient found!")
        print("Patient ID:", patient_id)
        print("Name:", details["name"])
        print("Age:", details["age"])
        print("Disease:", details["disease"])
    else:
        print("Patient not found.")


def delete_patient():
    patient_id = input("Enter Patient ID to delete: ").strip()

    if patient_id in patients:
        del patients[patient_id]

        # Remove appointments belonging to this patient
        appointments[:] = [
            appointment for appointment in appointments
            if appointment["patient_id"] != patient_id
        ]

        print("Patient deleted successfully!")
    else:
        print("No patient found with that ID.")


def book_appointment():
    patient_id = input("Enter registered Patient ID: ").strip()

    if patient_id not in patients:
        print("Register a patient before booking appointment.")
        return

    doctor = input("Enter doctor's name: ").strip()
    date = input("Enter appointment date (DD-MM-YYYY): ").strip()
    time = input("Enter appointment time: ").strip()

    if not doctor or not date or not time:
        print("All appointment details are required!")
        return

    appointment = {
        "patient_id": patient_id,
        "patient_name": patients[patient_id]["name"],
        "doctor": doctor,
        "date": date,
        "time": time
    }

    appointments.append(appointment)
    print("Appointment booked successfully!")


def view_appointments():
    if not appointments:
        print("No appointments booked yet.")
        return

    print("\n--- All Appointments ---")

    for appointment in appointments:
        print("Patient ID:", appointment["patient_id"])
        print("Patient Name:", appointment["patient_name"])
        print("Doctor:", appointment["doctor"])
        print("Date:", appointment["date"])
        print("Time:", appointment["time"])
        print("------------------------")


def main():
    print("Current folder:",os.getcwd())
    while True:
        print("\n===== HOSPITAL MANAGEMENT SYSTEM =====")
        print("1. Register Patient")
        print("2. View Patients")
        print("3. Search Patient")
        print("4. Delete Patient")
        print("5. View Appointments")
        print("6. Book Appointment")
        print("7. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            register_patient()

        elif choice == "2":
            view_patients()

        elif choice == "3":
            search_patient()

        elif choice == "4":
            delete_patient()

        elif choice == "5":
            view_appointments()

        elif choice == "6":
            book_appointment()

        elif choice == "7":
            print("Thank you for using Hospital Management System!")
            break

        else:
            print("Invalid choice! Please enter a number from 1 to 7:")

if __name__ == "__main__":
    main()
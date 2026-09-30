from storage import load_data, save_data
from validation import get_non_empty, get_age, get_phone

PATIENTS_FILE = "patients.json"


def register_patient():
    patients = load_data(PATIENTS_FILE)
    patient_id = get_non_empty("Enter Patient ID(example P101):")
    for patient in patients:
          patient_id = get_non_empty("Enter Patient ID (example P101): ")

    # Check whether the patient ID already exists
    for patient in patients:
      if  patient.get("patient_id", "").lower() == patient_id.lower():
            print("Patient ID already exists!")
    return

    name = get_non_empty("Enter patient name: ")
    age = get_age()
    gender = get_non_empty("Enter gender: ")
    phone = get_phone()

    patient = {
        "patient_id": patient_id,
        "name": name,
        "age": age,
        "gender": gender,
        "phone": phone
    }
    
    patient.append(patient)
    save_data(PATIENTS_FILE, patients)

    print("\nPatient registered successfully!")



def view_patients():
    patients = load_data(PATIENTS_FILE)

    if not patients:
        print("No patients registered yet.")
        return

    print("\n--- Registered Patients ---")

    for patient in patients:
        print("----------------------------")
        print("Patient ID:", patient.get("patient_id", ""))
        print("Name:", patient.get("name", ""))
        print("Age:", patient.get("age", ""))
        print("Gender:", patient.get("gender", ""))
        print("Phone:", patient.get("phone", ""))


def search_patient():
    patients = load_data(PATIENTS_FILE)

    patient_id = get_non_empty("Enter Patient ID to search: ")

    for patient in patients:
        if patient.get("patient_id", "").lower() == patient_id.lower():
            print("\nPatient found!")
            print("Patient ID:", patient.get("patient_id", ""))
            print("Name:", patient.get("name", ""))
            print("Age:", patient.get("age", ""))
            print("Gender:", patient.get("gender", ""))
            print("Phone:", patient.get("phone", ""))
            return

    print("Patient ID not found.")


def update_patient():
    patients = load_data(PATIENTS_FILE)

    if not patients:
        print("No patients available to update.")
        return

    patient_id = get_non_empty("Enter Patient ID to update: ")

    for patient in patients:
        if patient.get("patient_id", "").lower() == patient_id.lower():

            print("\nPatient found!")
            print("Press Enter to keep the existing value.")

            name = input(
                f"New name [{patient.get('name', '')}]: "
            ).strip()

            age = input(
                f"New age [{patient.get('age', '')}]: "
            ).strip()

            gender = input(
                f"New gender [{patient.get('gender', '')}]: "
            ).strip()

            phone = input(
                f"New phone [{patient.get('phone', '')}]: "
            ).strip()

            if name:
                patient["name"] = name

            if age:
                try:
                    age_number = int(age)
                    if not 0 <= age_number <= 120:
                        print("Age must be between 0 and 120.")
                        return
                    patient["age"] = age_number
                except ValueError:
                    print("Please enter a valid age.")
                    return

            if gender:
                patient["gender"] = gender

            if phone:
                if not phone.isdigit() or len(phone) != 10:
                    print("Phone number must contain 10 digits.")
                    return
                patient["phone"] = phone

            save_data(PATIENTS_FILE, patients)
            print("Patient updated successfully!")
            return

    print("Patient ID not found.")


def delete_patient():
    patients = load_data(PATIENTS_FILE)

    if not patients:
        print("No patients available to delete.")
        return

    patient_id = get_non_empty("Enter Patient ID to delete: ")

    for index, patient in enumerate(patients):
     if patient.get("patient_id", "").lower() == patient_id.lower():
         del patients[index]
         print("Patient deleted successfully.")
         break
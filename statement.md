# Problem Statement
## Hospital Patient Management System

### Introduction
Hospitals need an organized way to maintain patient
information and appointment records. Manual record keeping
can make searching and updating information time-consuming.

### Problem
Maintaining patient records manually can lead to misplaced
information, repeated entries, and difficulties in retrieving
records. A simple computer-based system can help organize
basic information.

### Proposed Solution
The Hospital Patient Management System is a Python console
application that stores patient and appointment details in
JSON files. It provides a menu for registration, searching,
viewing, updating, deleting, and appointment management.

### Objectives
1. Create unique patient records.
2. Make patient information easy to search.
3. Allow permitted updates to patient details.
4. Manage basic hospital appointments.
5. Save data so it remains available after restarting.
6. Validate user input and display clear messages.

### Functional Requirements
- Register a patient.
- Display all patients.
- Search by patient ID.
- Update patient information.
- Delete a patient after confirmation.
- Book an appointment for a registered patient.
- Display all appointments.
- Exit the application.

### Non-Functional Requirements
- Usability: Provide a simple menu.
- Reliability: Save records to JSON files.
- Maintainability: Separate features into Python modules.
- Validation: Reject invalid age, contact number, and date
  formats.
- Privacy: Use fictional information for this demonstration.

### Tools and Technologies
- Python programming language
- JSON file storage
- Visual Studio Code

### Expected Outcome
The system should allow users to manage sample patient
records and appointments through a terminal menu, with
changes saved between program runs.

### Scope and Limitations
This project demonstrates basic record management only.
It is not a complete hospital information system and does
not include login authentication, medical diagnosis, billing,
or secure handling of real patient information.

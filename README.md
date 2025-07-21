Filename: Kobe.Blake-Readme-ITT103-SU2025.txt

Authors:
  Kobe Blake

Date Created:
  July 20, 2025

Course:
  ITT103 – Introduction to Programming

GitHub Public URL to Code:
  https://github.com/kb29dev/hms-python-cli

------------------------------------------------------------
PURPOSE
------------------------------------------------------------
This Python application implements a console-based Hospital Management System (HMS). It demonstrates:
- Object-oriented design (Person, Patient, Doctor, Appointment, HospitalSystem)
- Modular functions for ID generation, input validation, and menu display
- Exception handling for invalid inputs and schedule conflicts
- Formatted console output for profiles, schedules, appointment lists, and billing receipts

The system allows users to register patients and doctors, book or cancel appointments without double-booking, and generate itemized bills.

------------------------------------------------------------
HOW TO RUN
------------------------------------------------------------
1. Ensure Python 3.6+ is installed on your machine.
2. Clone the repository:
     git clone https://github.com/kb29dev/hms-python-cli.git
3. Change into the project directory:
     cd hms-python-cli
4. Run the main program:
     python Blake.Kobe-HMS_Program-ITT103-SP2025.py
5. Follow on-screen menus to manage patients, doctors, appointments, and billing.

------------------------------------------------------------
REQUIRED MODIFICATIONS
------------------------------------------------------------
- Update CONSULTATION_FEE constant in Blake.Kobe-HMS_Program-ITT103-SP2025.py to change the base consultation charge.
- Modify the hospital name and address in the generate_bill() method header.
- Adjust input prompts or date/time parsing to enforce stricter formats (e.g., use datetime.strptime()).
- Integrate persistent storage (SQLite, JSON, etc.) by replacing in-memory dictionaries.

------------------------------------------------------------
ASSUMPTIONS & LIMITATIONS
------------------------------------------------------------
- All data is stored in memory; exiting the program will clear registered patients, doctors, and appointments.
- Date and time are accepted as simple strings (YYYY-MM-DD and HH:MM) without timezone handling or format validation.
- Single-user, CLI-only interface; no concurrency control or authentication.
- The schedule for each doctor is defined at creation and cannot be dynamically extended within a session.
- No automated tests are included; future improvements should add unit tests for core logic.

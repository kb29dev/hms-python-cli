#!/usr/bin/env python3
# specify Python 3 interpreter for executing this script

# Hospital Management System (CLI-Based)
# console-driven HMS for Blake Memorial Hospital
# features: patient registration, doctor registration,
# appointment booking/cancellation, billing with fees

import sys
# import sys to enable system-specific functions (e.g., exit)

import datetime  # for parsing dates and calculating ages
# import datetime module to handle date objects and operations

CONSULTATION_FEE = 3000  # JMD$


# -----------------------------------------------------------------------------
# Base Class: Person
# -----------------------------------------------------------------------------
class Person:
    # base class for storing common personal information
    def __init__(self,
                 first_name: str,
                 middle_name: str,
                 last_name: str,
                 dob: str,
                 age: int,
                 gender: str):
        # store first name
        self.first_name = first_name
        # store middle name
        self.middle_name = middle_name
        # Store last name
        self.last_name = last_name
        # store date of birth as string 
        self.dob = dob
        # store age
        self.age = age
        # store gender
        self.gender = gender
        
    # return a single-line summary of the person’s details 
    def display(self) -> str:
         # concatenate name parts and remove extra spaces    
        full = f"{self.first_name} {self.middle_name} {self.last_name}".strip()
        # format and return the summary string
        return (f"Name: {full} | DOB: {self.dob} | "
                f"Age: {self.age} | Gender: {self.gender}")


# -----------------------------------------------------------------------------
# Subclass: Patient
# -----------------------------------------------------------------------------
class Patient(Person):
   # define Patient class that extends Person to include medical system details
    def __init__(self,
                 fn: str, mn: str, ln: str,
                 dob: str, age: int, gender: str,
                 address: str, telephone: str,
                 pob: str, occupation: str, employer: str,
                 father_fn: str, father_ln: str,
                 mother_fn: str, mother_ln: str,
                 ward: str, union_status: str, religion: str,
                 nok_fn: str, nok_ln: str,
                 nok_address: str, nok_relation: str, nok_phone: str,
                 patient_id: str):
        super().__init__(fn, mn, ln, dob, age, gender)
        
        # store street address for patient
        self.address = address
        # store patient telephone number as string of digits
        self.telephone = telephone
        # store place of birth
        self.place_of_birth = pob
        # store current occupation
        self.occupation = occupation
        # store employer name
        self.employer = employer
        # combine father's first and last names into one string
        self.father_name = f"{father_fn} {father_ln}"
        # combine mother's first and last names into one string
        self.mother_name = f"{mother_fn} {mother_ln}"
        # store ward assignment or region
        self.ward = ward
        # store marital or union status
        self.union_status = union_status
        # store declared religion
        self.religion = religion
        # combine NOK's first and last names
        self.nok_name = f"{nok_fn} {nok_ln}"
        # store next-of-kin address
        self.nok_address = nok_address
        # store relation of NOK to patient
        self.nok_relation = nok_relation
        # store NOK telephone number
        self.nok_phone = nok_phone
        # assign the auto-generated patient ID
        self.patient_id = patient_id
        # initialize empty list to hold Appointment objects for this patient
        self.appointment_list = []


    def view_profile(self) -> None:
        # display a header with the patient’s unique ID
        print(f"\n--- Patient Profile [{self.patient_id}] ---")
        # call Person.display() to show name, DOB, age, gender
        print(self.display())
        # print stored address
        print(f"Address          : {self.address}")
        # print stored telephone number
        print(f"Telephone        : {self.telephone}")
        # print place of birth
        print(f"Place of Birth   : {self.place_of_birth}")
        # print occupation
        print(f"Occupation       : {self.occupation}")
        # print employer
        print(f"Employer         : {self.employer}")
        # print father's name
        print(f"Father's Name    : {self.father_name}")
        # print mother's name
        print(f"Mother's Name    : {self.mother_name}")
        # print ward
        print(f"Ward             : {self.ward}")
        # print union status
        print(f"Union Status     : {self.union_status}")
        # print religion
        print(f"Religion         : {self.religion}")
        # label next-of-kin block
        print("Next of Kin:")
        # print NOK name
        print(f"  Name           : {self.nok_name}")
        # print NOK address
        print(f"  Address        : {self.nok_address}")
        # print NOK relation
        print(f"  Relation       : {self.nok_relation}")
        # print NOK telephone
        print(f"  Telephone      : {self.nok_phone}\n")
        # if there are no appointments in the list
        if not self.appointment_list:
            # inform user no appointments booked
            print("No appointments booked.\n")
        else:
            # otherwise list all booked appointments
            print("Appointments:")
            for appt in self.appointment_list:
                # print ID, doctor’s name, date/time, and status
                print(f"  • {appt.appointment_id}: Dr. {appt.doctor.first_name} "
                      f"{appt.doctor.last_name} @ {appt.date} {appt.time} "
                      f"[{appt.status}]")
            # blank line after listing
            print()


# -----------------------------------------------------------------------------
# Subclass: Doctor
# -----------------------------------------------------------------------------
class Doctor(Person):
    # define Doctor class that extends Person but hides DOB/age
    def __init__(self,
                 first_name: str,
                 last_name: str,
                 gender: str,
                 doctor_id: str,
                 speciality: str,
                 schedule: list):
        # call Person.__init__ with empty middle name, DOB, and age=0
        super().__init__(first_name, "", last_name, "", 0, gender)
        # assign auto-generated doctor ID
        self.doctor_id = doctor_id
        # store medical speciality
        self.speciality = speciality
        # store list of available (date, time) tuples
        self.schedule = schedule

    def is_available(self, date: str, time: str) -> bool:
        # return True if the given slot exists in schedule
        return (date, time) in self.schedule

    def book_slot(self, date: str, time: str) -> None:
        # remove a booked slot from schedule
        self.schedule.remove((date, time))

    def cancel_slot(self, date: str, time: str) -> None:
        # add a canceled slot back into schedule
        self.schedule.append((date, time))

    def view_profile(self) -> None:
        # build full name string
        full = f"{self.first_name} {self.last_name}"
        # header with doctor ID
        print(f"\n--- Doctor Profile [{self.doctor_id}] ---")
        # display name with Dr. prefix
        print(f"Name       : Dr. {full}")
        # display gender
        print(f"Gender     : {self.gender}")
        # display speciality
        print(f"Speciality : {self.speciality}\n")

    def view_schedule(self) -> None:
        # list available slots
        print("Available Slots:")
        # if no slots left
        if not self.schedule:
            # indicate none available
            print("  • No slots available.\n")
        else:
            # otherwise iterate sorted slots
            for date, time in sorted(self.schedule):
                # print each slot
                print(f"  • {date} {time}")
            # blank line after schedule
            print()


# -----------------------------------------------------------------------------
# Class: Appointment
# -----------------------------------------------------------------------------
class Appointment:
    # define Appointment linking Patient + Doctor at date/time
    def __init__(self,
                 appointment_id: str,
                 patient: Patient,
                 doctor: Doctor,
                 date: str,
                 time: str):
        # store unique appointment ID
        self.appointment_id = appointment_id
        # reference Patient object
        self.patient = patient
        # reference Doctor object
        self.doctor = doctor
        # store appointment date string
        self.date = date
        # store appointment time string
        self.time = time
        # initial status set to "Scheduled"
        self.status = "Scheduled"

    def confirm(self) -> None:
        # mark this appointment as confirmed
        self.status = "Confirmed"

    def cancel(self) -> None:
        # mark this appointment as canceled
        self.status = "Canceled"


# -----------------------------------------------------------------------------
# Core System / Class Hospital System
# -----------------------------------------------------------------------------
class HospitalSystem:
    # manage collections of patients, doctors, appointments
    def __init__(self):
        # dictionary patient_id -> Patient instance
        self.patients = {}
        # dictionary doctor_id  -> Doctor instance
        self.doctors = {}
        # dictionary appointment_id -> Appointment instance
        self.appointments = {}
        # counters for auto-generating IDs
        self._pcounter = 0
        self._dcounter = 0
        self._acounter = 0

    def _generate_id(self, prefix: str) -> str:
        # generate zero-padded IDs based on prefix
        if prefix == "P":
            self._pcounter += 1
            return f"P{self._pcounter:03}"
        if prefix == "D":
            self._dcounter += 1
            return f"D{self._dcounter:03}"
        if prefix == "A":
            self._acounter += 1
            return f"A{self._acounter:03}"
        # error if unknown prefix supplied
        raise ValueError("Unknown ID prefix")

    def add_patient(self) -> None:
        # start patient registration sequence
        print("\n-- Register New Patient --")

        # prompt for and validate each name part
        fn = get_alpha("First Name        : ")
        mn = get_alpha("Middle Name       : ")
        ln = get_alpha("Last Name         : ")

        # loop until DOB and age match
        while True:
            # get valid date object for DOB
            dob_date = get_dob("Date of Birth (YYYY-MM-DD): ")
            # get integer age
            age = get_int("Age               : ")
            # calculate age from DOB
            calc_age = compute_age(dob_date)
            # if mismatch between entered and calculated age
            if calc_age != age:
                print(f"Invalid age; calculated age is {calc_age} based on DOB.")
                continue
            # convert date object back to ISO string
            dob_str = dob_date.isoformat()
            break

        # prompt for gender and contact details
        gender = input("Gender            : ").strip()
        address = input("Address           : ").strip()
        telephone = get_phone("Telephone Number  : ")
        pob = input("Place of Birth    : ").strip()
        occupation = input("Occupation        : ").strip()
        employer = input("Employer          : ").strip()
        # ward, union status, religion are patient-level fields
        ward = input("Ward               : ").strip()
        union_status = input("Union Status       : ").strip()
        religion = input("Religion           : ").strip()

        # parental names, validated alphabetically
        print("\n-- Parental Details --")
        father_fn = get_alpha("Father's First Name: ")
        father_ln = get_alpha("Father's Last Name : ")
        mother_fn = get_alpha("Mother's First Name: ")
        mother_ln = get_alpha("Mother's Last Name : ")

        # next-of-kin information
        print("\n-- Next of Kin (NOK) Details --")
        nok_fn = get_alpha("NOK First Name     : ")
        nok_ln = get_alpha("NOK Last Name      : ")
        nok_address = input("NOK Address        : ").strip()
        nok_relation = input("NOK Relation       : ").strip()
        nok_phone = get_phone("NOK Telephone No.  : ")
        
        # generate unique patient ID
        pid = self._generate_id("P")
        # create Patient instance with all collected data
        patient = Patient(
            fn, mn, ln,              # name parts
            dob_str, age, gender,    # DOB, age, gender
            address, telephone,      # contact info
            pob, occupation, employer,# additional patient info
            father_fn, father_ln,    # father's name
            mother_fn, mother_ln,    # mother's name
            ward, union_status, religion,                  # social info
            nok_fn, nok_ln, nok_address, nok_relation,    # next-of-kin name & details
            nok_phone, pid           # NOK phone and patient ID
        )
        # store patient in system dictionary
        self.patients[pid] = patient
        # confirm registration to user
        print(f"\nPatient registered. Patient ID: {pid}\n")
        
    def add_doctor(self) -> None:
        # begin the doctor registration process
        print("\n-- Register New Doctor --")  

        # prompt for the doctor's first name
        fn = input("First Name       : ").strip()  
        # prompt for the doctor's last name
        ln = input("Last Name        : ").strip()  
        # prompt for the doctor's gender
        gender = input("Gender           : ").strip()  
        # prompt for the doctor's specialty
        speciality = input("Speciality       : ").strip()  

        # inform user how to enter available schedule slots
        print("Enter available slots (YYYY-MM-DD HH:MM). Type 'done' to finish.")
        # initialize empty list to hold (date, time) tuples
        schedule = []  
        # loop until the user types 'done'
        while True:  
            # read a slot entry from the user
            slot = input("Slot              : ").strip()  
            # if the user indicates completion, exit loop
            if slot.lower() == "done":  
                break  
            try:
                # split the input into date and time components
                date, time = slot.split()  
                # append the tuple to the schedule list
                schedule.append((date, time))  
            except ValueError:
                # notify user if the input is not in the correct format
                print("Format error; use 'YYYY-MM-DD HH:MM'.")  

        # generate a new unique doctor ID
        did = self._generate_id("D")  
        # instantiate a Doctor object with collected information
        doctor = Doctor(fn, ln, gender, did, speciality, schedule)  
        # add the new doctor to the system's dictionary
        self.doctors[did] = doctor  
        # confirm successful registration and display the new ID
        print(f"\nDoctor registered. Doctor ID: {did}\n")

    def book_appointment(self, patient_id: str,
                         doctor_id: str, date: str, time: str) -> None:
        # Attempt to book and confirm an appointment given IDs and slot

        # Check that the patient ID exists in the system
        if patient_id not in self.patients:
            print("Error: Patient ID not found.\n")  # notify missing patient
            return  # abort booking

        # Check that the doctor ID exists in the system
        if doctor_id not in self.doctors:
            print("Error: Doctor ID not found.\n")  # notify missing doctor
            return  # abort booking

        # Retrieve Patient and Doctor objects by their IDs
        patient = self.patients[patient_id]
        doctor = self.doctors[doctor_id]

        # Verify the doctor is available at the requested date/time
        if not doctor.is_available(date, time):
            print("Error: Doctor not available at that slot.\n")  # slot taken or invalid
            return  # abort booking

        # Generate a unique appointment ID
        aid = self._generate_id("A")

        # Create the Appointment object and mark it confirmed
        appt = Appointment(aid, patient, doctor, date, time)
        appt.confirm()  # set status to "Confirmed"

        # Store the appointment in the system registry
        self.appointments[aid] = appt

        # Link this appointment to the patient's record
        patient.appointment_list.append(appt)

        # Remove the booked slot from the doctor's schedule
        doctor.book_slot(date, time)

        # Inform the user that booking succeeded
        print(f"Appointment confirmed. ID: {aid}\n")

    def cancel_appointment(self, appointment_id: str) -> None:
        # Cancel an appointment and restore the doctor's slot.
        """Cancel an appointment and restore doctor's slot."""
        
        # If the appointment ID is not registered, show error and exit.
        if appointment_id not in self.appointments:
            print("Error: Appointment ID not found.\n"); return
        
        # Retrieve the Appointment object from the system.
        appt = self.appointments[appointment_id]
        
        # If the appointment is already marked canceled, notify and exit.
        if appt.status == "Canceled":
            print("Error: Already canceled.\n"); return
        
        # Mark the appointment status as canceled.
        appt.cancel()
        
        # Return the slot back to the doctor's availability.
        appt.doctor.cancel_slot(appt.date, appt.time)
        
        # Inform the user that cancellation succeeded.
        print(f"Appointment {appointment_id} canceled.\n")

    def view_appointments(self) -> None:
        # List all appointments with status.
        if not self.appointments:
            # If no appointments are in the system, inform the user and exit.
            print("\nNo appointments scheduled.\n"); return

        # Print a header for the appointments list.
        print("\n--- All Appointments ---")

        # Loop through each Appointment object stored in the system.
        for appt in self.appointments.values():
            # Display appointment details: ID, patient name, doctor name,
            # date, time, and current status.
            print(f"{appt.appointment_id}: Patient {appt.patient.first_name} "
                  f"{appt.patient.last_name} | Doctor {appt.doctor.first_name} "
                  f"{appt.doctor.last_name} | {appt.date} {appt.time} "
                  f"| {appt.status}")

        # Print a blank line to separate from subsequent output.
        print()

    def generate_bill(self, appointment_id: str) -> None:
        
        #Print formatted receipt for confirmed appointment:
           #Hospital header
           #Consultation fee + additional services
           #Dynamic column widths + thousands separators
        
        if appointment_id not in self.appointments:
            print("Error: Appointment ID not found.\n"); return
        appt = self.appointments[appointment_id]
        if appt.status != "Confirmed":
            print("Error: Only confirmed appointments can be billed.\n"); return

        items = [("Consultation Fee", CONSULTATION_FEE)]
        while True:
            svc = input("Enter extra service (blank to finish): ").strip()
            if not svc:
                break
            fee = get_int(f"Fee for '{svc}' (JMD$): ")
            items.append((svc, fee))

        # Compute widths
        hdr_svc = "Service"; hdr_amt = "Amount (JMD$)"
        max_s = max(len(hdr_svc), *(len(s) for s, _ in items))
        max_a = max(len(hdr_amt), *(len(f"{f:,}") for _, f in items))
        total = sum(f for _, f in items)
        width = max_s + max_a + 5

        # Print header
        name = "Blake Memorial Hospital"
        print("\n" + "=" * width)
        print(name.center(width))
        print("OFFICIAL RECEIPT".center(width))
        print("=" * width + "\n")

        # Details
        print(f"Appointment ID : {appointment_id}")
        print(f"Date/Time      : {appt.date}   {appt.time}")
        print(f"Patient        : {appt.patient.first_name} {appt.patient.last_name} ({appt.patient.patient_id})")
        print(f"Doctor         : Dr. {appt.doctor.first_name} {appt.doctor.last_name} ({appt.doctor.doctor_id})")
        print("-" * width)

        # Table
        print(f"{hdr_svc:<{max_s}}   {hdr_amt:>{max_a}}")
        print("-" * width)
        for s, f in items:
            print(f"{s:<{max_s}}   {f:>{max_a},}")
        print("-" * width)
        print(f"{'TOTAL':<{max_s}}   {total:>{max_a},}")
        print("=" * width + "\n")


# -----------------------------------------------------------------------------
# Utility Validators
# -----------------------------------------------------------------------------

def get_int(prompt: str) -> int:
    # repeatedly prompt until user enters a valid integer
    while True:
        val = input(prompt).strip()
        # read input and remove surrounding whitespace
        if val.isdigit():
            # if input contains only digits
            return int(val)
            # convert to integer and return
        print("Invalid input; enter a number.")
        # inform user and repeat on invalid input


def get_digits(prompt: str) -> str:
    # repeatedly prompt until user enters digits only
    while True:
        val = input(prompt).strip()
        # read input and trim whitespace
        if val.isdigit():
            # if all characters are digits
            return val
        print("Invalid input; only digits allowed.")
        # reject any non-digit input


def get_phone(prompt: str) -> str:
    # prompt until user enters at least 10 digits for a phone number
    while True:
        tel = input(prompt).strip()
        # read and strip whitespace
        if tel.isdigit() and len(tel) >= 10:
            # ensure numeric and minimum length
            return tel
        print("Invalid telephone number; must be at least 10 digits.")
        # reject input not meeting criteria


def get_alpha(prompt: str) -> str:
    # prompt until user enters letters, spaces, or hyphens only
    while True:
        val = input(prompt).strip()
        # trim whitespace
        cleaned = val.replace(" ", "").replace("-", "")
        # remove spaces and hyphens for validation
        if cleaned.isalpha():
            # ensure remaining characters are alphabetic
            return val
        print("Invalid input; please enter letters only.")
        # reject any numeric or symbolic characters


def get_dob(prompt: str) -> datetime.date:
    # prompt until user enters a date in YYYY-MM-DD format
    while True:
        val = input(prompt).strip()
        # trim whitespace
        try:
            dob = datetime.datetime.strptime(val, "%Y-%m-%d").date()
            # parse string into date object
            return dob
        except ValueError:
            # catch parsing errors
            print("Invalid date format; please use YYYY-MM-DD.")
            # inform user of correct format


def compute_age(dob: datetime.date) -> int:
    # calculate age in full years from date of birth
    today = datetime.date.today()
    # get today's date
    years = today.year - dob.year
    # initial year difference
    if (today.month, today.day) < (dob.month, dob.day):
        # subtract one if birthday hasn't occurred yet this year
        years -= 1
    return years
    # return computed age


# -----------------------------------------------------------------------------
# CLI Menus & Main Loop
# -----------------------------------------------------------------------------
def main_menu() -> None:
    # Display main menu and prompt for choice
    print("=== Hospital Management System ===")
    print("1) Patient Management")
    print("2) Doctor Management")
    print("3) Appointment Scheduling")
    print("4) Billing")
    print("5) Exit")


def patient_menu() -> None:
    # Display patient menu and prompt for choice
    print("\n-- Patient Management --")
    print("1) Register New Patient")
    print("2) View Patient Profile")
    print("3) Back")


def doctor_menu() -> None:
    # Display doctor menu and prompt for choice
    print("\n-- Doctor Management --")
    print("1) Register New Doctor")
    print("2) View Doctor Profile & Schedule")
    print("3) Back")


def appointment_menu() -> None:
    # Display appointment menu and prompt for choice
    print("\n-- Appointment Scheduling --")
    print("1) Book Appointment")
    print("2) View All Appointments")
    print("3) Cancel Appointment")
    print("4) Back")


def billing_menu() -> None:
    # Display billing menu and prompt for choice
    print("\n-- Billing --")
    print("1) Generate Bill")
    print("2) Back")


def main() -> None:
    # create an instance of HospitalSystem to manage data and operations
    hs = HospitalSystem()

    # enter the main interactive loop
    while True:
        # display the top-level menu options
        main_menu()
        # prompt user for a main menu choice and strip whitespace
        choice = input("Select option: ").strip()

        if choice == "1":
            # if user selects Patient Management, enter its sub-loop
            while True:
                # display patient management submenu
                patient_menu()
                # prompt user for a patient submenu choice
                sub = input("Choice: ").strip()
                if sub == "1":
                    # register a new patient
                    hs.add_patient()
                elif sub == "2":
                    # prompt for existing patient ID
                    pid = input("Patient ID: ").strip()
                    if pid in hs.patients:
                        # if found, display patient profile
                        hs.patients[pid].view_profile()
                    else:
                        # otherwise, inform user of invalid ID
                        print("Patient not found.\n")
                elif sub == "3":
                    # go back to the main menu
                    break
                else:
                    # handle invalid submenu input
                    print("Invalid choice.\n")

        elif choice == "2":
            # if user selects Doctor Management, enter its sub-loop
            while True:
                # display doctor management submenu
                doctor_menu()
                # prompt user for a doctor submenu choice
                sub = input("Choice: ").strip()
                if sub == "1":
                    # register a new doctor
                    hs.add_doctor()
                elif sub == "2":
                    # prompt for existing doctor ID
                    did = input("Doctor ID: ").strip()
                    if did in hs.doctors:
                        # if found, display doctor profile and schedule
                        doc = hs.doctors[did]
                        doc.view_profile()
                        doc.view_schedule()
                    else:
                        # otherwise, inform user of invalid ID
                        print("Doctor not found.\n")
                elif sub == "3":
                    # go back to the main menu
                    break
                else:
                    # handle invalid submenu input
                    print("Invalid choice.\n")

        elif choice == "3":
            # if user selects Appointment Scheduling, enter its sub-loop
            while True:
                # display appointment scheduling submenu
                appointment_menu()
                # prompt user for an appointment submenu choice
                sub = input("Choice: ").strip()
                if sub == "1":
                    # gather inputs to book a new appointment
                    pid = input("Patient ID: ").strip()
                    did = input("Doctor ID : ").strip()
                    date = input("Date (YYYY-MM-DD): ").strip()
                    time = input("Time (HH:MM): ").strip()
                    # attempt booking with given details
                    hs.book_appointment(pid, did, date, time)
                elif sub == "2":
                    # view all scheduled appointments
                    hs.view_appointments()
                elif sub == "3":
                    # prompt for appointment ID to cancel
                    aid = input("Appointment ID: ").strip()
                    # attempt to cancel the appointment
                    hs.cancel_appointment(aid)
                elif sub == "4":
                    # go back to the main menu
                    break
                else:
                    # handle invalid submenu input
                    print("Invalid choice.\n")

        elif choice == "4":
            # if user selects Billing, enter its sub-loop
            while True:
                # display billing submenu
                billing_menu()
                # prompt user for a billing submenu choice
                sub = input("Choice: ").strip()
                if sub == "1":
                    # prompt for appointment ID to bill
                    aid = input("Appointment ID: ").strip()
                    # generate and display the bill
                    hs.generate_bill(aid)
                elif sub == "2":
                    # go back to the main menu
                    break
                else:
                    # handle invalid submenu input
                    print("Invalid choice.\n")

        elif choice == "5":
            # if user selects Exit, print goodbye and terminate
            print("Exiting... Goodbye!")
            sys.exit(0)

        else:
            # handle invalid main menu input
            print("Invalid selection; try again.\n")

if __name__ == "__main__":
    # entry point guard: call main() only if script is run directly
    main()


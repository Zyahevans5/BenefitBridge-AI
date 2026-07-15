# BenefitBridge AI
# MyFriendBen Application Status Tracker

import json

applications = []


class Application:

    def __init__(self, program, status, date):
        self.program = program
        self.status = status
        self.date = date


    def update_status(self, new_status):
        self.status = new_status


    def show_application(self):
        print("---------------------")
        print("Program:", self.program)
        print("Status:", self.status)
        print("Applied Date:", self.date)
        print("---------------------")

from application import Application
from storage import save_applications, load_applications
from menu import show_menu


applications = load_applications()

# Add Application
def add_application():

    print("\nAdd New Application")

    program = input("Benefit Program: ")
    status = input("Application Status: ")
    date = input("Application Date: ")

    application = Application(
        program,
        status,
        date
    )

    applications.append(application)

    save_applications(applications)

    print("Application added successfully!")


# View Applications
def view_applications():

    print("\nBenefitBridge AI Dashboard")

    if len(applications) == 0:
        print("No applications found.")
        return

    for index, app in enumerate(applications, start=1):

        print(f"\nApplication #{index}")

        app.show_application()


# Update Application
def update_application():

    view_applications()

    choice = int(input("\nWhich application? "))

    new_status = input("New status: ")

    applications[choice - 1].update_status(new_status)

    save_applications(applications)

    print("Updated!")


# Main Program
running = True


while running:

    show_menu()

    choice = input("\nChoose an option: ")


    if choice == "1":

        add_application()


    elif choice == "2":

        view_applications()


    elif choice == "3":

        update_application()


    elif choice == "4":

        print("Goodbye!")

        running = False


    else:

        print("Invalid choice")


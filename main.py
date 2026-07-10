# BenefitBridge AI
# MyFriendBen Application Status Tracker


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

    print("Application added successfully!")



# View Applications

def view_applications():

    print("\n==========================")
    print("BenefitBridge AI Dashboard")
    print("==========================")

    if len(applications) == 0:
        print("No applications found.")
        return

    for index, app in enumerate(applications, start=1):

        print(f"\nApplication #{index}")

        app.show_application()



# Update Application

def update_application():

    view_applications()

    if len(applications) == 0:
        return


    choice = int(
        input("\nWhich application would you like to update? ")
    )


    new_status = input("Enter new status: ")


    applications[choice - 1].update_status(new_status)


    print("Status updated!")



# Menu

def show_menu():

    print("\n==============================")
    print("       BenefitBridge AI")
    print("==============================")
    print("1. Add Application")
    print("2. View Applications")
    print("3. Update Status")
    print("4. Exit")



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

        print("Invalid option. Please try again.")
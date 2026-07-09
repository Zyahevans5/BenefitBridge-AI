# BenefitBridge AI
# MyFriendBen Application Status Tracker


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



# Create a SNAP application

snap_application = Application(
    "SNAP Food Assistance",
    "Submitted",
    "July 8, 2026"
)


# Show current status

snap_application.show_application()


# Update application status

snap_application.update_status("Approved")


print("Updated Application Status:")


# Show new status

snap_application.show_application()

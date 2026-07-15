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
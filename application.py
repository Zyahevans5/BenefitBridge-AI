class Application:

    def __init__(
        self,
        program,
        status,
        date,
        notes="",
        timeline=None,
        documents=None
    ):

        self.program = program
        self.status = status
        self.date = date
        self.notes = notes


        if timeline is None:
            self.timeline = []
        else:
            self.timeline = timeline


        if documents is None:
            self.documents = []
        else:
            self.documents = documents



    def update_status(self, new_status):

        self.status = new_status



    def add_timeline_event(self, event):

        self.timeline.append(event)



    def add_document(self, document):

        self.documents.append(
            {
                "name": document,
                "completed": False
            }
        )
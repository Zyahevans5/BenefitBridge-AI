import json
from application import Application


def save_applications(applications):

    data = []

    for app in applications:

        data.append({
            "program": app.program,
            "status": app.status,
            "date": app.date,
            "notes": app.notes,
            "timeline": app.timeline,
            "documents": app.documents
        })


    with open("applications.json", "w") as file:

        json.dump(
            data,
            file,
            indent=4
        )



def load_applications():

    applications = []

    try:

        with open("applications.json", "r") as file:

            data = json.load(file)


            for item in data:

                application = Application(

                    item["program"],

                    item["status"],

                    item["date"],

                    item.get("notes", ""),

                    item.get("timeline", []),

                    item.get("documents", [])

                )


                applications.append(application)


    except FileNotFoundError:

        pass


    return applications
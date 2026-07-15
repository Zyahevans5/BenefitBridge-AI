# BenefitBridge AI

BenefitBridge AI is a Python application designed to help people keep track of their public benefit applications after they have applied.

This project was inspired by the work of MyFriendBen, a nonprofit that helps people discover the government benefits they may qualify for. While MyFriendBen helps users find benefits, BenefitBridge AI focuses on helping users stay organized throughout the application process by tracking application statuses in one place.

## Problem

Applying for public benefits can be overwhelming. People may apply for multiple programs at once and struggle to remember:

- Which programs they applied for
- The current status of each application
- When they applied
- Which applications still need follow-up

BenefitBridge AI provides a simple way to organize this information.

## Features

- Add benefit applications
- View all saved applications
- Update application statuses
- Save application data using JSON
- Load saved applications when the program starts

## Technologies Used

- Python 3
- JSON
- Visual Studio Code

## Project Structure

```
BenefitBridge-AI/
│
├── main.py
├── application.py
├── storage.py
├── menu.py
├── applications.json
└── README.md
```

## How to Run

1. Clone this repository.

2. Open the project in Visual Studio Code.

3. Run:

```bash
python main.py
```

4. Use the menu to:
   - Add an application
   - View applications
   - Update an application's status
   - Exit the program

## Future Improvements

This project is still under development. Planned features include:

- User accounts
- Application deadlines
- Document checklist
- Reminder notifications
- AI-powered application guidance
- Simple web dashboard using Streamlit

## Inspiration

This project was created as part of a portfolio project inspired by the mission of MyFriendBen and the Claude Corps Fellowship to explore how AI can support nonprofit organizations and improve access to public benefits.

## Author

Zyah Evans

## Project Vision

The long-term goal of BenefitBridge AI is to support nonprofit organizations by making it easier for people to successfully complete benefit applications. In future versions, the application could provide AI-powered guidance, explain application statuses, send reminders about deadlines, and help users understand the next steps in the enrollment process.

Rather than replacing nonprofit staff, BenefitBridge AI is intended to reduce administrative burden and help organizations serve more people efficiently.
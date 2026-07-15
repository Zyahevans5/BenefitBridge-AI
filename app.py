from benefits import BENEFITS
import streamlit as st
from datetime import date

from application import Application
from storage import save_applications, load_applications

applications = load_applications()
if "message" in st.session_state:
    st.success(st.session_state["message"])
    del st.session_state["message"]
# -----------------------------
# Page Setup
# -----------------------------

st.set_page_config(
    page_title="BenefitBridge AI",
    page_icon="🏛️",
    layout="wide"
)


applications = load_applications()


# -----------------------------
# Sidebar Navigation
# -----------------------------

page = st.sidebar.radio(
    "Navigation",
    [
        "🏠 Dashboard",
        "➕ Add Application",
        "📋 My Applications",
        "📚 Benefit Information",
        "📝 Case Notes",
        "📄 Documents",
        "🤖 AI Assistant"
    ]
)


# =====================================================
# DASHBOARD
# =====================================================

if page == "🏠 Dashboard":

    st.title("🏛️ BenefitBridge AI")

    st.write(
        "Track your public benefit applications."
    )
    st.info(
    "💡 Keep track of applications, documents, notes, and important  all in one place."
)

    total = len(applications)

    approved = sum(
        1 for app in applications
        if app.status == "Approved"
    )

    pending = sum(
        1 for app in applications
        if app.status == "Pending Review"
    )

    submitted = sum(
        1 for app in applications
        if app.status == "Submitted"
    )

    denied = sum(
        1 for app in applications
        if app.status == "Denied"
    )


    col1, col2, col3 = st.columns(3)

    col1.metric(
        "Total Applications",
        total
    )

    col2.metric(
        "Approved",
        approved
    )

    col3.metric(
        "Pending",
        pending
    )


    col4, col5 = st.columns(2)

    col4.metric(
        "Submitted",
        submitted
    )

    col5.metric(
        "Denied",
        denied
    )



# =====================================================
# ADD APPLICATION
# =====================================================

elif page == "➕ Add Application":

    st.title("➕ Add Application")


    program = st.selectbox(
        "Benefit Program",
        list(BENEFITS.keys())
    )


    status = st.selectbox(
        "Application Status",
        [
            "Not Started",
            "Submitted",
            "Pending Review",
            "Approved",
            "Denied"
        ]
    )


    application_date = st.date_input(
        "Application Date"
    )


    if st.button("Save Application"):

     new_application = Application(
        program,
        status,
        str(application_date)
    )

    new_application.add_timeline_event(
        f"{application_date} - Application Created"
    )

    if program in BENEFITS:
        for document in BENEFITS[program]["documents"]:
            new_application.add_document(document)

    applications.append(new_application)

    save_applications(applications)

    st.session_state["message"] = "✅ Application saved successfully!"
    st.rerun()

# =====================================================
# MY APPLICATIONS
# =====================================================

elif page == "📋 My Applications":

    st.title("📋 My Applications")


    search = st.text_input(
        "🔍 Search by benefit"
    )


    filter_status = st.selectbox(
        "Filter Status",
        [
            "All",
            "Not Started",
            "Submitted",
            "Pending Review",
            "Approved",
            "Denied"
        ]
    )


    for app in applications:


        if search.lower() not in app.program.lower():
            continue


        if (
            filter_status != "All"
            and app.status != filter_status
        ):
            continue


        st.subheader(
            app.program
        )

        st.write(
            f"Status: {app.status}"
        )

        st.write(
            f"Applied: {app.date}"
        )

        st.divider()



    if applications:

        st.subheader(
            "Update Status"
        )


        program_list = [
            app.program
            for app in applications
        ]


        selected_program = st.selectbox(
            "Select Application",
            program_list,
            key="update"
        )


        new_status = st.selectbox(
            "New Status",
            [
                "Not Started",
                "Submitted",
                "Pending Review",
                "Approved",
                "Denied"
            ]
        )


        if st.button("Update Status"):


            for app in applications:


                if app.program == selected_program:


                    app.update_status(
                        new_status
                    )


                    app.add_timeline_event(
                        f"{date.today()} - Status changed to {new_status}"
                    )


            save_applications(
                applications
            )

          
        st.session_state["message"] = "✅ Application status updated successfully!"
        st.rerun()


        st.subheader(
            "🗑️ Delete Application"
        )


        delete_options = [
            f"{app.program} ({app.status})"
            for app in applications
        ]


        selected_delete = st.selectbox(
            "Choose Application",
            delete_options
        )


        if st.button("Delete Application"):


            index = delete_options.index(
                selected_delete
            )


            applications.pop(
                index
            )


            save_applications(
                applications
            )


    st.session_state["message"] = "🗑️ Application deleted successfully!"
    st.rerun()



# =====================================================
# BENEFIT INFORMATION
# =====================================================

elif page == "📚 Benefit Information":

    st.title(
        "📚 Benefit Information"
    )


    selected = st.selectbox(
        "Choose Benefit",
        list(BENEFITS.keys())
    )


    benefit = BENEFITS[selected]


    st.subheader(
        selected
    )


    st.write(
        "### ⏳ Processing Time"
    )

    st.info(
        benefit["processing_time"]
    )


    st.write(
        "### 📄 Documents Needed"
    )


    for item in benefit["documents"]:
        st.write(
            f"✅ {item}"
        )


    st.write(
        "### 💡 Helpful Tips"
    )


    for tip in benefit["tips"]:
        st.success(
            tip
        )



# =====================================================
# CASE NOTES + TIMELINE
# =====================================================

elif page == "📝 Case Notes":

    st.title(
        "📝 Case Notes"
    )


    if not applications:

        st.info(
            "No applications available."
        )


    else:


        program_list = [
            app.program
            for app in applications
        ]


        selected_program = st.selectbox(
            "Choose Application",
            program_list
        )


        selected_app = next(
            app for app in applications
            if app.program == selected_program
        )


        notes = st.text_area(
            "Notes",
            selected_app.notes,
            height=200
        )


        if st.button("Save Notes"):


            selected_app.notes = notes


            selected_app.add_timeline_event(
                f"{date.today()} - Notes updated"
            )


            save_applications(
                applications
            )


            st.session_state["message"] = "📝 Notes saved successfully!"
            st.rerun()


        st.subheader(
            "📅 Timeline"
        )


        if not selected_app.timeline:

            st.info(
                "No timeline events yet."
            )


        else:

            for event in selected_app.timeline:

                st.write(
                    "•",
                    event
                )

# =====================================================
# DOCUMENT CHECKLIST
# =====================================================

elif page == "📄 Documents":

    st.title("📄 Document Checklist")


    if not applications:

        st.info(
            "No applications available."
        )


    else:

        programs = [
            app.program
            for app in applications
        ]


        selected_program = st.selectbox(
            "Choose Application",
            programs
        )


        selected_app = next(
            app for app in applications
            if app.program == selected_program
        )


        st.subheader(
            "Required Documents"
        )


        for document in selected_app.documents:


            checked = st.checkbox(
                document["name"],
                value=document["completed"]
            )


            document["completed"] = checked



        if st.button("Save Documents"):

         save_applications(applications)

    st.session_state["message"] = "📄 Documents saved successfully!"
    st.rerun()

# =====================================================
# AI ASSISTANT
# =====================================================

elif page == "🤖 AI Assistant":

    st.title(
        "🤖 AI Assistant"
    )


    question = st.text_input(
        "Ask a question about benefits"
    )


    if st.button("Ask"):

        st.info(
            "AI responses coming soon!"
        )
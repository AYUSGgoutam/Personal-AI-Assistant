
import streamlit as st
from modules.ai_chatbot import render_chatbot

# --------------------------------
# PAGE CONFIGURATION
# --------------------------------

st.set_page_config(
    page_title="Ayush AI Assistant",
    page_icon="🤖",
    layout="wide"
)

# --------------------------------
# CUSTOM CSS
# --------------------------------

st.markdown("""
<style>
.main-title {
    font-size: 32px;
    font-weight: bold;
    color: #4A90E2;
}
.subtitle {
    font-size: 16px;
    color: gray;
}
</style>
""", unsafe_allow_html=True)


# --------------------------------
# SIDEBAR NAVIGATION
# --------------------------------

st.sidebar.title("🤖 Ayush AI")
st.sidebar.write("Your Personal AI Assistant")

menu = st.sidebar.radio(
    "Navigation",
    [
        "Dashboard",
        "AI Chatbot",
        "Email Manager",
        "Job Search",
        "Job Apply",
        "Application Tracker"
    ]
)

st.sidebar.divider()
st.sidebar.caption("Developed by Ayush Gautam")


# --------------------------------
# DASHBOARD PAGE
# --------------------------------

if menu == "Dashboard":

    st.markdown(
        '<p class="main-title">Welcome to Ayush AI Assistant 🚀</p>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<p class="subtitle">Your personal AI-powered productivity assistant.</p>',
        unsafe_allow_html=True
    )

    st.divider()

    col1, col2, col3 = st.columns(3)

    with col1:
        st.info("🤖 AI Chatbot")
        st.write("Ask questions and get AI-powered answers.")

    with col2:
        st.info("📧 Email Manager")
        st.write("Prepare professional emails.")

    with col3:
        st.info("💼 Job Search")
        st.write("Explore job opportunities.")

    st.divider()

    st.subheader("Available Features")

    st.markdown("""
    - 🤖 Gemini AI Chatbot
    - 📧 Email writing and management
    - 🔍 Job search
    - 📝 Job application preparation
    - 📊 Application tracking
    """)


# --------------------------------
# AI CHATBOT PAGE
# --------------------------------

elif menu == "AI Chatbot":

    render_chatbot()


# --------------------------------
# EMAIL MANAGER PAGE
# --------------------------------

elif menu == "Email Manager":

    st.title("📧 Email Manager")

    st.write("Prepare professional emails with AI assistance.")

    email_type = st.selectbox(
        "Select Email Type",
        [
            "Job Application",
            "HR Follow-up",
            "Interview Request",
            "Leave Request",
            "General Email"
        ]
    )

    details = st.text_area(
        "Enter your email details"
    )

    if st.button("Prepare Email"):

        if details.strip():
            st.info(
                "Email drafting feature will be connected to Gemini next."
            )
        else:
            st.warning("Please enter email details.")


# --------------------------------
# JOB SEARCH PAGE
# --------------------------------

elif menu == "Job Search":

    st.title("🔍 Job Search")

    role = st.text_input(
        "Enter Job Role",
        placeholder="Python Developer"
    )

    location = st.text_input(
        "Enter Location",
        placeholder="Indore"
    )

    experience = st.selectbox(
        "Experience",
        ["Fresher", "0-1 Year", "1-2 Years"]
    )

    if st.button("Search Jobs"):

        if role.strip() and location.strip():
            st.info(
                "Job search integration will be connected in the next step."
            )
        else:
            st.warning("Please enter job role and location.")


# --------------------------------
# JOB APPLY PAGE
# --------------------------------

elif menu == "Job Apply":

    st.title("📝 Job Application Assistant")

    company = st.text_input("Company Name")

    job_role = st.text_input("Job Role")

    job_link = st.text_input("Job Application URL")

    if st.button("Prepare Application"):

        if company.strip() and job_role.strip():
            st.success("Application details saved for preparation.")
            st.write("Company:", company)
            st.write("Role:", job_role)
            st.write("Link:", job_link)
        else:
            st.warning("Please enter company and job role.")


# --------------------------------
# APPLICATION TRACKER PAGE
# --------------------------------

elif menu == "Application Tracker":

    st.title("📊 Application Tracker")

    st.write("Track your job applications here.")

    st.info(
        "Application database and tracking functionality "
        "will be implemented in the next step."
    )


# --------------------------------
# FOOTER
# --------------------------------

st.sidebar.divider()
st.sidebar.caption("Ayush AI Assistant | Python + Streamlit + Gemini")


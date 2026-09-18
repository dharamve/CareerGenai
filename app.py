import streamlit as st

from services.chat_service import ChatService
from utils.logger import setup_logger


# --------------------------------------------------
# PAGE CONFIGURATION
# --------------------------------------------------

st.set_page_config(
    page_title="CareerGenie",
    page_icon="💼",
    layout="centered"
)


# --------------------------------------------------
# LOGGER
# --------------------------------------------------

logger = setup_logger()


# --------------------------------------------------
# TITLE
# --------------------------------------------------

st.title("💼 CareerGenie")

st.write(
    "Your AI-powered career advisor built with "
    "LangChain and Google Gemini."
)


# --------------------------------------------------
# SIDEBAR
# --------------------------------------------------

with st.sidebar:

    st.header("CareerGenie")

    st.write(
        """
        CareerGenie can help you with:

        - 📊 Data Analytics
        - 💻 Software Careers
        - 🤖 AI & ML
        - 📄 Resume Building
        - 🎯 Interview Preparation
        - 🗺️ Career Roadmaps
        - 🧠 Skill Gap Analysis
        """
    )

    st.divider()

    if st.button("🗑️ Clear Conversation"):

        st.session_state.messages = []

        st.rerun()


# --------------------------------------------------
# SESSION STATE
# --------------------------------------------------

if "messages" not in st.session_state:

    st.session_state.messages = []


# --------------------------------------------------
# DISPLAY CHAT HISTORY
# --------------------------------------------------

for message in st.session_state.messages:

    with st.chat_message(message["role"]):

        st.markdown(message["content"])


# --------------------------------------------------
# USER INPUT
# --------------------------------------------------

user_input = st.chat_input(
    "Ask me anything about your career..."
)


# --------------------------------------------------
# PROCESS USER MESSAGE
# --------------------------------------------------

if user_input:

    # Add user message
    st.session_state.messages.append(
        {
            "role": "user",
            "content": user_input
        }
    )

    # Display user message
    with st.chat_message("user"):

        st.markdown(user_input)

    # Generate response
    with st.chat_message("assistant"):

        with st.spinner("CareerGenie is thinking..."):

            try:

                chat_service = ChatService()

                response = chat_service.get_response(
                    st.session_state.messages
                )

                st.markdown(response)

                # Save assistant response
                st.session_state.messages.append(
                    {
                        "role": "assistant",
                        "content": response
                    }
                )

            except Exception as error:

                logger.exception(
                    "Unexpected application error."
                )

                st.error(
                    "Something went wrong. "
                    "Please check your API configuration."
                )

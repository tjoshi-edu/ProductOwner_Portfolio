import streamlit as st

from src.llm_service import OllamaService
from src.prompts import build_user_story_prompt


# ---------------------------------------------------------
# Page Configuration
# ---------------------------------------------------------

st.set_page_config(
    page_title="AI Requirements & User Story Generator",
    page_icon="🤖",
    layout="wide"
)


# ---------------------------------------------------------
# Header
# ---------------------------------------------------------

st.title("🤖 AI Requirements & User Story Generator")

st.markdown(
    """
    Transform business requirements into structured,
    product-ready user stories using Generative AI.
    """
)

st.divider()


# ---------------------------------------------------------
# Sidebar
# ---------------------------------------------------------

with st.sidebar:

    st.header("AI Configuration")

    model = st.selectbox(
        "LLM Model",
        [
            "llama3.2"
        ]
    )

    st.info(
        "This application uses Ollama to run the AI model locally."
    )


# ---------------------------------------------------------
# Requirement Input
# ---------------------------------------------------------

st.subheader("Business Requirement")

requirement = st.text_area(
    "Enter a business requirement",
    placeholder=(
        "Example: Customers should be able to reset their "
        "password using their registered email address."
    ),
    height=180
)


# ---------------------------------------------------------
# Generate
# ---------------------------------------------------------

generate_button = st.button(
    "🚀 Generate User Story",
    type="primary"
)


if generate_button:

    if not requirement.strip():

        st.warning(
            "Please enter a business requirement."
        )

    else:

        with st.spinner(
            "Analyzing requirement with AI..."
        ):

            try:

                service = OllamaService(
                    model=model
                )

                prompt = build_user_story_prompt(
                    requirement
                )

                result = service.generate(
                    prompt
                )

                st.success(
                    "Requirement analysis completed!"
                )

                st.subheader(
                    "AI-Generated Product Requirements"
                )

                st.markdown(result)

            except Exception as e:

                st.error(
                    "Unable to connect to Ollama."
                )

                st.code(str(e))
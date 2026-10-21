import streamlit as st

from agent import create_research_report


st.set_page_config(
    page_title="AI Research Agent",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 AI Research Agent")
st.write(
    "Enter a research topic and the AI agent will search the web "
    "and generate a structured research report."
)

research_topic = st.text_area(
    "Research Topic",
    placeholder="Example: Latest trends in Generative AI",
    height=120
)

generate_button = st.button("🔍 Generate Research Report", type="primary")

if generate_button:
    if not research_topic.strip():
        st.warning("Please enter a research topic.")
    else:
        with st.spinner("Researching the topic... This may take a moment."):
            try:
                report = create_research_report(research_topic)
                st.success("Research report generated!")
                st.markdown(report)
                st.download_button(
                    label="⬇️ Download report",
                    data=report,
                    file_name="research_report.md",
                    mime="text/markdown"
                )
            except Exception as error:
                st.error(f"Something went wrong: {error}")
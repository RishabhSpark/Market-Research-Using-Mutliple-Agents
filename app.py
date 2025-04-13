import streamlit as st
from agents.agents_pipeline import agents_pipeline

st.set_page_config(page_title="AI Use Case Generator", layout="wide")
st.title("AI-Powered Market Research & Use Case Generation Agent")
st.markdown("Generate actionable AI/ML/GenAI use cases, discover relevant datasets, and explore implementation ideas — all tailored to your target industry or company.")

industry = st.text_input("Enter the industry or company you want to research:")

if st.button("Generate Insights"):
    if not industry.strip():
        st.warning("Please enter a valid industry or company name.")
    else:
        with st.spinner("Running agent pipeline..."):
            results = agents_pipeline(industry)

        st.subheader("Industry Research")
        st.markdown(results["summary"])

        st.subheader("AI/ML Use Cases")
        st.markdown(results["usecases"])

        st.subheader("Dataset Search Links (Kaggle & HuggingFace)")
        st.markdown(results["datasets"], unsafe_allow_html=True)

        st.subheader("Suggested GenAI Tools")
        st.markdown(results["genai_tools"])
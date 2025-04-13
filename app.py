import streamlit as st
# from agents.industry_research_agent import industry_research
# from agents.usecase_generation_agent import usecase_generation
# from agents.resource_collector_agent import collect_dataset_links
# from agents.genai_solutions_agent import genai_solutions
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


# if st.button("Generate Insights"):
#     if not industry.strip():
#         st.warning("Please enter a valid industry or company name.")
    
#     with st.spinner("Researching the industry..."):
#         summary = industry_research(industry)
#         st.subheader("Industry Research")
#         with st.expander("Industry Research Summary", expanded=True):
#             st.markdown(summary)

#     with st.spinner("Generating use cases..."):
#         usecases = usecase_generation(summary)
#     with st.expander("Proposed AI/ML Use Cases", expanded=True):
#             st.markdown(usecases)

#     with st.spinner("Finding related datasets..."):
#         dataset_links = collect_dataset_links(usecases)
#     with st.expander("Dataset Search Links (Kaggle & HuggingFace)", expanded=True):
#         st.markdown(dataset_links, unsafe_allow_html=True)

#     with st.spinner("Suggesting GenAI tools..."):
#         genai_solutions = genai_solutions(summary)
#     with st.expander("Suggested GenAI Solutions", expanded=True):
#             st.markdown(genai_solutions)
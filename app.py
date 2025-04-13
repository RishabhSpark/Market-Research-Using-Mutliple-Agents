import streamlit as st 
from agents.industry_research_agent import industry_research
from agents.usecase_generation_agent import usecase_generation
# from agents.resource_collector_agent import resource_collector
from agents.resource_collector_agent import collect_dataset_links
from agents.genai_solutions_agent import run_genai_solutions

st.title("Market Research & Use Case Generation Agent")

industry = st.text_input("Enter the industry or company you want to research:")

if st.button("Generate"):
    with st.spinner("Researching the industry..."):
        summary = industry_research(industry)
        st.subheader("Industry Research")
        st.markdown(summary)

    with st.spinner("Generating use cases..."):
        usecases = usecase_generation(summary)
        st.subheader("AI/ML Use Cases")
        st.markdown(usecases)

    # with st.spinner("Finding related datasets..."):
        # datasets = resource_collector(usecases)
        # st.subheader("Related Datasets & Projects")
        # st.markdown(datasets, unsafe_allow_html=True)
        # st.subheader("Dataset Search Links (Kaggle & HuggingFace)")
        # st.markdown(dataset_links, unsafe_allow_html=True)

    with st.spinner("Finding related datasets..."):
        st.subheader("Dataset Search Links (Kaggle & HuggingFace)")
        dataset_links = collect_dataset_links(usecases)
        st.markdown(dataset_links, unsafe_allow_html=True)

    with st.spinner("Suggesting GenAI tools..."):
        genai_solutions = run_genai_solutions(summary)
        st.subheader("GenAI Tool Suggestions")
        st.markdown(genai_solutions)
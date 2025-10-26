import streamlit as st
import json
import helpers as h

project_data = st.session_state.get("project_data", None)

if project_data is None:
    with open('data/projects.json') as f:
        project_data = json.load(f)
        st.session_state.project_data = project_data

all_tech_stacks = []
for id, data in project_data.items():
    all_tech_stacks += data['techstacks']

main_container = st.container(gap="large")

container = main_container.container()
container.title("Hi, I'm :blue[Aung Khant Kyaw] 👋")

container = main_container.container()
container.header("Summary 📃")
container.write("Final-year B.Sc. student in Information and Communication Technology at Rangsit University, Thailand, seeking an AI Engineer internship. Experienced in LangChain, LangGraph, Streamlit, Python, n8n, SQL, LLMs, Hugging Face models, RAG, and structured output, with a strong motivation to apply AI workflows in practical, industry-focused solutions.")

container = main_container.container()
container.header("Skills 🤹")
container.markdown(h.create_techstack_blocks(all_tech_stacks), unsafe_allow_html=True)

container = main_container.container()
container.header("Education 🎓")
container.write("**Rangsit University, Thailand**")
container.write("Bachelor of Science in Information and Communication Technology ***(2020 - 2024)***")
container.caption("Ongoing")
container.markdown(":green[**GPA: 3.76/4.00**]", unsafe_allow_html=True)

container = main_container.container()
container.header("Keep in Touch 🪪")
container.write("Mail: [aungkhant.k66@rsu.ac.th](mailto:aungkhant.k66@rsu.ac.th)")
container.write("LinkedIn Profile: [Aung Khant Kyaw](https://www.linkedin.com/in/aung-khant-kyaw-2k0430/)")
container.write("Phone: [+66 64 010 1240](tel:+66640101240)")
container.write("Line ID: vech342")
import streamlit as st
import json
import helpers as h

project_data = st.session_state.get("project_data", None)

if project_data is None:
    with open('data/projects.json') as f:
        project_data = json.load(f)
        st.session_state.project_data = project_data

query_params = st.query_params

project_id = query_params.get("projectid", None)

if project_id is not None:
    st.session_state.selected_project_id = project_id

    with open(f"projects/{project_id}.py") as f:
        code = f.read()
        exec(code)

    st.stop()

project_id = st.session_state.get("selected_project_id", None)
if project_id is not None:
    with open(f"projects/{project_id}.py") as f:
        code = f.read()
        exec(code)

    st.session_state.selected_project_id = None

    st.stop()

main_container = st.container(gap="large")
for id, data in project_data.items():
    container = main_container.container(border=True)

    container.header(data['name'])
    container.write(data['description'])
    container.markdown(h.create_techstack_blocks(data['techstacks']), unsafe_allow_html=True)
    container.markdown(h.create_techstack_blocks(data['category'], color="blue"), unsafe_allow_html=True)

    clicked = container.button("View Detail", key=id)

    if clicked:
        st.session_state.selected_project_id = id
        st.rerun()
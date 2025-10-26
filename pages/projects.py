import streamlit as st
import json
import helpers as h
import importlib.util
import os


project_data = st.session_state.get("project_data", None)

if project_data is None:
    with open('data/projects.json') as f:
        project_data = json.load(f)
        st.session_state.project_data = project_data

query_params = st.query_params

project_id = query_params.get("projectid", None)

if project_id is not None:
    st.session_state.selected_project_id = project_id
    module_path = f"projects/{project_id}.py"

    if os.path.exists(module_path):
        spec = importlib.util.spec_from_file_location(project_id, module_path)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)

        # Call its run() function if it exists
        if hasattr(module, "run"):
            module.run()

            st.stop()
        else:
            st.error(f"Module '{project_id}' has no run() function.")
    else:
        st.error(f"Project file '{module_path}' not found.")

project_id = st.session_state.get("selected_project_id", None)

if project_id is not None:
    st.session_state.selected_project_id = project_id
    module_path = f"projects/{project_id}.py"

    if os.path.exists(module_path):
        spec = importlib.util.spec_from_file_location(project_id, module_path)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)

        # Call its run() function if it exists
        if hasattr(module, "run"):
            module.run()

            st.session_state.selected_project_id = None

            st.stop()
        else:
            st.error(f"Module '{project_id}' has no run() function.")
    else:
        st.error(f"Project file '{module_path}' not found.")

main_container = st.container(gap="large")

selected_categories = st.session_state.get("selected_categories", {})
if len(selected_categories) == 0:
    for id, data in project_data.items():
        for category in data['category']:
            if category not in selected_categories:
                selected_categories[category] = True

category_param = query_params.get("category", None)
if category_param is not None:
    for category in selected_categories:
        selected_categories[category] = False

    selected_categories[category_param] = True

    st.session_state.selected_categories = selected_categories
    st.switch_page("pages/projects.py")

filter_container = main_container.container(horizontal=True, horizontal_alignment="left")
for category, selected in selected_categories.items():
    check = filter_container.checkbox(label=category, value=selected, key=category)

    if check:
        selected_categories[category] = True
        st.session_state.selected_categories = selected_categories
    else:
        selected_categories[category] = False
        st.session_state.selected_categories = selected_categories


for id, data in project_data.items():
    include = False
    for category in data['category']:
        if selected_categories[category]:
            include = True
            break

    if not include:
        continue

    container = main_container.container(border=True)

    container.header(data['name'])
    container.write(data['description'])
    container.markdown(h.create_techstack_blocks(data['techstacks']), unsafe_allow_html=True)
    container.markdown(h.create_techstack_blocks(data['category'], color="blue"), unsafe_allow_html=True)

    clicked = container.button("View Detail", key=id)

    if clicked:
        st.session_state.selected_project_id = id
        st.rerun()
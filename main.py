import streamlit as st

pages = {
    "about_me": st.Page(page="pages/about_me.py", title="About Me"),
    "projects": st.Page(page="pages/projects.py", title="Projects"),
}

# Define pages with custom labels
pg = st.navigation(list(pages.values()))

pg.run()

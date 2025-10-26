import streamlit as st

pages = [
    st.Page("pages/about_me.py", title="🤓 About Me"),
    st.Page("pages/projects.py", title="🚀 Projects"),
]

pg = st.navigation(pages)
pg.run()

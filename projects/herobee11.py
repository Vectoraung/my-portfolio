import streamlit as st
import helpers as h
import requests

all_projects = st.session_state.get("project_data", None)

if all_projects is None:
    st.write("No projects data found")
    st.stop()
    
data = all_projects["herobee"]
st.header(data['name'])
st.write(data['description'])

st.markdown(h.create_techstack_blocks(data['techstacks']), unsafe_allow_html=True)

st.subheader("Game Play", divider=True)
st.write("Your character is a Bee and you have to eliminate angry Rhinos charging at you by shooting stinger bullets.")
st.markdown(h.video_block("https://drive.google.com/file/d/1iBxXcwTN2DM7cXDO_xXAsViavira9Ai3/preview"), unsafe_allow_html=True)

st.subheader("Game Rules", divider=True)
st.write("You lose one health point when the enemy hits you with its horn.")
st.write("The enemy loses one health point when you hit it with your stinger bullet.")
st.write("You have 5 health points and each enemy has 3 health point.")
st.markdown(h.video_block("https://drive.google.com/file/d/1G05p25Qjy_nzw0o68itYFPwIgDBVXKdC/preview"), unsafe_allow_html=True)

st.subheader("Enemies", divider=True)
st.write("The number of enemies will be increased as your score goes up.")
st.image("images/herobee3.png")

st.subheader("Map", divider=True)
st.write("Used the free map tiles from unity assets store.")
st.write("Generated map from differnet tiles randomly with specific size using script.")
st.write("Wrapped with a specific tiles that has collision as a wall.")
st.image("images/herobee4.png")

st.subheader("Enemy Spawner", divider=True)
st.write("Have an enemy spawner that will spawn enemies outside of the camera field of view.")
st.image("images/herobee5.png")

st.subheader("Links", divider=True)
st.write("Used map tiles: [Backyard Top-Down Tileset - Unity Asset Store](https://assetstore.unity.com/packages/2d/environments/backyard-top-down-tileset-53854)")
st.write("Used characters package: [Pixel Adventure 2 - Unity Asset Store](https://assetstore.unity.com/packages/2d/characters/pixel-adventure-2-155418)")

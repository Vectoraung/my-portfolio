import streamlit as st
import helpers as h
import requests

all_projects = st.session_state.get("project_data", None)

if all_projects is None:
    st.write("No projects data found")
    st.stop()
    
data = all_projects["herobee"]

main_container = st.container(gap="large")

container = main_container.container()
container.title(data['name'])
container.write(data['description'])
container.markdown(h.create_techstack_blocks(data['techstacks']), unsafe_allow_html=True)

container = main_container.container()
container.subheader("Game Play")
container.markdown(h.video_block("https://drive.google.com/file/d/1iBxXcwTN2DM7cXDO_xXAsViavira9Ai3/preview"), unsafe_allow_html=True)
container.write("Your character is a Bee and you have to eliminate angry Rhinos charging at you by shooting stinger bullets.")

container = main_container.container()
container.subheader("Game Rules")
container.markdown(h.video_block("https://drive.google.com/file/d/1G05p25Qjy_nzw0o68itYFPwIgDBVXKdC/preview"), unsafe_allow_html=True)
container.write("You lose one health point when the enemy hits you with its horn.")
container.write("The enemy loses one health point when you hit it with your stinger bullet.")
container.write("You have 5 health points and each enemy has 3 health point.")

container = main_container.container()
container.subheader("Enemies")
container.image("images/herobee3.png")
container.write("The number of enemies will be increased as your score goes up.")

container = main_container.container()
container.subheader("Map")
container.image("images/herobee4.png")
container.write("Used the free map tiles from unity assets store.")
container.write("Generated map from differnet tiles randomly with specific size using script.")
container.write("Wrapped with a specific tiles that has collision as a wall.")

container = main_container.container()
container.subheader("Enemy Spawner")
container.image("images/herobee5.png")
container.write("Have an enemy spawner that will spawn enemies outside of the camera field of view.")

container = main_container.container()
container.subheader("Links")
container.write("Used map tiles: [Backyard Top-Down Tileset - Unity Asset Store](https://assetstore.unity.com/packages/2d/environments/backyard-top-down-tileset-53854)")
container.write("Used characters package: [Pixel Adventure 2 - Unity Asset Store](https://assetstore.unity.com/packages/2d/characters/pixel-adventure-2-155418)")

import streamlit as st

def create_techstack_blocks(techstacks: list, color="green"):
    text = ""
    for ts in techstacks:
        text += f":{color}-badge[{ts}] "

    return text

def video_block(url):
    return f"""
    <div style="position:relative;padding-bottom:56.25%;height:0;overflow:hidden;">
        <iframe src="{url}" 
        style="position:absolute;top:0;left:0;width:100%;height:100%;border:none;"
        allow="autoplay"></iframe>
    </div>
    """
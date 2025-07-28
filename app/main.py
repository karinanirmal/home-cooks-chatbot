import streamlit as st
from app.avatars import avatars
import requests
import os

st.set_page_config(page_title= "Home Cooks Chatbot", page_icon="🍽️")
st.title("Home Cooks Chatbot")
st.write("Pick a cooking avatar to ask what dish you should make!")

avatar_name=st.selectbox("Choose an avatar:", list(avatars.keys()))
user_input=st.text_area("What ingredients do you have / what do you feel like eating?")

def call_openrouter(system_prompt,user_input):
    api_key=os.getenv("OPENROUTER_API_KEY")
    headers={
        "Authorization": f"Bearer{api_key}",
        "Content-Type": "application/json"
    }
    body={
        "model": "openrouter/gpt-4",
        "messages":[
            {"role":"system","content":system_prompt},
            {"role":"user", "content": user_input}
        ]
    }
    response= requests.post("https://openrouter.ai/api/v1/chat/completions", headers=headers, json=body)
    
                   
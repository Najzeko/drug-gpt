import streamlit as st
from openai import OpenAI

client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

def generate_response(message_history):
    messages = [{"role": m["role"], "content": m["content"]} for m in message_history]
    messages.insert(0, {
        "role": "system", 
        "content": """You are a helpful assistant named Drug-GPT whose goal is to aid users with pharmaceutical drug-related questions. 
        Make sure to introduce yourself in your initial message."""})
    response = client.chat.completions.create(
                model="gpt-3.5-turbo-0125",
                messages=messages
            )
    return response.choices[0].message.content

def generate_stream(message_history):
    messages = [{"role": m["role"], "content": m["content"]} for m in message_history]
    messages.insert(0, {
        "role": "system", 
        "content": """You are a helpful assistant named Drug-GPT whose goal is to aid users with pharmaceutical drug-related questions. If a user 
        asks for information about a drug, give a brief description, then list the class of drug, the mechanism of action, and the efficacy presented 
        using quantitative values. Also, list the drug's main competitors in point form, along with a brief description of each. Do not respond to off-topic inquiries"""})
    stream = client.chat.completions.create(
                model="gpt-3.5-turbo-0125",
                messages=messages,
                temperature=0.1,
                stream=True,
            )
    return stream
import streamlit as st
from agent import generate_stream, generate_response


st.set_page_config(
    page_title="Drug-GPT",
    page_icon="💊",
    menu_items={
        'About': "This app is a prototype made for demo purposes. It is not meant for real life use. Do not take anything from this app as advice."
    }
)
st.title("Drug-GPT")



# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []
    response = generate_response(st.session_state.messages)
    st.session_state.messages.append({"role": "assistant", "content": response})
    

# Display chat messages from history on app rerun
# if len(st.session_state.messages) > 1:
for message in st.session_state.messages:
    if message["role"] == "assistant":     
        with st.chat_message(name="assistant", avatar="👨‍⚕️"):
            st.markdown(message["content"])
    else:
        with st.chat_message(message["role"]):
            st.write(message["content"])

# Accept user input
if prompt := st.chat_input("Message Drug-GPT"):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)

# Display assistant response in chat message container
    with st.chat_message(name="assistant", avatar="👨‍⚕️"):
        stream = generate_stream(st.session_state.messages)
        response = st.write_stream(stream)
    st.session_state.messages.append({"role": "assistant", "content": response})
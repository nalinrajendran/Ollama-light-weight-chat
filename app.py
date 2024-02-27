import streamlit as st
import requests
import json
import subprocess

st.set_page_config(page_title="OLLAMA-Light-Weight-Memory-Chat")




with st.sidebar:

    st.title('OLLAMA Chatbot')
    st.subheader('Models and parameters')

    output = subprocess.check_output(['ollama', 'list'], text=True)
    models = [line.split()[0] for line in output.strip().split('\n')]
    available_models = models

    selected_model = st.selectbox('Choose a model', models, key='selected_model')

    if selected_model:
        st.subheader(selected_model)
        model_name = selected_model

    # model_name = 'gemma:2b'

    temperature = st.slider('Temperature', min_value=0.01, max_value=5.0, value=0.1, step=0.01)
    seed = st.number_input('Seed', min_value=0, max_value=10000, value=101, step=1)

def clear_chat_history():
    st.session_state['conversation_history'] = []

if 'conversation_history' not in st.session_state:
    st.session_state['conversation_history'] = []

st.sidebar.button('Clear Chat History', on_click=clear_chat_history)


def generate_response(prompt_input):
    conversation_history = st.session_state['conversation_history'].copy()
    conversation_history.append({"role": "user", "content": prompt_input})

    data = {
        "model": model_name,
        "messages": conversation_history,
        "stream": False,
        "options": {
            "seed": seed,
            "temperature": temperature
        }
    }

    headers = {'Content-Type': 'application/json'}
    response = requests.post('http://localhost:11434/api/chat', json=data, headers=headers)

    if response.status_code == 200:
        try:
            model_response = response.json()
        except json.JSONDecodeError:
            print("Manually extracting JSON")
            try:
                start = response.text.find('{')
                end = response.text.rfind('}') + 1
                valid_json = response.text[start:end]
                model_response = json.loads(valid_json)
            except json.JSONDecodeError as e:
                print("Failed to parse JSON:", e)
                print(response.text)
                return

        assistant_response = model_response.get("message", {}).get("content", "Couldn't process it.")
        st.session_state['conversation_history'].append({"role": "assistant", "content": assistant_response})
    else:
        st.error("Failed to get response from the model")

    return assistant_response

def handle_input():
    user_input = st.session_state.user_input
    if user_input:
        assistant_response = generate_response(user_input)
        with st.chat_message("user"):
            st.write(user_input)
        with st.chat_message("assistant"):
            st.write(assistant_response)
        st.session_state.user_input = '' 


user_input = st.text_input("You: ", key='user_input', on_change=handle_input)


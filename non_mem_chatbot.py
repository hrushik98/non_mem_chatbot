import openai
import streamlit as st

api_key = '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'
openai.api_key = api_key
st.header("Talk to me 🙂 ")

input_question = st.text_input("type something...")

start_sequence = "\nAI:"
restart_sequence = "\nHuman: "

def ask(question, chat_log = None):
    prompt_text = f'{chat_log}{restart_sequence}: {question}{start_sequence}'
    response = openai.Completion.create(
        model="text-davinci-002",
        prompt=prompt_text,
        temperature=0.9,
        max_tokens=150,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0.6,
        stop=[" Human:", " AI:"]
    )
    story = response['choices'][0]['text']
    return story
if st.button("Go"):
    x = ask(str(input_question))
    st.title(x)


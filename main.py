import streamlit as st

st.title('Hello World!')

from langchain.chat_models import ChatOpenAI
from langchain.schema import HumanMessage, SystemMessage

OPENAI_API_KEY = "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"

chat = ChatOpenAI(
    temperature=0.7,
    model_name="gpt-3.5-turbo",
    openai_api_key=OPENAI_API_KEY
)

def send_click(chat,prompt):
    messages = [SystemMessage(content='I want you to act as a philosopher'),HumanMessage(content=prompt)
]
    response = chat(messages).content
    return response    

def main():
    st.title('Ask ChatGPT')
    user_input = st.text_input("Question: ", key='prompt')
    if st.button("Send"):
        response = send_click(chat, user_input)
        st.subheader("Answer: ")
        st.success(response, icon= "👍")

if  __name__ == '__main__':   
    main()

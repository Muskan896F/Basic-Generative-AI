import streamlit as st
from langchain.schema import HumanMessage,SystemMessage,AIMessage
from langchain.chat_models import ChatOpenAI
from langchain_community.chat_models import ChatOpenAI


from dotenv import load_dotenv
load_dotenv()
import os

st.set_page_config(page_title="My chatbot")
st.header(" I am your  chatbot , Ask me a question ?")

api_key = os.getenv("OPENAI_API_KEY")
chat = ChatOpenAI(openai_api_key=api_key, temperature=0.5)


if 'mymessages' not in st.session_state:
    st.session_state['mymessages']=[
        SystemMessage(content="You  are Muskan Ara chatbot and your work is to answer my question")
    ]


def chatmodel_response(question):
    st.session_state['mymessages'].append(HumanMessage(content=question))
    response = chat.invoke(st.session_state['mymessages'])

    st.session_state['mymessages'].append(AIMessage(content=response.content))
    return response.content

input=st.text_area("Input: ",key="input")

response=chatmodel_response(input)

submit_button=st.button("Ask Question ?")

if submit_button:
    st.subheader("This is your Response :")
    st.write(response)




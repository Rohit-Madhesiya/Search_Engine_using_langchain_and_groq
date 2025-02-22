import streamlit as st
import os
from dotenv import load_dotenv
load_dotenv()
from langchain_groq import ChatGroq
from langchain_community.utilities import ArxivAPIWrapper,WikipediaAPIWrapper
from langchain_community.tools import ArxivQueryRun,WikipediaQueryRun,DuckDuckGoSearchRun
from langchain.agents import initialize_agent,AgentType
from langchain.callbacks import StreamlitCallbackHandler
from langchain.prompts import ChatPromptTemplate

# Arxiv and wikipedia tools
arxiv_api_wrapper=ArxivAPIWrapper(top_k_results=1,doc_content_chars_max=300)
arxiv=ArxivQueryRun(api_wrapper=arxiv_api_wrapper)

wiki_api_wrapper=WikipediaAPIWrapper(top_k_results=1,doc_content_chars_max=300)
wiki=WikipediaQueryRun(api_wrapper=wiki_api_wrapper)

duckduckgo_search=DuckDuckGoSearchRun(name="Search")



st.title("LangChain-Chat with Search")

"""
Here, we are going to use `StreamlitCallbackHandler` to display 
the thoughts and actions of an agent in an interactive Streamlit app.
"""



# sidebar for settings
st.sidebar.title("Settings")
api_key=st.sidebar.text_input("Enter the Groq API Key",type="password")

if "messages" not in st.session_state:
  st.session_state["messages"]=[
    {"role":"assistant","content":"Hi, I am a chatbot who can search the web. How can I help you?"}
  ]

for message in st.session_state.messages:
  st.chat_message(message['role']).write(message['content'])

if prompt:=st.chat_input(placeholder="What is Generative AI?"):
  st.session_state.messages.append({'role':'user',"content":prompt})
  st.chat_message("user").write(prompt)
  llm_model=ChatGroq(model_name="Llama3-8b-8192",groq_api_key=api_key,streaming=True)
  tools=[arxiv,wiki,duckduckgo_search]

  search_agent=initialize_agent(tools,
                                llm_model,
                                agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
                                handling_parsing_errors=True
                                )
  with st.chat_message('assistant'):
    callback_handler=StreamlitCallbackHandler(st.container(),expand_new_thoughts=False)
    response=search_agent.run(st.session_state.messages,callbacks=[callback_handler])
    st.session_state.messages.append({"role":'assistant',"content":response})
    st.write(response)

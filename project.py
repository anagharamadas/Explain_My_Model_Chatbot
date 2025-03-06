import os
from langchain_community.chat_models import ChatPerplexity
import streamlit as st
from langchain_core.prompts import ChatPromptTemplate  # type: ignore

st.title("LLM powered Model Info Application")

PPLX_API_KEY = st.text_input("Enter your API key: ", type="password")


os.environ["PPLX_API_KEY"] = PPLX_API_KEY

chat = ChatPerplexity(temperature=0, pplx_api_key="PPLX_API_KEY", model="sonar-reasoning")


# User input for the question
user_question = st.text_input("Enter the model name:")

if st.button("Get Description"):
    if not PPLX_API_KEY:
         st.error("Please enter your Perplexity API key.")
    elif not user_question:
        st.error("Please enter the model name.")

    else:

        
        headers = {
            "accept": "application/json",
            "content-type": "application/json",
            "authorization": f"Bearer {PPLX_API_KEY}"
        }

        try:
            # Make the API request
            # prompt = ChatPromptTemplate.from_messages([("system", content)])
            chat = ChatPerplexity(
                temperature=0, 
                pplx_api_key=os.environ["PPLX_API_KEY"],
                model="sonar-reasoning"
                )

            prompt = ChatPromptTemplate.from_messages([
                ("system", "You are a helpful AI assistant."),
                ("human", f"Explain the model {user_question}")
            ])
            chain = prompt | chat
            response = chain.invoke({"user_question": user_question})
           

            # Display the answer
            st.subheader("Answer:")
            st.write(response.content)

        except Exception as e:
            # Handle errors gracefully
            st.error(f"An error occurred: {str(e)}")


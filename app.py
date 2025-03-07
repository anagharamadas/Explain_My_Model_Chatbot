import os
from langchain_community.chat_models import ChatPerplexity
import streamlit as st
from langchain_core.prompts import ChatPromptTemplate  # type: ignore
import re

st.title("Explain My Model")
PPLX_API_KEY = st.text_input("Enter your API key: ", type="password")


os.environ["PPLX_API_KEY"] = PPLX_API_KEY

chat = ChatPerplexity(temperature=0, pplx_api_key="PPLX_API_KEY", return_intermediate_steps=False, model="sonar-reasoning")


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
            internal_reasoning_prompt = ChatPromptTemplate.from_messages([
                ("system", "You are a helpful assistant. Reason through the problem without answering yet."),
                ("human", "Explain the model {user_question} internally.")
                ])
            final_response_prompt = ChatPromptTemplate.from_messages([
                ("system", "You are a helpful assistant. Provide a concise answer."),
                ("human", "What is the final explanation of the model?")
            ])
            # Create a chain for internal reasoning
            internal_chain = internal_reasoning_prompt | chat

            # Create a chain for the final response
            final_chain = final_response_prompt | chat


            internal_response = internal_chain.invoke({"user_question": user_question})
            final_response = final_chain.invoke({"user_question": user_question})

            cleaned_output = re.sub(r'<think>.*?</think>', '', final_response.content, flags=re.DOTALL)
           

            # Display the answer
            st.subheader("Answer:")
            st.write(final_response.content)

        except Exception as e:
            # Handle errors gracefully
            st.error(f"An error occurred: {str(e)}")


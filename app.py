import streamlit as st
from langchain.chains import LLMChain
from langchain.llms import OpenAI
import openai
import time

# Initialize the LLM
llm = OpenAI(temperature=0.7)

# Define the prompt template
from langchain.prompts import PromptTemplate

template = """
You are an AI that provides summaries of the latest news articles based on the following query: {query}.
Summarize the most relevant and important information.
"""

prompt = PromptTemplate(input_variables=["query"], template=template)

# Initialize the LLMChain
chain = LLMChain(llm=llm, prompt=prompt)

st.title('Equity Research News Tool')
st.write('Enter your query to get the latest news articles summarized.')

query = st.text_input('Query')

if st.button('Get News'):
    if query:
        try:
            # Attempt to run the chain with the provided query
            response = chain.run(query=query)
            st.write('### Summary:')
            st.write(response)
        except Exception as e:
            error_message = str(e)
            # Handle specific error messages for quota issues
            if "quota" in error_message.lower():
                st.error("API quota exceeded. Please check your plan and billing details.")
            else:
                st.error(f"An error occurred: {error_message}")
    else:
        st.write('Please enter a query.')

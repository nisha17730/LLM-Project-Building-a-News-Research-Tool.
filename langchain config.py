from langchain_core.prompts import PromptTemplate
from langchain_openai import OpenAI
from langchain_core.runnables import RunnableSequence

# Initialize OpenAI API
openai_api_key = 'sk-proj-v97jwPTau3Kbub136UuCT3BlbkFJNEt6OmjOY5P6mrCl3Kl0'
openai = OpenAI(api_key=openai_api_key)

# Define the prompt template
template = """
You are an AI assistant helping an equity research analyst. Given
the following query, summarize the most relevant news articles.
Query: {query}
"""
prompt = PromptTemplate(
    template=template,
    input_variables=['query']
)

# Create a RunnableSequence
sequence = RunnableSequence(prompt, openai)

# Function to get a summary for a query
def get_summary(query):
    response = sequence.invoke({"query": query})
    return response

# Example usage
if __name__ == "__main__":
    query = "Latest news on climate change"
    summary = get_summary(query)
    print(summary)

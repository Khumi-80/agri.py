import streamlit as st
from transformers import pipeline

# Load the pre-trained question-answering model
qa_model = pipeline("question-answering", model="distilbert-base-uncased-distilled-squad")

# Define the gardening knowledge base
context_data = """
In Punjab (Pakistan and India), the month of October is suitable for planting cool-season crops such as carrots, spinach, lettuce, radishes, and peas.
Coriander and fenugreek can also be planted in warmer areas. Tomatoes and onions are best planted in early winter.
Ensure regular watering and well-drained soil for all winter crops.
Avoid planting frost-sensitive crops until temperatures stabilize.
Other suitable vegetables for the season include garlic, turnips, and beets.
"""

# Streamlit app layout
st.title("Kitchen Garden Q&A Bot")
st.write("Ask questions about gardening in Punjab during October:")

# User input for questions
user_question = st.text_input("Your Question:")

if user_question:
    # Get the model's answer from the context
    result = qa_model(question=user_question, context=context_data)
    
    # Display the answer
    st.write("**GardenBot:**", result['answer'])


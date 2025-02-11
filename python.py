import streamlit as st
from langchain_groq import ChatGroq
llm = ChatGroq(
    model="mixtral-8x7b-32768",
    temperature=0,
    groq_api_key="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"
)
st.title("Own Chatbot")
st.write("Enter your query below:")
user_input = st.text_input("Your Question:", "")
if st.button("Get Answer"):
    response = llm.invoke(user_input)
    st.write("### Response:")
    st.write(response)


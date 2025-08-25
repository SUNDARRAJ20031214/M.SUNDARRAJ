import streamlit as st
from PyDictionary import PyDictionary

# Create dictionary object
dictionary = PyDictionary()

st.title("📖 Simple Dictionary Chatbot")

# Get user input
word = st.text_input("Enter a word:")

if word:
    meaning = dictionary.meaning(word)
    if meaning:
        st.write("### Meanings:")
        for pos, defs in meaning.items():
            st.write(f"**{pos}**:")
            for d in defs:
                st.write(f"- {d}")
    else:
        st.write("❌ Word not found")

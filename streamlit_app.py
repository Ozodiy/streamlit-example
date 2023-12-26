# Import the streamlit library
import streamlit as st

# Title of the app
st.title('My First Streamlit App')

# A simple button
if st.button('Say hello'):
    st.write('Why hello there!')
else:
    st.write('Goodbye')

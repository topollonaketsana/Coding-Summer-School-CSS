## The the streamlit app to visualize our data


import streamlit as st

st.title('WELCOME!')

st.write('Lets Play a Game!')

st.header('Number Selection')

number = st.slider('Pick a number', 1, 100)
st.write(f'You picked: {number}')








## my profile


import streamlit as st
import pandas as pd


about_page = st.Page(
    page= '/week 1/streamlit/about.py',
    title= 'About Me',
    default= True
)



# Title of the app
st.title("Researcher Profile Page")

# Collect basic information
name = "Topollo Naketsana"
field = "Astrophysics"
institution = "University of the Western Cape"
research_description = 'The cosmological gravitational wave, understanding how binary black holes creates ripples in spacetime'

# Display basic profile information
st.header("Researcher Overview")
st.write(f"**Name:** {name}")
st.write(f"**Field of Research:** {field}")
st.write(f"**Institution:** {institution}")
st.write(f"**My Research focuses on:** {research_description}")

# Add a section for publications
st.header("Publications")
#uploaded_file = st.file_uploader("Upload a CSV of Publications", type="csv")
st.write( '1. Quantum computing\n\n',
         '2. SpaceTime ripples\n\n',
         '3. Machine Learning classification project\n\n'
         
         )



# Add a section for awards
st.header("Awards")  
st.write('2024:\nReceived a recognition award for attending IAU') 
st.write('2025:\nReceived a recognition award for attending CSS')      



# Add a section for 
st.header("About me")
st.write('I am Topollo Naketsana, I am currently studying my passion for the cosmos at the university of the western cape - Bsc Astrophysics..')


#



# Add a section for visualizing Education
st.header("Education")

st.write('BSc Physics \n')
st.write('University of the western cape')



#st.write()


# Add a contact section
st.header("Contact Information")
email = "topollonaketsana60@gmail.com"
contact_number = '0782806610'
website = 'https://github.com/topollonaketsana'
st.write(f"You can reach {name} at {email}.\n\n")
st.write(f"or you can contact me at {contact_number}.\n\n")
st.write(f"This is my website {website}.\n\n")



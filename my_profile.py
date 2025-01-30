## my profile


import streamlit as st
import pandas as pd


about_page = st.Page(
    page= './week 1/streamlit/about.py',
    title= 'About Me',
    default= True,
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



# Add a section for 
st.header("About me")
st.write(f'Hi, Im Topollo Naketsana, an aspiring astrophysicist currently pursuing my Honours in Astrophysics at the University of the Western Cape (UWC). I have a strong passion for exploring the mysteries of the universe, from exoplanet detection to gravitational waves and black holes. \n\nBeyond academics, I actively work on personal machine learning and astrophysics projects, some of which you can find on my https://github.com/topollonaketsana.')


#



# Add a section for Education
st.header("Education")

st.write('I hold a BSc in Physics, where I studied:\n\n\n',
        '🔹 Mathematics (Calculus, Linear Algebra, ODEs)\n\n',
        '🔹 Physics (Classical Mechanics, Quantum Mechanics, Astronomy)\n\n',
        '🔹 Computational Physics (Python, Machine Learning, Scientific Computing)\n\n'

)

st.write('University of the western cape')



#st.write()


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





# Add a contact section
st.header("Contact Information")
email = "topollonaketsana60@gmail.com"
contact_number = '0782806610'
website = 'https://github.com/topollonaketsana'
st.write(f"You can reach {name} at {email}.\n\n")
st.write(f"or you can contact me at {contact_number}.\n\n")
st.write(f"This is my website {website}.\n\n")


pg = st.navigation(
    {
        'info': [about_page]
    }
      


)
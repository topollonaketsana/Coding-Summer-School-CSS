## my profile


import streamlit as st
import pandas as pd

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
uploaded_file = st.file_uploader("Upload a CSV of Publications", type="csv")

if uploaded_file:
    publications = pd.read_csv(uploaded_file)
    st.dataframe(publications)

    # Add filtering for year or keyword
    keyword = st.text_input("Filter by keyword", "")
    if keyword:
        filtered = publications[
            publications.apply(lambda row: keyword.lower() in row.astype(str).str.lower().values, axis=1)
        ]
        st.write(f"Filtered Results for '{keyword}':")
        st.dataframe(filtered)
    else:
        st.write("Showing all publications")


# Add a section for awards
st.header("Awards")  
st.write('2024:\nReceived a recognition award for attending IAU') 
st.write('2025:\nReceived a recognition award for attending CSS')      



# Add a section for 
st.header("About me")
st.write('I am Topollo Naketsana, I am currently studying my passion for the cosmos at the university of the western cape - Bsc Astrophysics..')


# Add a section for visualizing publication trends
st.header("Publication Trends")

if uploaded_file:
    if "Year" in publications.columns:
        year_counts = publications["Year"].value_counts().sort_index()
        st.bar_chart(year_counts)
    else:
        st.write("The CSV does not have a 'Year' column to visualize trends.")



# Add a section for visualizing Education
st.header("Education")

st.write('BSc Physics \n')
st.write('University of the western cape')



#st.write()


# Add a contact section
st.header("Contact Information")
email = "topollonaketsana60@gmail.com"
st.write(f"You can reach {name} at {email}.")



#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 29 12:00:53 2025

@author: socco
"""

import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image

# Title of the app
st.title("Researcher Profile Page")

# Collect basic information
name = "Anele Ntokozo Mahlangu"
field = "Oceanography"
institution = "University of Cape Town"

# Display basic profile information
st.header("Researcher Overview")
st.write(f"**Name:** {name}")
st.write(f"**Field of Research:** {field}")
st.write(f"**Institution:** {institution}")

# Load the image
image_path = "Picture_AN.jpeg"

try:
    image = Image.open(image_path)
except FileNotFoundError:
    st.error(f"Image not found at the specified path: {image_path}")
    st.stop()

# Resize the image using thumbnail while keeping the aspect ratio
#max_size = (200, 200)  # Max size for width and height
#image.thumbnail(max_size)

# Display the resized image
st.image("Picture_AN.jpeg")
#st.image(image, caption="Profile Picture", use_container_width=False)

 # Professional Summary Button
st.button("Professional Summary")
st.write("My name is Anele Mahlangu, and I am a Master’s student in Ocean and Atmospheric Sciences at the University of Cape Town. Originally from Siyabuswa, a rural area in Mpumalanga, South Africa, I was raised by my grandmother and single mother. I obtained my Bachelor of Science (Honours) in Microbiology and Biotechnology from the University of the Witwatersrand, where I developed a strong passion for research. Although I started without a background in oceanography, I quickly adapted despite the challenges, and I am committed to excelling in this field. My interest in oceanography stems from the ocean's vital role in shaping Earth’s climate and ecosystems. Along the way, I have also gained proficiency in programming languages, including Python, MATLAB, and the Centre for High Performance Computing (CHPC), which were completely new to me when I began.")

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

# Add a section for visualizing publication trends
st.header("Publication Trends")
if uploaded_file:
    if "Year" in publications.columns:
        year_counts = publications["Year"].value_counts().sort_index()
        st.bar_chart(year_counts)
    else:
        st.write("The CSV does not have a 'Year' column to visualize trends.")

# Add a contact section
st.header("Contact Information")
email = "anelee888@gmail.com"
st.write(f"You can reach {name} at {email}.")

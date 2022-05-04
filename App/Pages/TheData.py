import streamlit as st
import altair as alt
import pandas as pd

class TheDataPage:
    def __init__(self) -> None:
        # TODO: Define page-specific variables here
        pass

    def display(self):
        # TODO: define the streamlit view here
        st.header("About the Data")
        
    option = st.selectbox(
     'Select the following factors to see if they are potential causes of Heart Disease?',
     ('Stroke', 'Smoking', 'Sex', 'Smoking', 'AlcoholDrinking', 'Asthma', 'DiffWalking', 'PhysicalActivity', 'KidneyDisease', 'SkinCancer'))
    st.write('You selected:', option)
        
     df = pd.read_csv('heart_2020_cleaned.csv')
    
    stroke =df[df['HeartDisease'] == 'Yes']["Stroke"].value_counts().to_frame().reset_index()
    alt.Chart(stroke).mark_bar().encode(
    y= "Stroke:Q",
    x= "index:O")
    
    smoking=df[df['HeartDisease'] == 'Yes']["Smoking"].value_counts().to_frame().reset_index()
    alt.Chart(smoking).mark_bar().encode(
    y= "Smoking:Q",
    x= "index:O")
       
    alcoholdrinking=df[df['HeartDisease'] == 'Yes']["AlcoholDrinking"].value_counts().to_frame().reset_index()
    alt.Chart(alcoholdrinking).mark_bar().encode(
    y= "AlcoholDrinking:Q",
    x= "index:O")
    
    sex =df[df['HeartDisease'] == 'Yes']["Sex"].value_counts().to_frame().reset_index()
    alt.Chart(sex).mark_bar().encode(
    y= "Sex:Q",
    x= "index:O")

    asthma=df[df['HeartDisease'] == 'Yes']["Asthma"].value_counts().to_frame().reset_index()
    alt.Chart(asthma).mark_bar().encode(
    y= "Asthma:Q",
    x= "index:O")
    
    physicalactivity=df[df['HeartDisease'] == 'Yes']["PhysicalActivity"].value_counts().to_frame().reset_index()
    alt.Chart(physicalactivity).mark_bar().encode(
    y= "PhysicalActivity:Q",
    x= "index:O")
    
    diffwalking =df[df['HeartDisease'] == 'Yes']["DiffWalking"].value_counts().to_frame().reset_index()
    alt.Chart(diffwalking).mark_bar().encode(
    y= "DiffWalking:Q",
    x= "index:O")
    
    kidneydisease =df[df['HeartDisease'] == 'Yes']["KidneyDisease"].value_counts().to_frame().reset_index()
    alt.Chart(kidneydisease).mark_bar().encode(
    y= "KidneyDisease:Q",
    x= "index:O")
    
    skincancer =df[df['HeartDisease'] == 'Yes']["SkinCancer"].value_counts().to_frame().reset_index()
    alt.Chart(skincancer).mark_bar().encode(
    y= "SkinCancer:Q",
    x= "index:O")

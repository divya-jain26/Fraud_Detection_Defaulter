import streamlit as st
import pandas as pd

header=st.beta_container()
dataset=st.beta_container()
features=st.beta_container()
modelTraining=st.beta_container()

with header:
    st.title('Welcome to my awesome data science project!')
    st.text('In this Project I look into the transactions of taxis in NYC. ...')


with dataset:
    st.header('Fraud Detection Dataset')
    st.text('I like this dataset')

    data=pd.read_csv('C:/Users/EJAIDIV/Downloads/DataScientist-Casestudy(1)/DataScientist-Casestudy/CaseStudy_FraudIdentification.csv')
    st.write(data.head())
    st.write(data.info())




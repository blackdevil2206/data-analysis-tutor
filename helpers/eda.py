import streamlit as st

def generate_summary(df):
    st.write("**Shape:**", df.shape)
    
    st.write("**Column Types:**")
    st.write(df.dtypes)

    st.write("**Missing Values:**")
    st.write(df.isnull().sum())

    st.write("**Descriptive Statistics:**")
    st.write(df.describe(include='all'))
    
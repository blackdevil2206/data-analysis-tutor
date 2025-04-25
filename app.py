import streamlit as st
import pandas as pd
from helpers.eda import generate_summary
from helpers.visualizations import show_visualizations

st.set_page_config(page_title="Data Analysis Tutor", layout="wide")
st.title("📊 Data Analysis Tutor")
st.markdown("Upload your dataset and get instant analysis & insights.")

uploaded_file = st.file_uploader("Upload your dataset (CSV or Excel)", type=['csv', 'xlsx'])

if uploaded_file:
    try:
        if uploaded_file.name.endswith('.csv'):
            df = pd.read_csv(uploaded_file)
        else:
            df = pd.read_excel(uploaded_file)

        st.success("✅ File successfully uploaded!")
        st.subheader("📌 Dataset Preview")
        st.dataframe(df.head())

        st.subheader("📊 Summary Statistics")
        generate_summary(df)

        st.subheader("📈 Visualizations")
        show_visualizations(df)

    except Exception as e:
        st.error(f"⚠️ Error reading file: {e}")
else:
    st.info("Please upload a CSV or Excel file to begin.")
    
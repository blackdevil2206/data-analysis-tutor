import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt

def show_visualizations(df):
    numeric_cols = df.select_dtypes(include='number').columns

    if len(numeric_cols) == 0:
        st.warning("No numeric columns found for visualization.")
        return

    col = st.selectbox("Select a column for histogram", numeric_cols)
    
    fig, ax = plt.subplots()
    sns.histplot(df[col], kde=True, ax=ax)
    st.pyplot(fig)

    if len(numeric_cols) >= 2:
        x_col = st.selectbox("X-axis for scatter plot", numeric_cols)
        y_col = st.selectbox("Y-axis for scatter plot", numeric_cols, index=1)
        
        fig2, ax2 = plt.subplots()
        sns.scatterplot(x=df[x_col], y=df[y_col], ax=ax2)
        st.pyplot(fig2)
    
import streamlit as st
import pandas as pd

st.title("Life Expectancy Data Analysis")

st.write(
    "This application demonstrates data cleaning and analysis "
    "using the Life Expectancy dataset."
)

df = pd.read_csv("data/cleaned_life_expectancy.csv")

st.subheader("Dataset Overview")

col1, col2 = st.columns(2)

with col1:
    st.metric("Rows", df.shape[0])

with col2:
    st.metric("Columns", df.shape[1])

st.subheader("Cleaned Dataset")

st.dataframe(df.head(20))

st.subheader("Life Expectancy Distribution")

st.bar_chart(
    df["Life expectancy"].value_counts().sort_index()
)

st.subheader("Average Life Expectancy by Year")

yearly_data = df.groupby("Year")["Life expectancy"].mean()

st.line_chart(yearly_data)
# importing the required libraries
import streamlit as st
import altair as alt
import seaborn as sns
import pandas as pd
import plotly.express as px
from matplotlib import pyplot as plt
from streamlit_extras.dataframe_explorer import dataframe_explorer

# setting page configurations
def main():

 st.set_page_config(page_title="📊Data Analysis Dashboard", layout="wide")

 st.title("📊Data Analysis Dashboard")
 

 # load the dataset
 df = pd.read_csv("./data/data.csv")
 #st.write(df)
 #st.dataframe(df)

 # sidebar
 st.sidebar.image("./data/image.jpg", use_column_width=True)

 # sidebar date picker
 with st.sidebar:
    st.title("Select Date Range")
    start_date = st.date_input("Start Date", value=pd.to_datetime(df["OrderDate"]).min())
    end_date = st.date_input("End Date", value=pd.to_datetime(df["OrderDate"]).max())

    # filter the dataset by prefered dates
    df = df[(df["OrderDate"] >= str(start_date)) & (df['OrderDate'] <= str(end_date))]

    st.write(df)

    st.success("You have choosen analytics from" + str(start_date) + " to " +str(end_date))




if __name__=="__main__":
    main()

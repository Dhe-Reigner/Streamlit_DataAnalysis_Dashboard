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
 st.sidebar.image("./data/image.jpg", use_container_width=True)


 # sidebar date picker
 with st.sidebar:
    st.title("Select Date Range")
    start_date = st.date_input("Start Date", value=pd.to_datetime(df["OrderDate"]).min())
    end_date = st.date_input("End Date", value=pd.to_datetime(df["OrderDate"]).max())

# filter date range
 df1 = df[(df["OrderDate"] >= str(start_date)) & (df['OrderDate'] <= str(end_date))]

 st.write(df1)

 st.success("You have choosen analytics from" + str(start_date) + " to " +str(end_date))


 # Expander  for filtering the dataset
 with st.expander('Filter Excel Data'):
    filtered_data = dataframe_explorer(df1,case=False)
    st.dataframe(filtered_data,use_container_width=True)

 # columns
 a1, a2 = st.columns(2)

 with a1:
    st.subheader("Product & Quantities", divider='rainbow')
    
    if df1.empty:
       st.warning('No data available for the selected date range')
    else:
       source = df1.rename(columns={'Quantity':'quantity'})

       bar_chart = (
          alt.Chart(source)
          .mark_bar()
          .encode(
             x=alt.X('sum(quantity):Q', title='Total Quantity'),
             y=alt.Y("Product:N", sort='-x'),
             tooltip=['Product:N', 'sum(quantity):Q']
          )
       )
    st.altair_chart(bar_chart,use_container_width=True)

 with a2:
    st.subheader("Data Metrics", divider='rainbow')
    from streamlit_extras.metric_cards import style_metric_cards
    col1,col2=st.columns(2)
    col1.metric(label="All number of Items", value=df1.Product.count(),delta="All Items in Dataset", delta_color="normal")
    col2.metric(label="Sum of Product Price USD", value=f"{df1.TotalPrice.sum():,.0f}", delta=df1.TotalPrice.median())

    col11,col12,col13 = st.columns(3)
    col11.metric(label="Maximum Price", value=f"{df1.TotalPrice.max():,.0f}",delta="High Price")
    col12.metric(label="Maximum Price", value=f"{df1.TotalPrice.min():,.0f}",delta="High Price")
    col13.metric(label="Price Range", value=f"{df1.TotalPrice.max()-df1.TotalPrice.min():,.0f}",delta="Range")

    # style the metric
    style_metric_cards(background_color= "#FFF",
    border_size_px = 1,
    border_color = "#CCC",
    border_radius_px = 5,
    border_left_color  = "#9AD8E1",
    box_shadow = True)
 
 b1,b2 = st.columns(2)
 # dot plot
 with b1:
    st.subheader("Products & Total Price",divider='rainbow')
    source = df1
    chart = alt.Chart(source).mark_circle().encode(
       x = 'Product',
       y = 'TotalPrice',
       color = 'Category'
    ).interactive()
    st.altair_chart(chart,theme='streamlit',use_container_width=True)

 with b2:
    st.subheader("Product & UnitPrice", divider='rainbow')
    
    energy_source = pd.DataFrame({
      'Product':df1['Product'],
      'UnitPrice ($)': df1['UnitPrice'],
      'Date': df1['OrderDate']
    })

    bar_chart = (
      alt.Chart(energy_source)
      .mark_bar()
      .encode(
          x='month(Date):O',
          y='sum(UnitPrice ($)):Q',
          color='Product:N'
      )
    )
    st.altair_chart(bar_chart,use_container_width=True)




if __name__=="__main__":
    main()

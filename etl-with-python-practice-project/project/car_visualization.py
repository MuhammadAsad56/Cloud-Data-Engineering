# car_visualization.py
import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Car Data Visualization", layout="wide")
st.title("🚗 Car Data Visualization Dashboard")

# --- Load CSV ---
@st.cache_data
def load_data():
    df = pd.read_csv("pakwheels_cars.csv")  # Make sure your CSV is named cars_data.csv
    return df

df = load_data()
st.subheader("Sample of Car Data")
st.dataframe(df.head())

# --- 1. Bar Chart: Number of Cars by Brand ---
st.subheader("Number of Cars by Brand")
if 'brand' in df.columns:
    brand_counts = df['brand'].value_counts()
    fig1 = px.bar(x=brand_counts.index, y=brand_counts.values,
                  labels={'x':'Brand','y':'Count'}, color=brand_counts.values)
    st.plotly_chart(fig1)
else:
    st.warning("Column 'brand' not found in CSV.")

# --- 2. Histogram: Price Distribution ---
st.subheader("Price Distribution")
if 'price' in df.columns:
    fig2 = px.histogram(df, x='price', nbins=30, labels={'price':'Price'})
    st.plotly_chart(fig2)
else:
    st.warning("Column 'price' not found in CSV.")

# --- 3. Box Plot: Price by Brand ---
st.subheader("Price by Brand")
if 'price' in df.columns and 'brand' in df.columns:
    fig3 = px.box(df, x='brand', y='price', labels={'brand':'Brand','price':'Price'})
    st.plotly_chart(fig3)
else:
    st.warning("Columns 'price' or 'brand' not found in CSV.")

# --- 4. Scatter Plot: Mileage vs Price ---
st.subheader("Mileage vs Price")
if 'mileage' in df.columns and 'price' in df.columns:
    fig4 = px.scatter(df, x='mileage', y='price', color='brand' if 'brand' in df.columns else None,
                      labels={'mileage':'Mileage','price':'Price'})
    st.plotly_chart(fig4)
else:
    st.warning("Columns 'mileage' or 'price' not found in CSV.")

# --- 5. Pie Chart: Fuel Type Distribution ---
st.subheader("Fuel Type Distribution")
if 'fuel_type' in df.columns:
    fuel_counts = df['fuel_type'].value_counts()
    fig5 = px.pie(values=fuel_counts.values, names=fuel_counts.index)
    st.plotly_chart(fig5)
else:
    st.warning("Column 'fuel_type' not found in CSV.")

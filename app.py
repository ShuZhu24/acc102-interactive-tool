import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Coca-Cola Sales Analysis", layout="wide")

st.title("Coca-Cola Sales Data Analysis Dashboard")

@st.cache_data  
def load_data():
    df = pd.read_csv('CocaCola_Ventas_Mundiales.csv') 
    df['Profit'] = (df['Precio Unitario (USD)'] - df['Costo Unitario (USD)']) * df['Unidades Vendidas']
    return df

df = load_data()

st.sidebar.header("Filter data")

all_countries = df['País'].unique().tolist()
selected_countries = st.sidebar.multiselect(
    "Select Country",
    all_countries,
    default=all_countries  
)

all_products = df['Producto'].unique().tolist()
selected_products = st.sidebar.multiselect(
    "Select Product",
    all_products,
    default=all_products
)

filtered_df = df[
    df['País'].isin(selected_countries) & 
    df['Producto'].isin(selected_products)
]

st.subheader("Key Indicators")

col1, col2, col3, col4 = st.columns(4)

total_quantity = filtered_df['Unidades Vendidas'].sum()
total_sales = (filtered_df['Unidades Vendidas'] * filtered_df['Precio Unitario (USD)']).sum()
total_profit = filtered_df['Profit'].sum()
avg_price = filtered_df['Precio Unitario (USD)'].mean()

col1.metric("Total Sales Volume", f"{total_quantity:,.0f}")
col2.metric("Total Sales Revenue ", f"${total_sales:,.0f}")
col3.metric("Total Profit ", f"${total_profit:,.0f}")
col4.metric("Average Unit Price", f"${avg_price:.2f}")

st.subheader("Product Sales Ranking")

product_sales = filtered_df.groupby('Producto')['Unidades Vendidas'].sum().sort_values()

fig1, ax1 = plt.subplots(figsize=(10, 6))
product_sales.plot(kind='barh', ax=ax1)
ax1.set_title('Product Sales Volume')
ax1.set_xlabel('Sales Volume')
ax1.set_ylabel('Product')
st.pyplot(fig1)

st.subheader("National Sales Ranking (Top 8)")

country_sales = filtered_df.groupby('País')['Unidades Vendidas'].sum().sort_values(ascending=False).head(8)

fig2, ax2 = plt.subplots(figsize=(10, 6))
country_sales.plot(kind='bar', ax=ax2)
ax2.set_title('Top 8 Countries by Sales Volume')
ax2.set_xlabel('Country')
ax2.set_ylabel('Sales Volume')
plt.xticks(rotation=45)
st.pyplot(fig2)

st.subheader("Monthly Sales Trend")

monthly_sales = filtered_df.groupby('Mes')['Unidades Vendidas'].sum()

fig3, ax3 = plt.subplots(figsize=(10, 5))
monthly_sales.plot(kind='line', marker='o', ax=ax3)
ax3.set_title('Monthly Sales Trend')
ax3.set_xlabel('Month')
ax3.set_ylabel('Sales Volume')
ax3.grid(True)
st.pyplot(fig3)

st.subheader("Profit Proportion of Sales Channels")

channel_profit = filtered_df.groupby('Canal de Venta')['Profit'].sum()

fig4, ax4 = plt.subplots(figsize=(8, 8))
ax4.pie(channel_profit, labels=channel_profit.index, autopct='%1.1f%%')
ax4.set_title('Profit Share by Sales Channel')
st.pyplot(fig4)

st.subheader("Data Preview")
st.dataframe(filtered_df.head(100))

st.markdown("---")
st.caption("Data Source: Coca-Cola Sales Dataset from Kaggle | Analysis Tool: Streamlit")
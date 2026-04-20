import streamlit as st
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt

st.set_page_config(page_title="Coca-Cola Sales Analysis", layout="wide")

st.title("Coca-Cola Sales Data Analysis Dashboard")

@st.cache_data
def load_sales_data():
    df = pd.read_csv('CocaCola_Ventas_Mundiales.csv')
    df['Profit'] = (df['Precio Unitario (USD)'] - df['Costo Unitario (USD)']) * df['Unidades Vendidas']
    return df

@st.cache_data
def load_stock_data():
    df = pd.read_csv('KO_CocaCola_Stock_Prices_1980_2026.csv')
    df['Date'] = pd.to_datetime(df['Date'])
    return df

df_sales = load_sales_data()
df_stock = load_stock_data()

st.sidebar.title("📊 Navigation Panel")

analysis_tab = st.sidebar.radio(
    "Select Analysis Module",
    ["📈 Sales Data Analysis", "💰 Stock Price Analysis"]
)

# ==================== Sales Data Analysis Module ====================
if analysis_tab == "📈 Sales Data Analysis":
    st.title("🥤 Coca-Cola Global Sales Data Analysis")
    
    st.sidebar.subheader("Filter Options")
    
    countries = df_sales['País'].unique().tolist()
    selected_countries = st.sidebar.multiselect(
        "Select Country",
        countries,
        default=countries[:3]
    )
    
    products = df_sales['Producto'].unique().tolist()
    selected_products = st.sidebar.multiselect(
        "Select Product",
        products,
        default=products[:3]
    )
    
    filtered_df = df_sales[
        (df_sales['País'].isin(selected_countries)) &
        (df_sales['Producto'].isin(selected_products))
    ]
    
    st.subheader("Key Indicators")
    
    col1, col2, col3, col4 = st.columns(4)
    
    total_quantity = filtered_df['Unidades Vendidas'].sum()
    total_sales = (filtered_df['Unidades Vendidas'] * filtered_df['Precio Unitario (USD)']).sum()
    total_profit = filtered_df['Profit'].sum()
    avg_price = filtered_df['Precio Unitario (USD)'].mean()
    
    col1.metric("Total Sales Volume", f"{total_quantity:,.0f}")
    col2.metric("Total Sales Revenue", f"${total_sales:,.0f}")
    col3.metric("Total Profit", f"${total_profit:,.0f}")
    col4.metric("Average Unit Price", f"${avg_price:.2f}")
    
    # Product Sales Ranking
    st.subheader("Product Sales Ranking")
    product_sales = filtered_df.groupby('Producto')['Unidades Vendidas'].sum().sort_values()
    
    fig1, ax1 = plt.subplots(figsize=(10, 6))
    product_sales.plot(kind='barh', ax=ax1)
    ax1.set_title('Product Sales Volume')
    ax1.set_xlabel('Sales Volume')
    ax1.set_ylabel('Product')
    st.pyplot(fig1)
    
    # Country Sales Ranking
    st.subheader("Country Sales Ranking (Top 8)")
    country_sales = filtered_df.groupby('País')['Unidades Vendidas'].sum().sort_values(ascending=False).head(8)
    
    fig2, ax2 = plt.subplots(figsize=(10, 6))
    country_sales.plot(kind='bar', ax=ax2)
    ax2.set_title('Top 8 Countries by Sales Volume')
    ax2.set_xlabel('Country')
    ax2.set_ylabel('Sales Volume')
    plt.xticks(rotation=45)
    st.pyplot(fig2)
    
    # Monthly Sales Trend
    st.subheader("Monthly Sales Trend")
    monthly_sales = filtered_df.groupby('Mes')['Unidades Vendidas'].sum()
    
    fig3, ax3 = plt.subplots(figsize=(10, 5))
    monthly_sales.plot(kind='line', marker='o', ax=ax3)
    ax3.set_title('Monthly Sales Trend')
    ax3.set_xlabel('Month')
    ax3.set_ylabel('Sales Volume')
    ax3.grid(True)
    st.pyplot(fig3)
    
    # Profit Share by Sales Channel
    st.subheader("Profit Share by Sales Channel")
    channel_profit = filtered_df.groupby('Canal de Venta')['Profit'].sum()
    
    fig4, ax4 = plt.subplots(figsize=(8, 8))
    ax4.pie(channel_profit, labels=channel_profit.index, autopct='%1.1f%%')
    ax4.set_title('Profit Share by Sales Channel')
    st.pyplot(fig4)
    
    st.subheader("Data Preview")
    st.dataframe(filtered_df.head(100))

# ==================== Stock Price Analysis Module ====================
elif analysis_tab == "💰 Stock Price Analysis":
    st.title("📈 Coca-Cola Stock Price Analysis (1980-2026)")
    
    col1, col2, col3 = st.columns(3)
    
    start_price = df_stock['Close'].iloc[0]
    end_price = df_stock['Close'].iloc[-1]
    total_return = (end_price - start_price) / start_price * 100
    
    with col1:
        st.metric("Starting Price (1980)", f"${start_price:.2f}")
    with col2:
        st.metric("Latest Price", f"${end_price:.2f}")
    with col3:
        st.metric("Total Return", f"{total_return:.1f}%")
    
    min_year = int(df_stock['Date'].dt.year.min())
    max_year = int(df_stock['Date'].dt.year.max())
    
    st.subheader("📅 Year Range Filter")
    year_range = st.slider(
        "Select Year Range",
        min_year,
        max_year,
        (min_year, max_year)
    )
    
    mask = (df_stock['Date'].dt.year >= year_range[0]) & (df_stock['Date'].dt.year <= year_range[1])
    filtered_stock = df_stock[mask]
    
    st.subheader("📉 Stock Price Trend")
    fig_stock = px.line(filtered_stock, x='Date', y='Close',
                         title=f'Coca-Cola Stock Price ({year_range[0]}-{year_range[1]})',
                         labels={'Close': 'Stock Price (USD)', 'Date': 'Date'})
    fig_stock.update_traces(line_color='#2E86AB', line_width=2)
    st.plotly_chart(fig_stock, use_container_width=True)
    
    if 'Volume' in df_stock.columns:
        st.subheader("📊 Monthly Trading Volume")
        fig_volume = px.bar(filtered_stock, x='Date', y='Volume',
                             title='Trading Volume Over Time',
                             labels={'Volume': 'Trading Volume', 'Date': 'Date'})
        st.plotly_chart(fig_volume, use_container_width=True)
    
    st.subheader("📋 Annual Stock Statistics")
    df_stock['Year'] = df_stock['Date'].dt.year
    yearly_stats = df_stock.groupby('Year')['Close'].agg(['mean', 'min', 'max']).reset_index()
    yearly_stats.columns = ['Year', 'Average Price', 'Min Price', 'Max Price']
    yearly_stats = yearly_stats[(yearly_stats['Year'] >= year_range[0]) & (yearly_stats['Year'] <= year_range[1])]
    
    st.dataframe(yearly_stats, use_container_width=True)

# ==================== Footer ====================
st.markdown("---")
st.caption("Data Source: Coca-Cola Sales Dataset from Kaggle | Stock Data: Yahoo Finance | Tool: Streamlit")
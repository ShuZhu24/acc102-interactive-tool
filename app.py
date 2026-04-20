import streamlit as st
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt

st.set_page_config(page_title="Coca-Cola Sales Analysis", layout="wide")

st.title("Coca-Cola Sales Data Analysis Dashboard")

@st.cache_data  
def load_data():
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

st.sidebar.title("📊 导航面板")

analysis_tab = st.sidebar.radio(
    "选择分析模块",
    ["📈 销售数据分析", "💰 股票价格分析"]
)

if analysis_tab == "📈 销售数据分析":
    st.title("🥤 Coca-Cola 全球销售数据分析")

st.sidebar.subheader("筛选条件")

countries = df_sales['Country'].unique().tolist()
selected_countries = st.sidebar.multiselect(
        "选择国家", 
        countries, 
        default=countries[:3])

products = df_sales['Product'].unique().tolist()
selected_products = st.sidebar.multiselect(
        "选择产品", 
        products, 
        default=products[:3]

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

elif analysis_tab == "💰 股票价格分析":
    st.title("📈 Coca-Cola 股票价格分析 (1980-2026)")
    
    col1, col2, col3 = st.columns(3)
    
    start_price = df_stock['Close'].iloc[0]
    end_price = df_stock['Close'].iloc[-1]
    total_return = (end_price - start_price) / start_price * 100
    
    with col1:
        st.metric("起始股价 (1980)", f"${start_price:.2f}")
    with col2:
        st.metric("最新股价", f"${end_price:.2f}")
    with col3:
        st.metric("累计回报率", f"{total_return:.1f}%")
    
    min_year = int(df_stock['Date'].dt.year.min())
    max_year = int(df_stock['Date'].dt.year.max())
    
    st.subheader("📅 年份范围筛选")
    year_range = st.slider(
        "选择年份范围", 
        min_year, 
        max_year, 
        (min_year, max_year)
    )
    
    mask = (df_stock['Date'].dt.year >= year_range[0]) & (df_stock['Date'].dt.year <= year_range[1])
    filtered_stock = df_stock[mask]
    
    st.subheader("📉 股价历史趋势")
    fig3 = px.line(filtered_stock, x='Date', y='Close',
                    title=f'Coca-Cola 股价走势 ({year_range[0]}-{year_range[1]})',
                    labels={'Close': '股价 (USD)', 'Date': '日期'})
    fig3.update_traces(line_color='#2E86AB', line_width=2)
    st.plotly_chart(fig3, use_container_width=True)
    
    if 'Volume' in df_stock.columns:
        st.subheader("📊 月度交易量")
        fig4 = px.bar(filtered_stock, x='Date', y='Volume',
                       title='交易量变化',
                       labels={'Volume': '交易量', 'Date': '日期'})
        st.plotly_chart(fig4, use_container_width=True)
    
    st.subheader("📋 年度股价统计")
    df_stock['Year'] = df_stock['Date'].dt.year
    yearly_stats = df_stock.groupby('Year')['Close'].agg(['mean', 'min', 'max']).reset_index()
    yearly_stats.columns = ['年份', '平均股价', '最低价', '最高价']
    yearly_stats = yearly_stats[(yearly_stats['年份'] >= year_range[0]) & (yearly_stats['年份'] <= year_range[1])]
    
    st.dataframe(yearly_stats, use_container_width=True)




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
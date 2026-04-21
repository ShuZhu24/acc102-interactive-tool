Coca-Cola Global Sales Interactive Dashboard
This interactive tool enables sales managers and marketing analysts to quickly examine Coca-Cola's global sales performance across different countries, products, and time periods.Users can interactively filter data to identify top-performing regions and seasonal trends without writing any code.In addition, you can access stock data up to 2026, helping you gain a better understanding of the Coca-Cola Company's business performance.
2. Data
   Source: Coca-Cola World Sales Dataset (publicly available on Kaggle)
   Access Date: 2026-04-20
  Key Fields: 
  - `Country` - Sales region/country
  - `Product` - Product category (e.g., Coca-Cola, Sprite, Fanta)
  - `Year` / `Month` - Time period
  - `Sales` - Total sales amount (in USD)
  - `Profit` - Total profit (in USD)
Sales Data
  Source: Coca-Cola World Sales Dataset (Kaggle)
  Access Date: 2026-04-10
  Key Fields: Country, Product, Sales, Profit, Sales Channel
Stock Price Data 
  Source:publicly available on Kaggle
  Access Date: 2026-04-20
  Ticker: KO (Coca-Cola)
  Date Range: 1980 - 2026
  Key Fields: Date, Close Price, Trading Volume
3. Methods
 1)Data Loading & Cleaning**: Loaded CSV file using pandas, checked for missing values, converted date columns to datetime format
 2)Exploratory Analysis**: Calculated total sales by country, product, and time period using groupby aggregations
 3)Visualization**: Created interactive charts using Plotly Express (bar charts for country comparison, line charts for time trends)
 4)Interactive Dashboard**: Built a Streamlit app with dropdown filters allowing users to select country and product to dynamically update charts
### Sales Data Analysis
  1. **Data Loading & Cleaning**: Loaded CSV file using pandas...
  2. **Exploratory Analysis**: Calculated total sales by country...
  3. **Visualization**: Created interactive charts using Plotly...

### Stock Price Analysis (New!)
  4. **Stock Data Processing**: Loaded historical stock prices from CSV, converted Date column to   datetime
  5. **Time Series Analysis**: Calculated cumulative returns, yearly statistics
  6. **Interactive Features**: Added year range slider for dynamic filtering

4. Key Findings
 1)Top-performing country**: United States generates the highest total sales ($2.8M), followed by Mexico and Brazil
 2)Best-selling product**: Coca-Cola Classic accounts for approximately 45% of global sales
 3)Seasonal trend**: Sales peak in Q4 (October-December), likely due to holiday season demand
 4)Profit margin varies**: Sprite has the highest profit margin (28%), while Diet Coke has the lowest (18%)
 5)Growth opportunity**: Asian markets (India, China) show 15% year-over-year growth, outpacing mature markets
   ### Sales Findings
- **Top-performing country**: United States generates the highest total sales ($2.8M)
- **Best-selling product**: Coca-Cola Classic accounts for approximately 45% of global sales
- **Seasonal trend**: Sales peak in Q4 (October-December)

### Stock Market Findings (New!)
- **Long-term growth**: KO stock has delivered approximately 800% cumulative return since 1980
- **Price range**: Trading between $5 and $65 over the past 46 years
- **Volume trends**: Trading volume peaks during market volatility events

6. How to run
   Option A: Use the deployed app (no installation needed)
   Click the product link in Section 6 below

   Option B: Run locally
   1.Clone this repository
   2.Install dependencies:
   ```bash
   pip install -r requirements.txt
 7. Product link / Demo
- **Deployed App**: [https://acc102-interactive-tool-dmmydbvrnjwp8qhfupw5lc.streamlit.app/]
- **Demo Video**: [Link to your 1-3 minute demo video] 
- **GitHub Repository**: https://github.com/ShuZhu24/acc102-interactive-tool

 8. Limitations & next steps
  Limitations
- Data only covers 2020-2024, not including 2025 figures
- Some smaller countries are grouped as "Other" due to low sales volume
- Exchange rates are not normalized (all figures in nominal USD)
- ### Limitations
- Sales data only covers 2020-2024
- Stock data does not include dividends or stock splits adjustments
- No correlation analysis between sales performance and stock price

### Next steps
- Add correlation chart between quarterly sales and stock returns
- Integrate real-time stock price via yfinance API
- Add dividend yield analysis


  Next steps
- Add forecasting feature to predict next quarter sales using simple linear regression
- Integrate real-time data via API
- Add more interactive filters (year range, profit margin threshold)

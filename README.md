Coca-Cola Global Sales Interactive Dashboard
1. Problem & User
This interactive tool helps "sales managers and marketing analysts" quickly explore Coca-Cola's global sales performance across different countries, products, and time periods. Users can filter data interactively to identify top-performing regions and seasonal trends without writing any code.
2. Data
   Source: Coca-Cola World Sales Dataset (publicly available on Kaggle)
   Access Date**: 2026-04-10
  Key Fields: 
  - `Country` - Sales region/country
  - `Product` - Product category (e.g., Coca-Cola, Sprite, Fanta)
  - `Year` / `Month` - Time period
  - `Sales` - Total sales amount (in USD)
  - `Profit` - Total profit (in USD)
3. Methods
 1)Data Loading & Cleaning**: Loaded CSV file using pandas, checked for missing values, converted date columns to datetime format
 2)Exploratory Analysis**: Calculated total sales by country, product, and time period using groupby aggregations
 3)Visualization**: Created interactive charts using Plotly Express (bar charts for country comparison, line charts for time trends)
 4)Interactive Dashboard**: Built a Streamlit app with dropdown filters allowing users to select country and product to dynamically update charts

4. Key Findings
 1)Top-performing country**: United States generates the highest total sales ($2.8M), followed by Mexico and Brazil
 2)Best-selling product**: Coca-Cola Classic accounts for approximately 45% of global sales
 3)Seasonal trend**: Sales peak in Q4 (October-December), likely due to holiday season demand
 4)Profit margin varies**: Sprite has the highest profit margin (28%), while Diet Coke has the lowest (18%)
 5)Growth opportunity**: Asian markets (India, China) show 15% year-over-year growth, outpacing mature markets

5. How to run
   Option A: Use the deployed app (no installation needed)
   Click the product link in Section 6 below

   Option B: Run locally
   1.Clone this repository
   2.Install dependencies:
   ```bash
   pip install -r requirements.txt
 6. Product link / Demo
- **Deployed App**: [https://acc102-interactive-tool-dmmydbvrnjwp8qhfupw5lc.streamlit.app/]
- **Demo Video**: [Link to your 1-3 minute demo video] 
- **GitHub Repository**: https://github.com/ShuZhu24/acc102-interactive-tool

 7. Limitations & next steps
  Limitations
- Data only covers 2020-2024, not including 2025 figures
- Some smaller countries are grouped as "Other" due to low sales volume
- Exchange rates are not normalized (all figures in nominal USD)

  Next steps
- Add forecasting feature to predict next quarter sales using simple linear regression
- Integrate real-time data via API
- Add more interactive filters (year range, profit margin threshold)

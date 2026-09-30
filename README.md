Portfolio Analytics:
A Python and SQL-based portfolio analytics project designed to analyse the performance and composition of a simulated equity portfolio.

Project Overview:
The project analyses a simulated portfolio of nine Indian equities across multiple sectors. It combines Python-based financial analysis with SQL queries to evaluate portfolio performance, sector allocation, and individual stock returns.

Key Analysis:
- Total portfolio investment and current portfolio value
- Absolute and percentage portfolio returns
- Individual stock-level profit/loss
- Portfolio allocation across sectors
- Sector-wise investment and performance analysis
- Individual stock return visualisation

Tools & Technologies:
- Python
- Pandas
- SQL
- SQLite
- Matplotlib

Project Structure:
portfolio-analysis/
├── portfolio_allocation.png
├──stock_returns.png
├── portfolio_analysis.py
├── transactions.csv
├── prices.csv
├── requirements.txt
└── README.md

Methodology:
Transaction-level data is stored in CSV files and loaded into Python using Pandas. The data is then stored in a SQLite database, where SQL queries are used for sector-level aggregation and performance analysis.

Python is used to calculate portfolio-level metrics including current value, profit/loss, return percentage, and portfolio weights. Matplotlib is used to visualise portfolio allocation and individual stock returns.

Note:
The portfolio holdings, transactions, and prices used in this project are simulated for analytical and educational purposes and do not represent actual investments or investment recommendations.

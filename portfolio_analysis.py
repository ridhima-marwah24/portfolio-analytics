import pandas as pd
import sqlite3
import matplotlib.pyplot as plt

transactions = pd.read_csv("transactions.csv")
prices = pd.read_csv("prices.csv")

transactions["amount_invested"] = (transactions["quantity"] * transactions["price"])
portfolio = transactions.merge(
    prices[["ticker", "current_price"]],
    on="ticker",
    how="left")

portfolio["current_value"] = (portfolio["quantity"] * portfolio["current_price"])

portfolio["profit_loss"] = (
    portfolio["current_value"]
    - portfolio["amount_invested"])

portfolio["return_pct"] = (
    portfolio["profit_loss"]
    / portfolio["amount_invested"]) * 100

total_invested = portfolio["amount_invested"].sum()
total_current_value = portfolio["current_value"].sum()
total_profit_loss = portfolio["profit_loss"].sum()

total_return = (total_profit_loss / total_invested) * 100

print("\n--- PORTFOLIO SUMMARY ---")
print("Total Invested: ₹", round(total_invested, 2))
print("Current Value: ₹", round(total_current_value, 2))
print("Total P&L: ₹", round(total_profit_loss, 2))
print("Portfolio Return:", round(total_return, 2), "%")

conn = sqlite3.connect("portfolio.db")

transactions.to_sql(
    "transactions",
    conn,
    if_exists="replace",
    index=False)

prices.to_sql(
    "prices",
    conn,
    if_exists="replace",
    index=False)


query = """
SELECT
    sector,
    SUM(quantity * price) AS total_invested
FROM transactions
GROUP BY sector
ORDER BY total_invested DESC;
"""

sector_analysis = pd.read_sql_query(
    query,
    conn)

print("\n--- INVESTMENT BY SECTOR ---")
print(sector_analysis)

query = """
SELECT
    t.sector,
    SUM(t.quantity * t.price) AS invested,
    SUM(t.quantity * p.current_price) AS current_value,
    SUM(t.quantity * (p.current_price - t.price)) AS profit_loss
FROM transactions t
JOIN prices p
    ON t.ticker = p.ticker
GROUP BY t.sector
ORDER BY profit_loss DESC;
"""
sector_performance = pd.read_sql_query(query,conn)

sector_performance["return_pct"] = (
    sector_performance["profit_loss"]
    / sector_performance["invested"]) * 100

print("\n--- SECTOR PERFORMANCE ---")
print(sector_performance)

sector_allocation = (
    transactions.groupby("sector")["amount_invested"]
    .sum()
    .sort_values(ascending=False))

plt.figure(figsize=(8, 5))

sector_allocation.plot(kind="bar")

plt.title("Portfolio Allocation by Sector")
plt.xlabel("Sector")
plt.ylabel("Amount Invested (₹)")
plt.xticks(rotation=45)
plt.tight_layout()

plt.savefig("portfolio_allocation.png")

plt.close()

stock_returns = (
    portfolio[["company", "return_pct"]]
    .sort_values("return_pct", ascending=False))

plt.figure(figsize=(10, 5))

plt.bar(stock_returns["company"],
    stock_returns["return_pct"])

plt.title("Individual Stock Returns")
plt.xlabel("Company")
plt.ylabel("Return (%)")
plt.xticks(rotation=45)
plt.axhline(0, linewidth=0.8)
plt.tight_layout()

plt.savefig("stock_returns.png")

plt.close()
conn.close()

total_invested = portfolio["amount_invested"].sum()
total_current_value = portfolio["current_value"].sum()
total_profit_loss = portfolio["profit_loss"].sum()

total_return = (
    total_profit_loss / total_invested
) * 100

portfolio["portfolio_weight"] = (
    portfolio["amount_invested"] / total_invested) * 100

print("\nAnalysis completed successfully.")
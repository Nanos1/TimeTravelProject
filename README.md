# TimeTravelProject
Python-based stock market simulation using the "Huge Stock Market Dataset," enabling time-travel to 1960's Wall Street for strategic stock investment while adhering to space-time rules and experimenting with intraday trading.
Time-travel problem: travel back in time and make as much profit as you can on the New York Stock Exchange! [Dataset](https://www.kaggle.com/datasets/borismarjanovic/price-volume-data-for-all-us-stocks-etfs)


THE FOLLOWING ASSUMPTIONS ARE MADE FOR THE TRAVEL TIME IN THE STOCK EXCHANGE:

1. The total number of shares 𝑠 that we buy per day 𝑑 should not exceed 10% of its volume
share 𝑠 per day 𝑑.
2. Likewise, the total number of shares 𝑠 we sell per day 𝑑 should not exceed 10% of its volume
share 𝑠 per day 𝑑.
3. If before the opening of the day 𝑑 we have in our possession n ≥ 0 shares 𝑠, then during the day 𝑑 no
we can buy a total of more than 𝑛 + 1 shares 𝑠.

LEGAL MOVEMENTS:

• buy-open: buy at the opening price.
• sell-open: sold at the opening price.
• buy-close: buy at the closing price.
• sell-close: sold at the closing price

Title: Stock Market Time-Travel Simulation

Summary:

Have you ever pondered the possibilities of time-traveling to 1960s Wall Street, armed with historical stock market data? This project presents a Python simulation that enables you to delve into this intriguing scenario, offering the potential for substantial financial success.

Features:

• Harnesses a financial dataset to facilitate stock analysis and market simulation.
• Abides by the temporal regulations to preserve the space-time continuum, including constraints:
1. The ability to buy/sell up to 10% of a stock's volume in a single day.
2. The restriction on purchasing stocks, limited to N+1 if N stocks of the same company were held on the prior day.

• Permits specific intraday trading orders, encompassing (buy-open, sell-high), (buy-open, sell-close), (buy-high, sell-close), (sell-open, buy-low), (sell-open, buy-close), and (sell-high, buy-close).
• Presents a distinctive opportunity to experiment with historical stock market data, enabling the development of personalized investment strategies that may leave a lasting legacy for future generations.

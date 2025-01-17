from datetime import datetime

# List of stock tickers to include in the portfolio
TICKERS = ['AAPL', 'MSFT', 'GOOG']

# Date range for historical data
START_DATE = '2014-01-01'
END_DATE = datetime.today().strftime('%Y-%m-%d')  # Dynamic today's date

# Initial investment amount in dollars
INITIAL_INVESTMENT = 1000

# Number of Monte Carlo simulations to run
NUM_SIMULATIONS = 1000000

# Investment time horizon in days (e.g., 252 trading days in a year)
TIME_HORIZON = 252

# Risk-free rate for Sharpe Ratio calculation
RISK_FREE_RATE = 0.02

# Custom weights for each stock (should sum to 1)
# If None, equal weights are assumed unless optimization is used
WEIGHTS = None  # Example: [0.4, 0.3, 0.3]

# Optimization settings
OPTIMIZE = True  # Set to True to optimize the portfolio, False to use provided weights
BALANCED = False  # Set to True for a balanced portfolio, False to maximize Sharpe Ratio

# Print END_DATE to confirm it's today's date
print("End Date:", END_DATE)

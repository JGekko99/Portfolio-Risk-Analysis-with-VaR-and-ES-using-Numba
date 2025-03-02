import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import yfinance as yf
from datetime import datetime, timedelta
from numba import njit

# --- Optimized function using Numba ---
@njit
def compute_VaR_ES(returns, confidence_level):
    """
    Compute the Value at Risk (VaR) and Expected Shortfall (ES) using historical simulation.
    returns: 1D array of portfolio returns.
    confidence_level: Confidence level (e.g., 0.95 for 95%).
    Returns: VaR and ES.
    """
    # Sort the returns in ascending order
    sorted_returns = np.sort(returns)
    n = returns.shape[0]
    # Calculate the index corresponding to the lower percentile
    idx = int((1 - confidence_level) * n)
    if idx < 0:
        idx = 0
    if idx >= n:
        idx = n - 1
    VaR = sorted_returns[idx]
    
    # Calculate ES as the average of returns below the VaR
    es_sum = 0.0
    count = 0
    for x in sorted_returns:
        if x <= VaR:
            es_sum += x
            count += 1
    if count > 0:
        ES = es_sum / count
    else:
        ES = VaR
    return VaR, ES

def main():
    print("Starting portfolio risk analysis...\n")
    
    # --- Step 1: Configuration ---
    print("Step 1: Configuration")
    assets = ['AAPL', 'MSFT', 'GOOGL']
    weights = np.array([0.3, 0.4, 0.3])
    print("Assets:", assets)
    print("Weights:", weights)
    
    end_date = datetime.today()
    start_date = end_date - timedelta(days=365 * 3)
    print(f"Time period: {start_date.date()} to {end_date.date()}\n")
    input("Press Enter to continue to data download...")
    
    # --- Step 2: Download historical data ---
    print("\nStep 2: Downloading historical data")
    print("Downloading data for assets:", assets)
    # Use auto_adjust=True and select 'Close' since it is already adjusted
    data = yf.download(assets, start=start_date, end=end_date, auto_adjust=True)['Close']
    print("Data download complete.")
    print("Data shape:", data.shape)
    input("Press Enter to continue to data cleaning...")
    
    # --- Step 3: Data cleaning ---
    data.dropna(inplace=True)
    print("\nStep 3: Data Cleaning")
    print("Dropped rows with missing data. Data shape after cleaning:", data.shape)
    input("Press Enter to continue to return calculations...")
    
    # --- Step 4: Calculating returns ---
    print("\nStep 4: Calculating Daily Returns")
    returns = data.pct_change().dropna()
    print("Daily returns calculated. Data shape:", returns.shape)
    
    print("Computing portfolio returns using the defined weights...")
    portfolio_returns = returns.dot(weights).values  # convert to a 1D array for Numba
    print("Portfolio returns computed.")
    input("Press Enter to continue to risk calculations...")
    
    # --- Step 5: Calculating VaR and ES ---
    print("\nStep 5: Calculating Value at Risk (VaR) and Expected Shortfall (ES)")
    confidence_level = 0.95
    VaR, ES = compute_VaR_ES(portfolio_returns, confidence_level)
    print(f"Portfolio Value at Risk (95% confidence): {VaR:.4%}")
    print(f"Portfolio Expected Shortfall (95% confidence): {ES:.4%}")
    input("Press Enter to continue to visualization...")
    
    # --- Step 6: Visualizing the return distribution ---
    print("\nStep 6: Visualizing the return distribution")
    plt.figure(figsize=(10, 6))
    n, bins, patches = plt.hist(portfolio_returns, bins=50, alpha=0.7, color='skyblue', edgecolor='black')
    plt.axvline(VaR, color='red', linestyle='--', linewidth=2, label=f"VaR 95%: {VaR:.4%}")
    plt.title("Daily Return Distribution of the Portfolio")
    plt.xlabel("Daily Return")
    plt.ylabel("Frequency")
    plt.legend()
    plt.grid(True)
    plt.show()
    print("Histogram generated. Analysis complete.")

if __name__ == "__main__":
    main()


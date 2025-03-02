# Portfolio Risk Analysis with VaR and ES using Numba

This repository contains a Python script that performs portfolio risk analysis on selected assets using Value at Risk (VaR) and Expected Shortfall (ES) measures. The script uses Numba to optimize the risk calculations, downloads historical data from Yahoo Finance with `yfinance`, and visualizes the portfolio's return distribution.

## Features

- **Data Acquisition:** Downloads historical stock data for specified assets.
- **Data Cleaning:** Handles missing data by dropping incomplete rows.
- **Risk Metrics:** Calculates portfolio Value at Risk (VaR) and Expected Shortfall (ES) using a Numba-optimized function.
- **Visualization:** Plots a histogram of daily portfolio returns with a marked VaR threshold.
- **Interactivity:** Provides verbose output and interactive prompts to follow each step of the analysis.

## Requirements

- Python 3.x
- [NumPy](https://numpy.org/)
- [Pandas](https://pandas.pydata.org/)
- [Matplotlib](https://matplotlib.org/)
- [yfinance](https://github.com/ranaroussi/yfinance)
- [Numba](http://numba.pydata.org/)

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/yourusername/your-repo-name.git
   cd your-repo-name
2. **Create a virtual environment (optional but recommended):**

   ```bash
   python -m venv venv

Activate the virtual environment:

3. **Install the required packages:**
   You can install packages from the requirements.txt file:
   ```bash
   pip install -r requirements.txt

## Usage
Run the script using Python:

python var.py

1. The script will walk you through several steps:
2. Configuration of assets, weights, and time period.
3. Downloading and cleaning historical data.
4. Calculating daily returns and portfolio returns.
5. Computing VaR and Expected Shortfall.
6. Visualizing the return distribution.

Follow the on-screen prompts (press Enter to continue) to observe the progress at each step.

## Contributing

Contributions are welcome! If you have suggestions or improvements, please open an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

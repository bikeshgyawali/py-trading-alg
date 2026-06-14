# Python Trading Algorithm Backtester

A modular, configurable backtesting framework for evaluating trading strategies against historical stock market data. Built with flexibility in mind, this tool allows you to test different algorithmic trading approaches using real historical price data from Yahoo Finance.

## Features

- **Configurable Backtesting**: Define your trading parameters and time ranges via YAML configuration
- **Real Market Data**: Fetch historical stock data using Yahoo Finance API
- **Modular Strategy System**: Easily swap and test different trading strategies
- **Portfolio Management**: Track cash positions and share holdings throughout the backtest
- **Friction Modeling**: Account for real-world trading costs and transaction friction
- **Easy Setup**: Automated environment setup via bash script

## Current Strategies 
-Random Walk
-More soon to come!

## Prerequisites

- Python 3.8+
- pip (Python package installer)
- Virtual environment support

## Installation & Setup

### Quick Start (Recommended)

Use the provided bash script for automated setup:

```bash
./backtest.sh
```

This script will:
1. Create a Python virtual environment (`.venv` or `venv`)
2. Activate the environment
3. Install all dependencies from `requirements.txt`
4. Execute the backtest

### Manual Setup

If you prefer manual setup:

```bash
# Create and activate virtual environment
python3 -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the backtest
python main.py
```

For complete dependency information, see [requirements.txt](requirements.txt).

## Configuration

### Available Configuration Options 

The backtest is configured via `config.yaml`. Customize the following settings:


- **initial_portfolio**: Starting cash in your portfolio (default: $10,000)
- **initial_shares**: Initial shares to hold (default: 0)
- **ticker**: Stock ticker to backtest (e.g., "SPY", "AAPL", "TSLA")
- **start_date**: Beginning of backtest period
- **end_date**: End of backtest period

## Usage

### Run via Bash Script

```bash
./backtest.sh
```

### Run Directly with Python

```bash
python main.py
```

The backtest will:
1. Load configuration from `config.yaml`
2. Fetch historical data for the specified ticker and date range
3. Execute the trading strategy
4. Return the final portfolio value (cash + shares value)

## Project Structure

```
.
├── main.py                 # Entry point for backtesting
├── backtest.sh            # Automated setup and execution script
├── config.yaml            # Configuration file (user-editable)
├── requirements.txt       # Python dependencies
├── LICENSE                # MIT License
├── README.md              # This file
└── src/
    ├── __init__.py
    ├── config.py          # Configuration loader
    ├── data/
    │   ├── __init__.py
    │   └── data.py        # Data fetching utilities (Yahoo Finance API)
    ├── strategies/
    │   ├── __init__.py
    │   └── choose_random.py   # Example trading strategy
    └── utils/
        ├── __init__.py
        └── friction.py    # Transaction cost calculations
```

## Development

### Adding New Strategies

Create a new Python file in `src/strategies/` with your trading logic. Each strategy should accept the current price and portfolio state, then return updated portfolio and share counts.

### Project Modules

- **src/config.py**: Loads and validates configuration from YAML
- **src/data/data.py**: Interfaces with Yahoo Finance to retrieve historical price data
- **src/utils/friction.py**: Models trading costs and market friction
- **src/strategies/**: Contains different trading strategy implementations

## Example Output

```
15432.50
```

The output represents the total portfolio value at the end of the backtest period (cash + market value of holdings).

## License

This project is licensed under the MIT License - see [LICENSE](LICENSE) file for details.

---

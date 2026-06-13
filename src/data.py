import yfinance as yf
import pandas as pd

def get_spy_data():

    spy_data = yf.download("SPY", start="2025-01-01", end="2026-01-01")
    column_data = spy_data['Close'].squeeze().tolist()
    return column_data
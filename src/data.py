import yfinance as yf
import pandas as pd

def get_spy_data(ticker, start_date, end_date):

    spy_data = yf.download(ticker, start = start_date, end = end_date)
    column_data = spy_data['Close'].squeeze().tolist()

    return column_data
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def load_and_clean_data(filepath: str) -> pd.DataFrame:
    """Loads financial dataset and performs data cleaning."""
    df = pd.read_csv(filepath)
    df['Date'] = pd.to_datetime(df['Date'])
    df.set_index('Date', inplace=True)
    
    # Handle missing values by forward filling
    df.fillna(method='ffill', inplace=True)
    return df

def calculate_moving_averages(df: pd.DataFrame, window: int = 50) -> pd.DataFrame:
    """Calculates Simple Moving Average (SMA)."""
    df[f'SMA_{window}'] = df['Close'].rolling(window=window).mean()
    return df

def plot_closing_price_with_sma(df: pd.DataFrame):
    """Visualizes Closing Price alongside 50-day SMA."""
    plt.figure(figsize=(14, 7))
    plt.plot(df.index, df['Close'], label='Closing Price', color='blue', alpha=0.6)
    plt.plot(df.index, df['SMA_50'], label='50-Day SMA', color='red', alpha=0.9)
    plt.title('Stock Price Analysis: Close vs 50-Day SMA')
    plt.xlabel('Date')
    plt.ylabel('Price (USD)')
    plt.legend()
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    # Example usage:
    # df = load_and_clean_data('data/S&P500_historical.csv')
    # df = calculate_moving_averages(df, window=50)
    # plot_closing_price_with_sma(df)
    pass

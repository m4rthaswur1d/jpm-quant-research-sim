# Task 1 - Price Data Analysis
# JPMorgan Quantitative Research Job Simulation

# Goal:
# - Load commodity price data
# - Perform basic exploratory analysis
# - Generate summary statistics and plots

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

filepath = "task1_price_analysis/Nat_Gas.csv"
df = pd.read_csv("Nat_Gas.csv")

def plot_price_over_time(df, save_path=None):
    plt.plot(df["Dates"], df["Prices"])
    plt.title("Monthly Natural Gas Prices (2020–2024)")
    plt.xlabel("Date")
    plt.ylabel("Price")
    plt.grid(True)
    plt.tight_layout()

    if save_path:
        plt.savefig(save_path, dpi=200)
        plt.close()
    else:
        plt.show()

def compute_log_returns(df):
    log_returns = np.log(df["Prices"] / df["Prices"].shift(1))
    return log_returns

def rolling_mean_returns(df, k):
    rolling_sum = df["log_return"].rolling(k).sum()
    rolling_mean = rolling_sum / k
    return rolling_mean

def plot_rolling_mean(df, col_name="rm_12", save_path=None):
    plt.figure(figsize=(10, 5))
    plt.plot(df["Dates"], df["rm_12"])

    plt.title("Rolling Mean of Returns (12 Month)")
    plt.xlabel("Date")
    plt.ylabel("Mean Return")
    plt.grid(alpha=0.3)

    if save_path:
        plt.tight_layout()
        plt.savefig(save_path, dpi=150)

    plt.show()

def rolling_volatility(df, k):
    rolling_var = df["log_return"].rolling(k).var()
    rolling_vol = np.sqrt(rolling_var)
    return rolling_vol

def plot_rolling_volatility(df, col_name="vol_12", save_path=None):
    plt.figure(figsize=(10, 5))
    plt.plot(df["Dates"], df["vol_12"])

    plt.title("Rolling Volatility of Returns (12 Month)")
    plt.xlabel("Date")
    plt.ylabel("Volatility")
    plt.grid(alpha=0.3)

    if save_path:
        plt.tight_layout()
        plt.savefig(save_path, dpi=150)

    plt.show()










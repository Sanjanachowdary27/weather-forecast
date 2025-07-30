import pandas as pd # type: ignore
import sys
import os
from datetime import datetime
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from utils.data_loader import load_weather_data
from ml.predictor import predict_next_30_days

# Load once and cache to speed up search
past_data = load_weather_data()
future_data = predict_next_30_days()

def search_by_date(date_str):
    """
    Search weather by exact date.
    Works for past or next 30 days.
    """
    date = pd.to_datetime(date_str)

    match_past = past_data[past_data['Date'] == date]
    if not match_past.empty:
        return match_past

    match_future = future_data[future_data['Date'].dt.date == date.date()]
    if not match_future.empty:
        return match_future

    return pd.DataFrame()  # Empty if nothing found

def search_by_range(start_date_str, end_date_str):
    """
    Search weather between two dates (inclusive).
    Supports past and next 30 days.
    """
    start = pd.to_datetime(start_date_str)
    end = pd.to_datetime(end_date_str)

    past_range = past_data[(past_data['Date'] >= start) & (past_data['Date'] <= end)]
    future_range = future_data[(future_data['Date'] >= start) & (future_data['Date'] <= end)]

    return pd.concat([past_range, future_range], ignore_index=True)

# Test run
if __name__ == "__main__":
    print("Search by date:")
    print(search_by_date("2024-06-15"))

    print("\nSearch by range:")
    print(search_by_range("2024-06-10", "2025-07-10"))

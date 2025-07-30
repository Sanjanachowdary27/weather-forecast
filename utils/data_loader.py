import pandas as pd
import os

def load_weather_data():
    df1 = pd.read_csv(os.path.join("data", "weather_data_2024_full.csv"))
    df2 = pd.read_csv(os.path.join("data", "weather_data_2025.csv"))
    
    df = pd.concat([df1, df2], ignore_index=True)

    df.rename(columns={
        'Temperature(C)': 'Temperature',
        'Humidity(%)': 'Humidity',
        'Rainfall(mm)': 'Rainfall',
        'Wind_speed(km/h)': 'WindSpeed'
    }, inplace=True)

    df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
    df = df.dropna(subset=['Date'])

    df['Day'] = df['Date'].dt.day
    df['Month'] = df['Date'].dt.month
    df['Year'] = df['Date'].dt.year
    df['DayOfYear'] = df['Date'].dt.dayofyear

    return df

# Test directly
if __name__ == "__main__":
    df = load_weather_data()
    print(df.head())

import pandas as pd

# Load the CSV file
data=pd.read_csv('weather_data_2024_full.csv')

# Create DataFrame and convert 'Date' column to datetime
df = pd.DataFrame(data)
df['Date'] = pd.to_datetime(df['Date'])

# Filter to previous year(2024, assuming current yea is 2025)
prev_year = pd.Timestamp.today().year - 1
df_prev_year = df[df['Date'].dt.year == prev_year]

#Set the date as index for resampling
df_prev_year.set_index('Date', inplace=True)

# Resample to weekly data (average temperature per week)
weekly_data = df_prev_year.resample('W').mean().reset_index()

# show result
print(weekly_data.head())
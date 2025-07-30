import pandas as pd
import joblib
from datetime import datetime, timedelta
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

def predict_next_30_days():
    # Load models
    model_temp = joblib.load("ml/model_temp.pkl")
    model_hum = joblib.load("ml/model_hum.pkl")
    model_wind = joblib.load("ml/model_wind.pkl")
    model_rain = joblib.load("ml/model_rain.pkl")

    today = datetime.today()
    dates = [today + timedelta(days=i) for i in range(1, 31)]

    df_future = pd.DataFrame({
        'Date': dates,
        'Day': [d.day for d in dates],
        'Month': [d.month for d in dates],
        'DayOfYear': [d.timetuple().tm_yday for d in dates]
    })

    # Predict temperature, humidity, wind
    df_future['Temperature'] = model_temp.predict(df_future[['Day', 'Month', 'DayOfYear']])
    df_future['Humidity'] = model_hum.predict(df_future[['Day', 'Month', 'DayOfYear']])
    df_future['WindSpeed'] = model_wind.predict(df_future[['Day', 'Month', 'DayOfYear']])

    # Predict rainfall using other predictions
    df_future['Rainfall'] = model_rain.predict(df_future[['Temperature', 'Humidity', 'WindSpeed']])

    return df_future

# Test run
if __name__ == "__main__":
    df = predict_next_30_days()
    print(df.head())

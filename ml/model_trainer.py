import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import joblib
from sklearn.ensemble import RandomForestRegressor
from utils.data_loader import load_weather_data

def train_all_models():
    df = load_weather_data()

    features_base = ['Day', 'Month', 'DayOfYear']
    features_rain = ['Temperature', 'Humidity', 'WindSpeed']

    # === Trained model for Temperature
    X_temp = df[features_base]
    y_temp = df['Temperature']
    model_temp = RandomForestRegressor(n_estimators=100)
    model_temp.fit(X_temp, y_temp)
    joblib.dump(model_temp, 'ml/model_temp.pkl')

    # === Trained model for Humidity
    y_hum = df['Humidity']
    model_hum = RandomForestRegressor(n_estimators=100)
    model_hum.fit(X_temp, y_hum)
    joblib.dump(model_hum, 'ml/model_hum.pkl')

    # === Trained model for WindSpeed
    y_wind = df['WindSpeed']
    model_wind = RandomForestRegressor(n_estimators=100)
    model_wind.fit(X_temp, y_wind)
    joblib.dump(model_wind, 'ml/model_wind.pkl')

    # === Trained model for Rainfall using other outputs
    X_rain = df[features_rain]
    y_rain = df['Rainfall']
    model_rain = RandomForestRegressor(n_estimators=100)
    model_rain.fit(X_rain, y_rain)
    joblib.dump(model_rain, 'ml/model_rain.pkl')

    print(" All models trained and saved.")

if __name__ == "__main__":
    train_all_models()

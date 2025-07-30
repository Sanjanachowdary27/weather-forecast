import joblib
import pandas as pd
from sklearn.metrics import mean_absolute_error, r2_score
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from utils.data_loader import load_weather_data

def evaluate_rainfall_model():
    model = joblib.load("ml/model_rain.pkl")
    df = load_weather_data()

    features = ['Temperature', 'Humidity', 'WindSpeed']
    target = 'Rainfall'

    X = df[features]
    y_true = df[target]

    y_pred = model.predict(X)

    mae = mean_absolute_error(y_true, y_pred)
    r2 = r2_score(y_true, y_pred)

    print("Rainfall Prediction Accuracy:")
    print(f"Mean Absolute Error (MAE): {mae:.2f} mm")
    print(f"R² Score: {r2:.2f} (closer to 1 is better)")

if __name__ == "__main__":
    evaluate_rainfall_model()

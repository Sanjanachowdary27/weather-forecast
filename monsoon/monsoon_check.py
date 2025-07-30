import joblib
import numpy as np
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

# Loaded and trained rainfall model
model_rain = joblib.load("ml/model_rain.pkl")

def predict_monsoon(temp, humidity, windspeed):
    """
    Predicts rainfall and returns:
    - predicted rainfall (in mm)
    - monsoon probability (as percentage 0–100%)
    - monsoon status (based on threshold)
    """
    input_data = np.array([[temp, humidity, windspeed]])
    predicted_rainfall = model_rain.predict(input_data)[0]

    # Normalize rainfall to 0–100% chance (cap at 10mm for full confidence)
    capped_rainfall = min(max(predicted_rainfall, 0), 10)
    monsoon_percent = round((capped_rainfall / 10) * 100, 2)

    is_monsoon = predicted_rainfall >= 2.0 and monsoon_percent >= 50

    return round(predicted_rainfall, 2), monsoon_percent, is_monsoon

# Test it
if __name__ == "__main__":
    r, percent, monsoon = predict_monsoon(29.1, 91, 13)
    print(f" Rainfall: {r} mm | Chance of Rain: {percent}% | Monsoon: {'Yes' if monsoon else 'No'}")

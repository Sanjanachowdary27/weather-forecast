# 🌦️ Weather Forecast ML Dashboard

A **Streamlit-based dashboard** for machine learning-powered weather forecasting. Predicts temperature and rainfall for the next 30 days, supports weather data search (past, present, future), and provides monsoon prediction with confidence scores.

---

## 🔍 Features

- **30-Day Forecast:** ML-based weather predictions (Random Forest).
- **Weather Search:** Lookup by date or range (past & future).
- **Monsoon Predictor:** Input temperature, humidity, wind speed for rainfall and monsoon probability.
- **Model Evaluation:** R² Score and MAE metrics.
- **Modern UI:** Clean, responsive Streamlit interface.

---

## 📁 Project Structure

```
weather_dashboard_streamlit/
├── data/
│   └── weather_data_2025.csv
├── ml/
│   ├── model_trainer.py
│   ├── predictor.py
│   ├── evaluate_model.py
│   └── model_rain.pkl
├── monsoon/
│   └── monsoon_check.py
├── search/
│   └── search_feature.py
├── ui/
│   └── streamlit_ui.py
├── utils/
│   └── data_loader.py
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation & Usage

1. **Clone the repository**

   ```bash
   git clone https://github.com/yourusername/weather-dashboard-ml.git
   cd weather-dashboard-ml
   ```

2. **Create a virtual environment (optional)**

   ```bash
   python -m venv .venv
   .\.venv\Scripts\activate   # On Windows
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Run the app**
   ```bash
   streamlit run ui/streamlit_ui.py
   ```

---

## 🧠 ML Model

- **Algorithm:** Random Forest Regressor
- **Inputs:** Day, Month, DayOfYear
- **Outputs:** Temperature, Rainfall
- **Metrics:** R² ≈ 0.85, MAE ≈ 0.60 mm

---

## 💡 Notes

- Uses only the provided 2025 weather dataset.
- Monsoon probability is based on predicted rainfall.
- UI supports both forecasting and historical search.

---

## 📷 Screenshots

Add and embed screenshots for:

- Forecast Tab
- Search Feature
- Monsoon Prediction Output

---

## 📜 License

MIT License © 2025  
Developed for academic project use.

---

## 🙋‍♀️ Author

**Tummala Sanjana Chowdary**  
Machine Learning & Web App Developer

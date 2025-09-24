# 🏠 Household Energy Consumption Predictor

[![Streamlit App](https://img.shields.io/badge/Streamlit-Deployed-brightgreen?logo=streamlit)](https://household-energy-consumption-predictor-uxdfi8gryzh4azweemhrjt.streamlit.app/)

A **machine learning powered web application** that predicts household energy consumption (in Wh) using environmental and indoor conditions such as temperature, humidity, wind speed, and time features. The prediction model is built using a **Random Forest Regressor** trained on historical household energy data.

🔗 **Try the live app here:**
👉 [Household Energy Consumption Predictor](https://household-energy-consumption-predictor-uxdfi8gryzh4azweemhrjt.streamlit.app/)

---

## ✨ Features

* **Interactive Web App** built with [Streamlit](https://streamlit.io/).
* **Machine Learning Model** trained using scikit-learn’s RandomForestRegressor.
* **Gauge Meter Visualization** for quick insights into predicted energy consumption.
* **24-hour Energy Trend** to simulate usage patterns throughout the day.
* **Dynamic Input Panel** for customizing environmental & household conditions.

---

## 🚀 How It Works

1. User provides **input features** (temperature, humidity, pressure, wind speed, day, hour, etc.) through the sidebar.
2. The trained Random Forest model predicts `log_energy`.
3. The prediction is converted back into **watt-hours (Wh)** with the formula:

4. Results are displayed in:

   * A **Gauge Chart** showing consumption level.
   * A **Line Chart** showing the **24-hour trend**.

---

## 📊 Input Features

| Feature                         | Description                      |
| ------------------------------- | -------------------------------- |
| Outside Temperature (°C)        | Outdoor air temperature          |
| Outside Pressure (mm Hg)        | Atmospheric pressure             |
| Outside Humidity (%)            | Relative humidity outdoors       |
| Windspeed (m/s)                 | Wind speed                       |
| Visibility (km)                 | Visibility range                 |
| Dew Point (°C)                  | Dew point temperature            |
| Day of Month                    | Day of the calendar month (1–31) |
| Day of Week                     | 0 = Monday, … 6 = Sunday         |
| Month                           | Calendar month                   |
| Hour of Day                     | 0–23                             |
| Mean Indoor Temperature (°C)    | Average indoor temperature       |
| Max/Min Indoor Temperature (°C) | Max & min indoor temps           |
| Std Indoor Temperature          | Variation of indoor temperature  |
| Mean Indoor Humidity (%)        | Average indoor humidity          |
| Max/Min Indoor Humidity (%)     | Max & min humidity indoors       |
| Std Indoor Humidity             | Variation of indoor humidity     |

---

## ⚡ Tech Stack

* **Frontend / UI**: Streamlit
* **Backend / ML**: scikit-learn (RandomForestRegressor)
* **Visualization**: Plotly (gauge + trend plots)
* **Data Handling**: pandas, numpy
* **Deployment**: Streamlit Cloud

---

## 📂 Project Structure

```
📦 household-energy-consumption-predictor
 ┣ 📜 app.py                # Streamlit app
 ┣ 📜 rf_model.pkl          # Trained ML model
 ┣ 📜 requirements.txt      # Dependencies
 ┣ 📜 README.md             # Project documentation
```

---

## ⚙️ Installation & Local Run

Clone the repo and run locally:

```bash
git clone https://github.com/CodeRockstar24/household-energy-consumption-predictor.git
cd household-energy-consumption-predictor
pip install -r requirements.txt
streamlit run app.py
```

---

## ✅ Requirements

```
streamlit
numpy
pandas
plotly
scikit-learn
```

---

## 📸 Screenshots

### 🔹 Input Sidebar & Prediction

<img width="958" height="352" alt="image" src="https://github.com/user-attachments/assets/552ba93f-4d14-4620-abf9-cd12deafa8ad" />


### 🔹 Gauge Meter Visualization

<img width="718" height="364" alt="image" src="https://github.com/user-attachments/assets/ed8cffbb-ac40-4677-ba19-79c386057d06" />


### 🔹 24-Hour Predicted Trend

<img width="739" height="375" alt="image" src="https://github.com/user-attachments/assets/e41f052a-1d32-4f92-9bc5-23b9bc6b6a7d" />


---

## 🔮 Future Improvements

* Add **real-time data integration** (e.g., weather API).
* Support for **multiple households** comparison.
* Deploy with **Docker** for containerized scaling.
* Add **lag features** during feature engineering

---

## 🤝 Contributing

Pull requests are welcome! Please fork the repository and submit a PR with improvements.

---

## 📜 License

This project is licensed under the MIT License.



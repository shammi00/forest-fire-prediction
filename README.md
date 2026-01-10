# 🔥 Forest Fire Prediction using Machine Learning

This project predicts the **Forest Weather Index (FWI)** using machine learning techniques.
The goal is to estimate forest fire risk based on environmental conditions.

---

## 📌 Project Workflow

- Data cleaning and preprocessing performed in **Jupyter Notebooks**
- Feature engineering and scaling using **StandardScaler**
- Model training using **Ridge Regression**
- Model and scaler saved using **Pickle**
- Real-time predictions served through a **Flask web application**

---

## 🧠 Features Used

- Temperature
- Relative Humidity (RH)
- Wind Speed (Ws)
- Rain
- FFMC
- DMC
- ISI
- Classes
- Region

---

## 🛠️ Tech Stack

- Python
- Flask
- NumPy
- Scikit-learn
- HTML / CSS
- Jupyter Notebook

---

## ▶️ How to Run the Project

1. Clone the repository
2. Create and activate a virtual environment
3. Install dependencies:
   ```bash
   pip install -r requirements.txt


## 📂 Project Structure

```text
forest/
├── application.py        # Flask application entry point
├── templates/            # HTML templates
│   ├── home.html
│   └── model.html
├── static/               # Static files (CSS, JS)
│   └── css/
│       └── style.css
├── model/                # Saved ML models
│   ├── ridge.pkl
│   └── scaler.pkl
├── notebook/             # Jupyter notebooks
│   ├── model traning.ipynb
│   └── ridge lasso elasticnet.ipynb
├── requirements.txt      # Project dependencies
└── README.md             # Project documentation
```

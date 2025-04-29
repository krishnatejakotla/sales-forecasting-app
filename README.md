# 📈 Sales Forecasting Web Application

This project is a **Sales Forecasting Web App** developed using **Python**, **Streamlit**, and a **Machine Learning model** trained on sales data. It predicts expected sales based on user inputs like quantity ordered, price, month, year, and quarter.

---

## 🧩 Project Overview

- Built a machine learning model to predict sales revenue.
- Developed an interactive web application using **Streamlit**.
- Deployed the app using **Streamlit Cloud**.
- End-to-end flow from **Data Processing ➔ Model Training ➔ Model Saving ➔ Web App Development ➔ Deployment**.

---

## 🧠 Problem Statement

Retail businesses face challenges forecasting future sales based on seasonal and pricing variations. This project solves the problem by providing real-time sales predictions through a simple web interface.

---

## 🏗️ Project Architecture

```
Google Colab (Model Training) 
       ↓
Save Model (.pkl)
       ↓
Streamlit App Development (app.py)
       ↓
GitHub (Code Hosting)
       ↓
Streamlit Cloud (Deployment)
```

---

## 📚 Detailed Workflow

### 1. Machine Learning Model Development

- Dataset preprocessing
- Feature engineering (Month, Year, Quarter extracted from dates)
- Model training using **GradientBoostingRegressor**
- Saved trained model as `sales_forecasting_model.pkl` using `joblib`

---

### 2. Web App Development (Streamlit)

- Input fields: 
  - Quantity Ordered
  - Price Each
  - Month
  - Year
- Backend:
  - Load the `.pkl` model
  - Predict and display sales revenue instantly

---

### 3. Deployment (Streamlit Cloud)

- Uploaded `app.py` and `sales_forecasting_model.pkl` to GitHub
- Linked the repository to Streamlit Cloud
- App now live and accessible to everyone

---

## 🛠️ Tech Stack

- **Python 3.10**
- **Libraries**:
  - pandas
  - numpy
  - scikit-learn
  - xgboost
  - streamlit
  - joblib
- **Tools**:
  - Google Colab (for model training)
  - GitHub (for code hosting)
  - Streamlit Cloud (for deployment)

---

## ⚙️ Installation & Running Locally

1. Clone the repository:

```
git clone https://github.com/krishnatejakotla/sales-forecasting-app.git
```

2. Move into the project directory:

```
cd sales-forecasting-app
```

3. Install dependencies:

```
pip install pandas numpy scikit-learn xgboost streamlit joblib
```

4. Run the Streamlit application:

```
streamlit run app.py
```

---

## 🌐 Live Demo

✅ **App is live at:**  
👉 [Sales Forecasting App](https://sales-forecasting-app-yetjfwnowzdaup4nrjhtef.streamlit.app/)

---

## 🛠️ Requirements

If you want to replicate:

```
pip install pandas numpy scikit-learn xgboost streamlit joblib
```

---

## 🎯 Use Cases

- Retail Sales Predictions
- Inventory Management Optimization
- Financial Forecasting for Businesses
- Price-Volume Sensitivity Analysis

---

## 🔥 Challenges Faced

- Initially saved model wrongly (`.json` instead of `.pkl`)
- Module import errors (`sklearn`, `xgboost`) while deploying
- PATH issues for `streamlit` command locally
- Streamlit Cloud GitHub linking and file path corrections

✅ **All challenges were solved with careful debugging, re-saving the model, and correct environment setup.**

---

## 🚀 Future Improvements

- Add user authentication
- Add feature for multiple product category predictions
- Train a more advanced model (LightGBM or CatBoost)
- Visualize prediction trends dynamically

---

## 🙌 Acknowledgements

- Thanks to Streamlit for providing a free deployment platform.
- Special thanks to Google Colab for easy model training.
- Inspired by real-world retail business needs.

---

# ✨ Thank You for Visiting!







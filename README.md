# 🏎️ Car Price Prediction using Gradient Boosting

---

## 🧩 Overview
This project predicts the **price of a car** based on its physical and engine attributes such as wheelbase, car length, engine size, horsepower, etc.  
The model uses **Gradient Boosting Regression**, a powerful ensemble learning technique known for its high accuracy and ability to handle non-linear data.  
A **Streamlit web application** is built on top of the model to make predictions interactively.

---

## 💡 Problem Statement
Determining the right price for a car is complex and depends on multiple parameters like size, weight, engine performance, and build specifications.  
The goal of this project is to build a **data-driven model** that can accurately predict car prices based on these features, helping both manufacturers and customers make informed pricing decisions.

---

## 🎯 Objective
- Develop a regression model capable of predicting car prices with minimal error.  
- Implement a simple and interactive **Streamlit web app** for real-time predictions.  
- Use the **best-performing model (Gradient Boosting)** for deployment.

---

## 📊 Dataset
- **Source:** [UCI Machine Learning Repository – Automobile Dataset](https://archive.ics.uci.edu/dataset/10/automobile)
- **Target Variable:** `price`
- **Features Used:**
  - `wheelbase`
  - `carlength`
  - `carwidth`
  - `carheight`
  - `curbweight`
  - `enginesize`
  - `boreratio`
  - `stroke`
  - `compressionratio`
  - `horsepower`

---

## 🧰 Tools & Libraries
- **Programming Language:** Python 🐍  
- **Libraries:**
  - `pandas` – Data handling and preprocessing  
  - `numpy` – Numerical computations  
  - `scikit-learn` – Model training and evaluation  
  - `streamlit` – Web app deployment  
  - `pickle` – Model serialization  

---

## 🧠 Model Architecture
- **Model Used:** Gradient Boosting Regressor  
- **Base Learner:** Decision Tree Regressor  
- **Ensemble Strategy:** Boosting weak learners sequentially to minimize residual errors.  

Training involved evaluating multiple models (`Linear Regression`, `Decision Tree`, `Random Forest`, `Gradient Boosting`) and selecting **Gradient Boosting** as the best performer.

---

## ⚙️ Data Preprocessing
1. Loaded and cleaned raw dataset (handled missing values, categorical encoding).  
2. Selected relevant numeric features influencing price.  
3. Performed feature scaling where necessary.  
4. Split data into **train-test sets** (80–20 ratio).  
5. Serialized the final model using `pickle` as `best_pickle_car_pred.pkl`.

---

## 📏 Evaluation Metrics
- **Mean Squared Error (MSE)**  
- **Root Mean Squared Error (RMSE)**  
- **R² Score**

| Model | R² Score | RMSE |
|--------|----------|------|
| Linear Regression | 0.81 | 2350 |
| Decision Tree | 0.88 | 1800 |
| Random Forest | 0.92 | 1550 |
| **Gradient Boosting** | **0.94** | **1400** |

---

## 💻 Results
- The **Gradient Boosting model** achieved the highest accuracy with an R² score of **0.94**.  
- The deployed Streamlit app provides **instant predictions** with an intuitive UI.  

---

## 🌐 Streamlit App
**File Structure:**

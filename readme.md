# Shopping Behavior Prediction App

This is a **Streamlit web application** that predicts the number of previous purchases for a customer based on their **Age** and **Customer ID** using **Linear Regression**.

The app loads and preprocesses the dataset, normalizes the features, trains a Linear Regression model, and provides an interactive interface for predictions.

---

## Features

* Loads dataset from a CSV file
* Drops duplicate rows
* Fills missing categorical values
* Normalizes numeric features (Age and Customer ID)
* Linear Regression model training
* Interactive Streamlit UI with a **Predict button**
* Shows predicted number of previous purchases

---

## Requirements

* Python 3.x
* Libraries:

  * pandas
  * scikit-learn
  * streamlit

Install dependencies with:

```bash
pip install pandas scikit-learn streamlit
```

---

## How to Run

1. Clone or download this repository.
2. Make sure the dataset `shopping_behavior_updated.csv` is in the same folder as `app.py`.
3. Open terminal in the project folder and run:

```bash
streamlit run app.py
```

4. The app will open in your browser. Enter **Age** and **Customer ID** and click **Predict** to see the predicted previous purchases.

---

## Example

![Example Screenshot](screenshot.png)

---

## Notes

* This app currently uses only **Age** and **Customer ID** as input features.
* The Linear Regression model is trained on normalized feature values.
* You can extend the app by adding categorical features like **Gender, Payment Method, Item Purchased** for better predictions.

import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
import streamlit as st

# Load Dataset
df = pd.read_csv("C:\\Users\\SAKHAWAT\\Downloads\\shopping behaviour\\archive\\shopping_behavior_updated.csv")

# Preprocessing
df_cleaned = df.drop_duplicates()
df_cleaned['Gender'].fillna(df_cleaned['Gender'].mode()[0], inplace=True)

# Normalize only feature columns (exclude target)
numeric_features = ['Age', 'Customer ID']  
scaler = StandardScaler()
df_cleaned[numeric_features] = scaler.fit_transform(df_cleaned[numeric_features])

# Train Linear Regression
X = df_cleaned[numeric_features]
y = df_cleaned['Previous Purchases']
lr_model = LinearRegression()
lr_model.fit(X, y)

# Streamlit UI
st.title("Shopping Behavior Prediction App")
st.write("Predict Previous Purchases based on Age and Customer ID")

age_input = st.number_input("Enter Age", min_value=1, max_value=100, value=25)
customer_id_input = st.number_input("Enter Customer ID", min_value=1, value=1)

# Add Predict button
if st.button("Predict"):
    # Normalize user input
    input_df = pd.DataFrame({'Age': [age_input], 'Customer ID': [customer_id_input]})
    input_df[numeric_features] = scaler.transform(input_df[numeric_features])

    # Predict
    prediction = lr_model.predict(input_df)
    st.success(f"Predicted Previous Purchases: {prediction[0]:.2f}")

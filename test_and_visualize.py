import pandas as pd
import joblib
import tensorflow as tf
from tensorflow.keras.models import load_model
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

print("--- Starting Automated Model Testing and Visualization ---")

# --- 1. Load Models, Scaler, and Columns ---
try:
    print("Loading models and preprocessing objects...")
    xgb_model = joblib.load('xgb_model.pkl')
    fnn_model = load_model('fnn_model.h5')
    scaler = joblib.load('scaler.pkl')
    model_columns = joblib.load('model_columns.pkl')
    print("Successfully loaded all artifacts.")
except Exception as e:
    print(f"Error loading files: {e}")
    exit()

# --- 2. Load and Prepare the Original Dataset ---
try:
    print("Loading the original dataset...")
    
    # THIS LINE IS NOW CORRECTED TO READ YOUR EXACT EXCEL FILENAME
    df = pd.read_excel('synthetic_electricity_dataset.csv.xlsx')
    
    # Basic cleaning from your training script
    if df.columns[0].startswith('Unnamed'):
        df = df.drop(df.columns[0], axis=1)
    df.columns = df.columns.str.replace(' ', '_')
    
    print("Dataset loaded and cleaned.")
except Exception as e:
    print(f"Error loading dataset: {e}")
    exit()

# --- 3. Run Predictions on the Entire Dataset ---
print("Running predictions on the full dataset...")

# Separate features (X) and the actual target (y)
X = df.drop(columns=['Monthly_Bill_INR'])
y_actual = df['Monthly_Bill_INR']

# Preprocess the features exactly as you did for training
X_processed = pd.get_dummies(X, columns=['City', 'Weather_Condition', 'Appliance_Name'])
X_final = X_processed.reindex(columns=model_columns, fill_value=0)

# Get predictions from both models
xgb_predictions = xgb_model.predict(X_final)
X_scaled = scaler.transform(X_final)
fnn_predictions = fnn_model.predict(X_scaled).flatten() # Use .flatten() to make it a 1D array

# --- 4. Create a Results DataFrame ---
print("Compiling results...")
results_df = df.copy()
results_df['XGBoost_Prediction'] = xgb_predictions
results_df['FNN_Prediction'] = fnn_predictions
results_df['XGBoost_Error'] = results_df['XGBoost_Prediction'] - results_df['Monthly_Bill_INR']
results_df['FNN_Error'] = results_df['FNN_Prediction'] - results_df['Monthly_Bill_INR']

# Save the detailed results to a new CSV file
results_df.to_csv('predictions_and_errors.csv', index=False)
print("Results saved to 'predictions_and_errors.csv'.")


# --- 5. Generate and Save Visualizations for Journal ---
print("Generating visualizations...")
sns.set_style("whitegrid")

# --- Visualization 1: Actual vs. Predicted Scatter Plot ---
plt.figure(figsize=(10, 10))
plt.scatter(y_actual, xgb_predictions, alpha=0.5, label='XGBoost')
plt.scatter(y_actual, fnn_predictions, alpha=0.5, label='FNN')
plt.plot([y_actual.min(), y_actual.max()], [y_actual.min(), y_actual.max()], 'k--', lw=2, label='Perfect Prediction')
plt.xlabel("Actual Monthly Bill (INR)")
plt.ylabel("Predicted Monthly Bill (INR)")
plt.title("Actual vs. Predicted Bill Amount")
plt.legend()
plt.savefig('actual_vs_predicted.png', dpi=300)
print("Saved 'actual_vs_predicted.png'")

# --- Visualization 2: Residuals Distribution Plot ---
plt.figure(figsize=(12, 6))
sns.histplot(results_df['XGBoost_Error'], color='skyblue', kde=True, label='XGBoost Error', bins=50)
sns.histplot(results_df['FNN_Error'], color='red', kde=True, label='FNN Error', bins=50)
plt.xlabel("Prediction Error (Residuals) in INR")
plt.ylabel("Frequency")
plt.title("Distribution of Prediction Errors")
plt.legend()
plt.savefig('error_distribution.png', dpi=300)
print("Saved 'error_distribution.png'")

# --- Visualization 3: Residuals vs. Predicted Plot (for checking bias) ---
plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
plt.scatter(xgb_predictions, results_df['XGBoost_Error'], alpha=0.5)
plt.axhline(y=0, color='r', linestyle='--')
plt.xlabel("Predicted Values (XGBoost)")
plt.ylabel("Residuals")
plt.title("XGBoost Residual Plot")

plt.subplot(1, 2, 2)
plt.scatter(fnn_predictions, results_df['FNN_Error'], alpha=0.5)
plt.axhline(y=0, color='r', linestyle='--')
plt.xlabel("Predicted Values (FNN)")
plt.ylabel("Residuals")
plt.title("FNN Residual Plot")

plt.tight_layout()
plt.savefig('residual_plots.png', dpi=300)
print("Saved 'residual_plots.png'")

print("\n--- Automation Complete ---")
print("You can find the new CSV and plot images in your project folder.")
#  Blood Sugar Level Predictor using Linear Regression

This project uses a simple **Linear Regression** model to predict a person's blood sugar level based on their:

- Age
- Body Mass Index (BMI)
- Weekly Exercise Hours
- Daily Carbohydrate Intake

##  File Structure

- `file.py` – Main Python script that:
  - Creates a dataset
  - Trains a linear regression model
  - Takes user input for a new patient
  - Predicts and displays the estimated blood sugar level

##  How It Works

1. A sample dataset is created using `pandas`.
2. The data is split into features (X) and target (y).
3. A linear regression model is trained using `scikit-learn`.
4. The user is prompted to enter new patient data.
5. The model predicts and prints the expected blood sugar level.

## Run the Code

Make sure you have the required libraries:
```bash
pip install pandas scikit-learn

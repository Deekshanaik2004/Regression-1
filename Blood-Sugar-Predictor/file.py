# Step 1: Import Libraries
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

# Step 2: Create Sample Dataset
data = {
    'Age': [25, 35, 45, 30, 40, 50],
    'BMI': [22.0, 28.5, 31.0, 26.0, 29.0, 33.0],
    'ExerciseHours': [5, 2, 1, 4, 2, 1],
    'CarbIntake': [200, 300, 350, 250, 330, 400],
    'BloodSugar': [90, 110, 140, 100, 130, 160]  # Target (mg/dL)
}
df = pd.DataFrame(data)

# Step 3: Feature and Target Split
X = df.drop('BloodSugar', axis=1)
y = df['BloodSugar']

# Step 4: Train-test Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Step 5: Train the Model
model = LinearRegression()
model.fit(X_train, y_train)

# Step 6: Evaluate
y_pred = model.predict(X_test)
print("Mean Squared Error:", mean_squared_error(y_test, y_pred))

# Step 7: Take Input from Programmer
print("\n--- Enter New Patient Details ---")
age = float(input("Enter Age: "))
bmi = float(input("Enter BMI: "))
exercise = float(input("Enter Exercise Hours per Week: "))
carbs = float(input("Enter Daily Carb Intake (grams): "))

# Step 8: Predict Blood Sugar
new_patient = [[age, bmi, exercise, carbs]]
predicted_bs = model.predict(new_patient)
print("\nPredicted Blood Sugar Level (mg/dL):", round(predicted_bs[0], 2))

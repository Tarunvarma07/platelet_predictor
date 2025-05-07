import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, r2_score
from sklearn.preprocessing import LabelEncoder
import joblib
import numpy as np

# Load and preprocess the data
df = pd.read_csv('C:\\Users\\tarun\\OneDrive\\Desktop\\platelet_data.csv')

# Fill missing values
numeric_columns = df.select_dtypes(include=['float64', 'int64']).columns
df[numeric_columns] = df[numeric_columns].fillna(df[numeric_columns].mean())
categorical_columns = df.select_dtypes(include=['object']).columns
for col in categorical_columns:
    df[col] = df[col].fillna(df[col].mode()[0])

# Convert fever_date to the number of days since today
today = pd.to_datetime('today')
df['fever_date'] = (today - pd.to_datetime(df['fever_date'])).dt.days

# Encode categorical columns
label_encoder_type_of_fever = LabelEncoder()
df['type_of_fever'] = label_encoder_type_of_fever.fit_transform(df['type_of_fever'])

label_encoder_hydration_level = LabelEncoder()
df['hydration_level'] = label_encoder_hydration_level.fit_transform(df['hydration_level'])

label_encoder_location = LabelEncoder()
df['location'] = label_encoder_location.fit_transform(df['location'])

# Save label encoders for later use
joblib.dump(label_encoder_type_of_fever, 'label_encoder_type_of_fever.pkl')
joblib.dump(label_encoder_hydration_level, 'label_encoder_hydration_level.pkl')
joblib.dump(label_encoder_location, 'label_encoder_location.pkl')

# Split into features and target
X = df.drop(columns=['platelet_next_day'])
y = df['platelet_next_day']

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Model training
model = RandomForestRegressor(random_state=42)
model.fit(X_train, y_train)

# Model evaluation
y_pred = model.predict(X_test)
mae = mean_absolute_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)
print(f"Model Evaluation:\nMean Absolute Error: {mae}\nR² Score: {r2}\n")

# Save model
joblib.dump(model, 'model.pkl')
print("Model saved as model.pkl")


from flask import Flask, request, render_template, jsonify
import joblib
import pandas as pd
import numpy as np
from datetime import datetime

app = Flask(__name__)

# Load model and encoders
model = joblib.load('model.pkl')
label_encoder_type_of_fever = joblib.load('label_encoder_type_of_fever.pkl')
label_encoder_hydration_level = joblib.load('label_encoder_hydration_level.pkl')
label_encoder_location = joblib.load('label_encoder_location.pkl')

# Age group logic
def get_age_group(age):
    if age <= 12:
        return 'child'
    elif 13 <= age <= 19:
        return 'teen'
    elif 20 <= age <= 59:
        return 'adult'
    else:
        return 'elderly'

# Health recommendation logic
def health_recommendation(platelet_count, can_eat_raw_food=True, age_group='adult'):
    advice = ""
    foods = ""
    fluids = ""

    if platelet_count < 50000:
        advice = "Critical: Immediate medical attention required."
        foods = "Consult a healthcare professional for appropriate treatment."
        fluids = "Drink electrolyte solutions or oral rehydration salts (ORS)."
    elif platelet_count < 100000:
        advice = "Low platelet count: Increase fluid intake and rest."
        foods = "Include iron-rich foods like cooked spinach, lentils, and lean meats."
        fluids = "Drink plenty of water, herbal teas, and fresh fruit juices like orange or pomegranate."
    elif platelet_count < 150000:
        advice = "Moderate platelet count: Continue monitoring and stay hydrated."
        foods = "Consume vitamin-rich foods such as citrus fruits, leafy greens, and cooked carrots."
        fluids = "Stay hydrated with water, herbal teas, and fresh juices."
    else:
        advice = "Normal platelet count: Keep monitoring and maintain a healthy diet."
        foods = "Maintain a balanced diet with a variety of fruits, vegetables, lean proteins, and whole grains."
        fluids = "Drink water, coconut water, and fresh fruit juices to maintain hydration."

    if not can_eat_raw_food:
        foods += " Since raw foods are not recommended, consume cooked vegetables like spinach, carrots, and broccoli."

    if age_group == 'child':
        foods += " For children, focus on soft, easily digestible foods like bananas, boiled carrots, and scrambled eggs."
        fluids += " Ensure they drink enough water, fresh fruit juices, and oral rehydration drinks if needed."
    elif age_group == 'teen':
        foods += " For teens, encourage a variety of cooked vegetables, lean proteins, and vitamin-packed fruits like oranges and apples."
        fluids += " Smoothies are a fun way to incorporate these nutrients, along with water and herbal teas."
    elif age_group == 'elderly':
        foods += " For the elderly, focus on cooked vegetables, easy-to-digest fruits, and lean proteins. Avoid raw foods due to infection risk."
        fluids += " Hydration is crucial, so encourage drinking warm broths, herbal teas, and fresh fruit juices."

    return f"{advice} Suggested foods: {foods} Suggested fluids: {fluids}"

# Encode categorical inputs
def encode_new_data(new_data):
    if new_data['type_of_fever'] not in label_encoder_type_of_fever.classes_:
        label_encoder_type_of_fever.classes_ = np.append(label_encoder_type_of_fever.classes_, new_data['type_of_fever'])
    new_data['type_of_fever'] = label_encoder_type_of_fever.transform([new_data['type_of_fever']])[0]

    if new_data['hydration_level'] not in label_encoder_hydration_level.classes_:
        label_encoder_hydration_level.classes_ = np.append(label_encoder_hydration_level.classes_, new_data['hydration_level'])
    new_data['hydration_level'] = label_encoder_hydration_level.transform([new_data['hydration_level']])[0]

    if new_data['location'] not in label_encoder_location.classes_:
        label_encoder_location.classes_ = np.append(label_encoder_location.classes_, new_data['location'])
    new_data['location'] = label_encoder_location.transform([new_data['location']])[0]

    return new_data

@app.route('/', methods=['GET', 'POST'])
def index():
    prediction = None
    recommendation = None
    error = None

    if request.method == 'POST':
        try:
            age = int(request.form['age'])
            age_group = get_age_group(age)

            # Convert date to number of days since fever started
            fever_date = datetime.strptime(request.form['fever_date'], '%Y-%m-%d')
            days_since_fever = (datetime.today() - fever_date).days

            data = {
                'patient_age': age,
                'fever_date': days_since_fever,  # ✅ Now numeric!
                'type_of_fever': request.form['type_of_fever'],
                'headache': 1 if request.form.get('headache') else 0,
                'joint_pain': 1 if request.form.get('joint_pain') else 0,
                'nausea': 1 if request.form.get('nausea') else 0,
                'rash': 1 if request.form.get('rash') else 0,
                'hydration_level': request.form['hydration_level'],
                'existing_conditions': int(request.form['existing_conditions']),
                'weight': float(request.form['weight']),
                'location': request.form['location'],
                'platelet_day1': int(request.form['platelet_day1']),
                'platelet_day2': int(request.form['platelet_day2'])
            }

            # Encode categorical data
            data = encode_new_data(data)

            input_df = pd.DataFrame([data])
            prediction = int(model.predict(input_df)[0])

            # Recommendation
            can_eat_raw = request.form['raw_food'] == 'yes'
            recommendation = health_recommendation(prediction, can_eat_raw, age_group)

        except Exception as e:
            error = str(e)

    return render_template('index.html', prediction=prediction, recommendation=recommendation, error=error)

if __name__ == '__main__':
    app.run(debug=True)


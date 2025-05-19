# 🩸 Platelet Prediction System & Health Recommender 💉

## 💡 Inspiration

This project was born out of a personal experience. My sister suddenly fell ill with dengue fever, and we watched her platelet count decrease day by day. The anxiety of not knowing what would happen next, combined with the constant need for testing and monitoring, made me realize how critical timely platelet prediction could be.

That experience inspired me to create a system that could help patients, families, and healthcare providers anticipate changes in platelet levels using machine learning. With just basic input data, this system can provide early warnings, reduce stress, and potentially save lives — especially in areas where medical resources are limited.

This is more than just a project; it's a step toward using AI for compassionate, real-world impact.


Predict platelet counts and get health recommendations based on patient data using machine learning!  
This project uses a **RandomForestRegressor** model served through a **Flask** web app to provide real-time predictions and personalized health advice.

---

## 🧠 Features

| Input Attribute           | Description                |
| ------------------------- | --------------------------|
| Patient Age               | Age of the patient         |
| Fever Date                | Date when fever started    |
| Type of Fever             | Fever classification       |
| Headache                  | Presence of headache       |
| Joint Pain                | Presence of joint pain     |
| Nausea                   | Presence of nausea          |
| Rash                     | Presence of rash            |
| Hydration Level           | Level of hydration         |
| Existing Conditions       | Other medical conditions   |
| Weight                   | Patient's weight           |
| Location                 | Patient's location          |

> Enter accurate health details for best prediction results.

---

## 🛠 Tech Stack

* 🐍 Python 3.8+  
* 🔥 Flask – Web framework for serving the model  
* 🌲 scikit-learn – RandomForestRegressor for prediction  
* 🖥️ HTML/CSS – Frontend user interface  
* 📊 pandas, numpy – Data processing  

---


Fill in the patient health details form and submit to get platelet count prediction and health recommendations.

📌 **To stop the server**, press `Ctrl+C` in the terminal.

---

## 📂 Project Structure

```
Platelet-Prediction-System/
│
├─ app.py                 # Flask application script
├─ model.pkl              # Trained RandomForestRegressor model
├─ templates/
│   └─ index.html         # HTML form template
├─ static/
│   └─ styles.css         # CSS styles (optional)
├─ requirements.txt       # Python dependencies
└─ README.md              # This file
```

---

## 📸 How It Works (Architecture)

```plaintext
 User Input Data
      ↓
 Flask Server Receives Form
      ↓
 Data Preprocessing & Feature Extraction
      ↓
 RandomForestRegressor Model Predicts Platelet Count
      ↓
 Health Recommendations Generated
      ↓
 Flask Sends Prediction & Advice to User Interface
```

---

## 🥮 Tips for Best Accuracy

* Provide **accurate and complete** input data.
* Maintain consistent environment when running the app.
* This model is for educational purposes only; always consult healthcare professionals for medical advice.
---

## ⚠️ Disclaimer

This tool is designed for educational purposes and is not a substitute for professional medical diagnosis or treatment.

---

## 📄 License

Licensed under the [MIT License](LICENSE).

---

## 🤝 Acknowledgements

* [scikit-learn](https://scikit-learn.org/stable/)
* [Flask](https://flask.palletsprojects.com/)
* [pandas](https://pandas.pydata.org/)
* [NumPy](https://numpy.org/)

---

### 🔗 Author

**Venkata Sai Tarun Varma Chintha**
📍 Andhra Pradesh, India
👨‍💻 [GitHub](https://github.com/Tarunvarma07) Email:varmachintha30@gmail.com

```

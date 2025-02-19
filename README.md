# 🩺 Diabetes Risk Prediction System

This is a **Streamlit web application** that predicts the risk of diabetes based on user input and stores patient data in a SQLite database.

## 🚀 Features

- Accepts patient details such as **Glucose Level, BMI, Insulin, Age**, etc.
- Uses a **trained Random Forest model** to predict diabetes risk.
- Stores patient records with **timestamps** in a SQLite database.
- Displays stored patient data in a table.
- **Attractive UI** with a dark theme and styled buttons.

## 🛠 Installation

1. **Clone the repository**:
   ```sh
   git clone https://github.com/yourusername/diabetes-prediction.git
   cd diabetes-prediction
python -m venv env
source env/bin/activate   # On Mac/Linux
env\Scripts\activate      # On Windows
pip install -r requirements.txt
streamlit run app.py
diabetes-prediction/
│── app.py                  # Main Streamlit application
│── diabetes_model.pkl      # Pre-trained Random Forest model
│── clinic_data.db          # SQLite database (generated after running)
│── requirements.txt        # Required dependencies
│── README.md               # Project documentation

🖥 Technologies Used
Python
Streamlit (for the web app)
Scikit-Learn (for ML model)
SQLite (for storing patient data)
Pandas & NumPy (for data handling)

📌 Notes
The "Predict Diabetes Risk" button is green for visibility.
The app supports a dark theme for better readability.
Make sure diabetes_model.pkl is present in the project directory.
📜 License
This project is open-source under the MIT License.

👩‍💻 Developed by Reshma R B
📧 Contact: your.reshmarb8547@gmail.com

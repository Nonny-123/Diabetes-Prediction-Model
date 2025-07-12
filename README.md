Diabetes Prediction Model API 🩺✨
A robust and high-performance API for predicting the likelihood of diabetes using a custom-trained Random Forest Classifier. Deployable, validated, and fully documented.

📋 Table of Contents
🌟 Overview

✨ Features

🛠️ Technologies Used

🚀 Getting Started

Prerequisites

1. Clone the Repository

2. Create a Virtual Environment (Recommended)

3. Install Dependencies

4. Place Your Trained Model

5. Run the API

🧪 How to Test the API

1. FastAPI Interactive Docs (Swagger UI)

2. Using curl (Command Line)

🔗 API Endpoints

GET /

POST /diabetes_prediction

📂 Project Structure

📈 Model Training and Evaluation

🤝 Contributing

📄 License

🌟 Overview
This project delivers a powerful and user-friendly API designed to predict the presence of diabetes based on a set of key health indicators. At its core, it leverages a custom-trained RandomForestClassifier model, exposed via a blazing-fast FastAPI interface. With Pydantic ensuring strict data validation and automatic interactive documentation, this API is engineered for reliability, developer-friendliness, and seamless integration into various applications.

Whether you're building a health application, a research tool, or simply exploring machine learning deployments, this API offers a solid and transparent foundation for diabetes risk assessment.

✨ Features
Intelligent Predictions: Utilizes a custom-trained RandomForestClassifier model to provide accurate and informed diabetes predictions.

High-Performance API: Built with FastAPI, renowned for its incredible speed and efficiency, making it ideal for demanding production environments.

Strict Data Validation: Employs Pydantic models to meticulously ensure all incoming request data adheres to expected types and formats, drastically minimizing errors and enhancing data integrity.

Clear Input Definitions: Uses Python's Literal types for categorical features (like gender, smoking_history_cleaned), providing explicit and understandable valid options.

Comprehensive Error Handling: Gracefully manages invalid inputs and potential server-side issues, consistently returning descriptive JSON error messages for easier debugging.

Interactive Documentation (Swagger UI): Enjoy automatically generated API documentation at /docs! This interactive interface allows for effortless exploration, understanding, and direct testing of all endpoints right from your web browser.

Health Check Endpoint: A simple root endpoint (/) is provided to quickly verify the API's operational status.

🛠️ Technologies Used
FastAPI: Modern, asynchronous, and high-performance web framework for building APIs with Python 3.7+ based on standard Python type hints.

Pydantic: Data validation and settings management using Python type hints, ensuring robust and error-free data handling.

scikit-learn: The fundamental machine learning library used for the RandomForestClassifier model.

joblib: A robust library for persisting and loading Python objects, specifically used here for efficient handling of the trained ML model.

Pandas: The go-to library for data analysis and manipulation, crucial for preparing input data for the model.

Uvicorn: A lightning-fast ASGI server, responsible for running the FastAPI application.

🚀 Getting Started
Follow these straightforward steps to get the Diabetes Prediction API up and running on your local machine.

Prerequisites

Python 3.8+ installed.

pip (Python package installer).

1. Clone the Repository

First, grab a copy of this GitHub repository by cloning it to your local machine:

git clone https://github.com/YourUsername/your-repo-name.git
cd your-repo-name

(Remember to replace YourUsername and your-repo-name with your actual GitHub username and repository name.)

2. Create a Virtual Environment (Recommended)

It's always a best practice to use a virtual environment to isolate and manage your project dependencies:

python -m venv venv

Activate your newly created virtual environment:

On macOS/Linux:

source venv/bin/activate

On Windows:

.\venv\Scripts\activate

3. Install Dependencies

Create a requirements.txt file in the root of your project (if you don't have one) with the following essential content:

fastapi
uvicorn
pydantic
scikit-learn
pandas
joblib

Then, install all the required packages:

pip install -r requirements.txt

4. Place Your Trained Model

Ensure your pre-trained machine learning model file, specifically named diabetes_prediction_rfc.pkl, is placed directly in the root directory of this project, right alongside diabetes_prediction_fastapi.py.

5. Run the API

Navigate to the directory containing diabetes_prediction_fastapi.py (if you're not already there) and launch the API using uvicorn:

uvicorn diabetes_prediction_fastapi:app --reload

You should see console output indicating that the server is successfully running, typically accessible at http://127.0.0.1:8000.

🧪 How to Test the API
Once the API is live, you can easily test its functionality using various convenient methods:

1. FastAPI Interactive Docs (Swagger UI)

This is the easiest way to test locally! Open your web browser and navigate to: http://127.0.0.1:8000/docs

For / (GET): Expand the endpoint, click the "Try it out" button, and then "Execute." You should instantly see a 200 OK response with {"message": "Diabetes prediction API is running"}.

For /diabetes_prediction (POST): Expand this endpoint, click "Try it out," and modify the pre-filled example JSON request body with your desired input parameters. Finally, click "Execute" to receive the prediction.

2. Using curl (Command Line)

For quick command-line testing, curl is your friend!

Test Root Endpoint:

curl http://127.0.0.1:8000/

Test Prediction Endpoint:

curl -X POST "http://127.0.0.1:8000/diabetes_prediction" \
     -H "Content-Type: application/json" \
     -d '{
       "gender": "Female",
       "age": 45,
       "hypertension": 0,
       "heart_disease": 0,
       "smoking_history_cleaned": "never",
       "bmi": 25.5,
       "HbA1c_level": 5.8,
       "blood_glucose_level": 120
     }'

🔗 API Endpoints
Here's a detailed breakdown of the API's available endpoints:

GET /

Description: A simple health check endpoint to confirm the API is operational.

Response:

{
  "message": "Diabetes prediction API is running"
}

POST /diabetes_prediction

Description: The core endpoint for predicting whether a patient has diabetes based on provided health metrics.

Request Body (ModelInput - JSON Example):

{
  "gender": "Female",
  "age": 45,
  "hypertension": 0,
  "heart_disease": 0,
  "smoking_history_cleaned": "never",
  "bmi": 25.5,
  "HbA1c_level": 5.8,
  "blood_glucose_level": 120
}

Parameter Details:

gender: Literal['Female', 'Male', 'Other'] - Patient's biological gender.

age: int - Patient's age in years (e.g., 18-90).

hypertension: int (0 or 1) - 0 if no hypertension, 1 if hypertension is present.

heart_disease: int (0 or 1) - 0 if no heart disease, 1 if heart disease is present.

smoking_history_cleaned: Literal['never', 'unknown', 'current', 'past'] - Patient's smoking history.

bmi: float - Body Mass Index (BMI).

HbA1c_level: float - Hemoglobin A1c level, indicating average blood sugar over 2-3 months.

blood_glucose_level: int - Fasting blood glucose level.

Successful Response (JSON Example - Diabetes Predicted):

{
  "prediction": 1,
  "message": "This patient HAS Diabetes"
}

Successful Response (JSON Example - No Diabetes Predicted):

{
  "prediction": 0,
  "message": "This patient DOES NOT have Diabetes"
}

Error Response (JSON Example - Validation Error):

{
  "detail": [
    {
      "type": "literal_error",
      "loc": [
        "body",
        "gender"
      ],
      "msg": "Input should be 'Female', 'Male', or 'Other'",
      "input": "Invalid",
      "url": "https://errors.pydantic.dev/2.5/v/literal_error"
    }
  ]
}

Error Response (JSON Example - Server Error):

{
  "error": "Details of the internal server error"
}

📂 Project Structure
.

├── diabetes_prediction_fastapi.py   # 🐍 The main FastAPI application code

├── diabetes_prediction_rfc.pkl      # 🧠 The pre-trained machine learning model file

├── requirements.txt                 # 📦 List of Python dependencies

├── diabetes_prediction_notebook.ipynb # 📊 Jupyter Notebook with model training details

└── README.md                        # 📄 This README file

📈 Model Training and Evaluation
The RandomForestClassifier model at the heart of this API was meticulously trained by me! You can dive deep into the entire training process, including data preprocessing steps, feature engineering, and comprehensive model evaluation metrics, by exploring the provided Jupyter Notebook:

diabetes_prediction_notebook.ipynb 🚀

This notebook covers:

Data Loading and Initial Exploration 📊

Handling Missing Values and Outliers 🧹

Feature Engineering (e.g., smoking_history_cleaned) 💡

Data Scaling and Encoding 📏

Model Selection and Hyperparameter Tuning (GridSearchCV, SMOTE for imbalanced data) ⚙️

Evaluation Metrics (Classification Report, Confusion Matrix, Feature Importance) ✅

Model Persistence (joblib.dump) 💾

🤝 Contributing
Contributions, issues, and feature requests are highly welcome! If you're interested in improving this project, feel free to check the issues page for open tasks or submit your own pull requests.

📄 License
This project is open source and available under the MIT License.


AUTHOR:

OKONJI CHUKWUNONYELIM GABRIEL -- ML ENGINEER/ DATA SCIENTIST


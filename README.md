# AI-Powered Fraud Detection System

## Overview
This project implements a fraud detection system that analyzes transaction data to detect potential fraud using machine learning models. The models are trained using popular libraries such as XGBoost and scikit-learn, and the project integrates with cloud services like Azure, AWS, and Google Cloud for training and deployment.

## Setup

### Requirements
- Python 3.8+
- Docker (optional, for containerization)
- Cloud service accounts (Azure, AWS, Google Cloud)

### Installation
Clone the repository and install the dependencies:
```bash
git clone https://github.com/mdibella11/fraud-detection-api.git
cd fraud-detection-api
pip install -r config/requirements.txt
```

### Docker Setup (Optional)
If you'd like to run the project in a containerized environment using Docker, follow these steps:

1. **Build the Docker Image:**
   ```bash
   docker build -t fraud-detection-api .
   ```

2. **Run the Docker Container:**
   ```bash
   docker run -d -p 5000:5000 fraud-detection-api
   ```

   This will run your application in the background, and you can access it on port 5000. Replace `5000` with another port if necessary.

### Cloud Integration
The system supports integration with the following cloud platforms:
- **Azure ML**
- **AWS SageMaker**
- **Google AI Platform**

Follow the instructions in the respective folders (`cloud/azure`, `cloud/aws`, `cloud/google`) for setting up model training and deployment.

### Running Locally
Run the model training locally:
```bash
python app/train_model.py
```

### Predicting via API
To get predictions from the trained model:
1. Start the Flask API:
   ```bash
   python app/fraud_detection.py
   ```

2. Use a tool like Postman or cURL to make a POST request to `http://localhost:5000/predict` with the transaction data.

### License
MIT License. See [LICENSE](LICENSE) for details.

## Author
Marco Di Bella

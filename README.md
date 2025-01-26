# AI-Powered Fraud Detection System

An advanced API designed to analyze transactions or activities (e.g., banking transactions or credit card payments) and determine if they present a fraud risk. This API leverages trained machine learning models to detect patterns indicative of fraudulent behavior.

---

## How the API Works

### 1. Sample Data (CSV File)
The project includes a sample dataset in `transaction_data.csv`. This file is used to train the machine learning model. The dataset contains the following example fields:

- **Transaction ID**: A unique identifier for each transaction.
- **Amount**: The transaction amount.
- **Date**: The date of the transaction.
- **Payment Method**: E.g., credit card, bank transfer, etc.
- **Location**: The user's location at the time of the transaction.
- **Activity Type**: E.g., purchase, withdrawal, etc.

**Sample CSV Example:**
```csv
transaction_id,amount,date,payment_method,location,activity_type
1,100,2025-01-01,credit_card,New York,purchase
2,500,2025-01-02,debit_card,Los Angeles,purchase
3,3000,2025-01-03,credit_card,London,withdrawal
4,50,2025-01-04,credit_card,Paris,purchase
```

---

### 2. Model Training
The machine learning model is trained using the dataset provided in the CSV file. Key steps in the training process:

- **Technologies Used:**
  - `scikit-learn` for basic machine learning models (e.g., Logistic Regression, Random Forest).
  - `XGBoost` for advanced modeling on large datasets.
  - `TensorFlow` for deep learning models (if required).

The training process supports multiple cloud platforms:

- **Azure**: Azure ML is used for training and deployment.
- **AWS**: SageMaker handles large dataset training and model hosting.
- **Google Cloud**: AI Platform manages training and model operations.

Setup instructions for each cloud platform are provided in respective `cloud/azure`, `cloud/aws`, and `cloud/google` folders.

---

### 3. Prediction Endpoint
The API exposes a RESTful endpoint to analyze transactions. Users can send transaction data in the following JSON format:

```json
{
  "transaction_id": 12345,
  "amount": 200.0,
  "payment_method": "credit_card",
  "location": "Rome",
  "activity_type": "purchase"
}
```

The API processes this input, performs preprocessing (e.g., normalizing data, handling categorical values), and sends it to the trained model.

---

### 4. Fraud Detection Output
The model predicts whether the transaction is fraudulent and returns a response like this:

```json
{
  "transaction_id": 12345,
  "is_fraud": true,
  "fraud_probability": 0.85
}
```

In this example, transaction ID `12345` is flagged as fraudulent with an 85% probability.

---

### 5. Docker Deployment
The API is containerized for easier deployment using Docker.

**To build and run the container:**
```bash
# Build the Docker image
docker build -t fraud-detection-api .

# Run the container
docker run -p 8000:8000 fraud-detection-api
```

The API will be accessible at `http://localhost:8000`.

---

### 6. Environment Configuration
The project uses a `.env.example` file for managing environment variables like cloud service credentials. To configure:

1. Copy `.env.example` to `.env`.
2. Update the `.env` file with your credentials and configurations.

---

## Features

- **Advanced Fraud Detection**: Leveraging machine learning to detect fraudulent patterns in transactions.
- **Cloud Integration**: Supports Azure, AWS, and Google Cloud for model training and deployment.
- **RESTful API**: Easy-to-use endpoints for predictions.
- **Containerized Deployment**: Ready-to-use Docker setup.

---

## Project Structure

- **`app/`**: Contains the FastAPI application.
- **`config/`**: Contains config files.
- **`models/`**: Scripts and files for training the machine learning models.
- **`data/`**: Sample data (`transaction_data.csv`).
- **`cloud/`**: Instructions for cloud integration.
  - `azure/`: Azure-specific setup instructions.
  - `aws/`: AWS-specific setup instructions.
  - `google/`: Google-specific setup instructions.
- **`Dockerfile`**: Docker configuration for containerization.
- **`.env.example`**: Example environment configuration.

---

## Author

Developed by **Marco Di Bella**.

---

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.

---

## In Summary
This API processes transaction data, applies machine learning techniques to assess fraud risks, and provides predictions. With support for multiple cloud platforms and containerized deployment, it’s ready for diverse environments and use cases.

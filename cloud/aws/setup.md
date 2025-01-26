
# AWS Setup for Fraud Detection Model

## Requirements
- AWS account
- AWS SageMaker

## Steps
1. **Create an AWS SageMaker Notebook Instance**:
   - Log in to the AWS console and create a SageMaker notebook instance.
   - Follow the instructions here: https://docs.aws.amazon.com/sagemaker/latest/dg/how-it-works-notebooks.html

2. **Upload Data and Train Model**:
   - Upload your transaction data to Amazon S3.
   - Use SageMaker's built-in algorithms or custom model training using XGBoost.
   - Instructions: https://docs.aws.amazon.com/sagemaker/latest/dg/xgboost.html

3. **Deploy Model**:
   - After training, deploy the model using SageMaker endpoints.
   - Guide: https://docs.aws.amazon.com/sagemaker/latest/dg/ex1.html

# Models

This directory contains scripts for training and storing the machine learning models.

- `train_model.py`: The training script.
- `fraud_detection_model.pkl`: Generated after training, contains the serialized ML model.

## Steps to Train the Model

1. Place your dataset (`transaction_data.csv`) in the `../data/` directory.
2. Run the training script:
   ```bash
   python train_model.py
   ```
3. The trained model is saved as `fraud_detection_model.pkl`.

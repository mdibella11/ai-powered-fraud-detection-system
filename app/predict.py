
import xgboost as xgb
import pandas as pd

model = xgb.XGBClassifier()
model.load_model('fraud_detection_model.xgb')

new_data = pd.read_csv('data/new_transaction_data.csv')

predictions = model.predict(new_data)

print(predictions)


from flask import Flask, request, jsonify
import xgboost as xgb
import pandas as pd

app = Flask(__name__)

model = xgb.XGBClassifier()
model.load_model('fraud_detection_model.xgb')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    df = pd.DataFrame(data)
    prediction = model.predict(df)
    return jsonify({"prediction": prediction.tolist()})

if __name__ == '__main__':
    app.run(debug=True)

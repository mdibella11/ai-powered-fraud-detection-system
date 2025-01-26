# train_model.py

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report
import joblib

def main():
    data = pd.read_csv('../data/transaction_data.csv')
    X = data.drop(columns=['is_fraud'])
    y = data['is_fraud']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    preds = model.predict(X_test)
    print(classification_report(y_test, preds))
    joblib.dump(model, 'fraud_detection_model.pkl')
    print("Model saved as fraud_detection_model.pkl")

if __name__ == '__main__':
    main()

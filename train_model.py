from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import roc_auc_score
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from data import df
import joblib
import pandas as pd



X= df.drop(columns=["is_default"])
y = df["is_default"]

x_train, x_test, y_train, y_test= train_test_split(X, y, test_size=0.3, random_state=42, shuffle=True, stratify=y)


model = Pipeline([
    ("scaler", StandardScaler()),
    ("model", LogisticRegression(max_iter=1000, n_jobs=-1, class_weight="balanced"))
])

model.fit(x_train,y_train)

dummy_model = {
  "loan_amnt": 15000,
  "term": 36,
  "int_rate": 13.5,
  "installment": 510,
  "emp_length": 5,
  "annual_inc": 65000,
  "verification_status": 1,
  "dti": 18.2,
  "delinq_2yrs": 0,
  "inq_last_6mths": 1,
  "open_acc": 7,
  "pub_rec": 0,
  "revol_bal": 12000,
  "revol_util": 45.3,
  "total_acc": 18,

  "grade_B": True,
  "grade_C": False,
  "grade_D": False,
  "grade_E": False,
  "grade_F": False,
  "grade_G": False,

  "home_ownership_MORTGAGE": True,
  "home_ownership_NONE": False,
  "home_ownership_OTHER": False,
  "home_ownership_OWN": False,
  "home_ownership_RENT": False
}

y_pred_proba = model.predict_proba(x_test)[:, 1]

predict_to_dummy = model.predict(dummy_model)
roc = roc_auc_score(y_test, y_pred_proba)
print("ROC-AUC:", roc)

joblib.dump(model, "loan_default_pipeline.pkl")
joblib.dump(X.columns.tolist(), "feature_columns.pkl")

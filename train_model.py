from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import roc_auc_score
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from data import df
import joblib




X= df.drop(columns=["is_default"])
y = df["is_default"]

x_train, x_test, y_train, y_test= train_test_split(X, y, test_size=0.3, random_state=42, shuffle=True, stratify=y)


model = Pipeline([
    ("scaler", StandardScaler()),
    ("model", LogisticRegression(max_iter=1000, n_jobs=-1, class_weight="balanced"))
])

model.fit(x_train,y_train)



y_pred_proba = model.predict_proba(x_test)[:, 1]


roc = roc_auc_score(y_test, y_pred_proba)
print("ROC-AUC:", roc)

joblib.dump(model, "loan_default_pipeline.pkl")
joblib.dump(X.columns.tolist(), "feature_columns.pkl")

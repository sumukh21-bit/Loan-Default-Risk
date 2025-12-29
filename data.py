import pandas as pd
import numpy as np
import kaggle as kl


# data = pd.read_csv("DATA.csv", low_memory=False)

df = pd.DataFrame(data)

df = df[["loan_amnt","term","int_rate","installment","grade","sub_grade","emp_length","home_ownership","annual_inc","verification_status","purpose","addr_state","dti","delinq_2yrs","inq_last_6mths","open_acc","pub_rec","revol_bal","revol_util","total_acc","issue_d","earliest_cr_line", "loan_status"]]


df= df[df["loan_status"].isin(["Fully Paid","Current","Default"])].copy()


df["is_default"] = df["loan_status"].map({
    "Fully Paid": 0,
    "Charged Off": 1,
    "Default": 1
})

df.dropna(subset=["is_default"], inplace=True)

df["is_default"]=df["is_default"].astype(int)

df["term"] = df["term"].astype(str)
df["term"] = df["term"].str.replace(" months", "", regex=False)
df["term"] = pd.to_numeric(df["term"], errors="coerce")




df["emp_length"]=df["emp_length"].replace({
    "10+ years": "10",
        "< 1 year": "0",
        "n/a": np.nan,
})

df["emp_length"]= df["emp_length"].astype(str)
df["emp_length"]=df["emp_length"].str.replace(" years","", regex=False)
df["emp_length"]=pd.to_numeric(df["emp_length"],errors="coerce")

df["verification_status"] = df["verification_status"].map({
    "Verified":1,
    "Source Verified": 1,
    "Not Verified": 0
})


df = pd.get_dummies(
    df,
    columns=["grade", "home_ownership"],
    drop_first=True
)


df.drop(columns=["loan_status"], inplace=True)


df.dropna(inplace=True)

print("Final dataset shape:", df.shape)
print(df.head())

df.drop(
    columns=[
        "sub_grade",
        "purpose",
        "addr_state",
        "issue_d",
        "earliest_cr_line"
    ],
    inplace=True
)

print(df.dtypes)
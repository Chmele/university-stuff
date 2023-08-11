import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC


selected_fields = ["CVSS", "CVSS3.1", "QDS"]
data = pd.read_csv("vulnreport.csv")[selected_fields].dropna()

X = data.drop("QDS", axis=1)
y = data["QDS"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

model = SVC(kernel='rbf')
model.fit(X_train, y_train)
print("Accuracy:", model.score(X_test, y_test))

new_data = [
    pd.DataFrame({
        "CVSS": ["7.7"],
        "CVSS3.1": ["9.3"],
    }),
    pd.DataFrame({
        "CVSS": ["0.7"],
        "CVSS3.1": ["1.3"],
    }),
    pd.DataFrame({
        "CVSS": ["9.7"],
        "CVSS3.1": ["1.3"],
    }),
    pd.DataFrame({
        "CVSS": ["2.7"],
        "CVSS3.1": ["9.3"],
    }),
]
for d in new_data:
    print(d, "Predicted QDS:", model.predict(d))
    

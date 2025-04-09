from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
import pandas as pd

# 1. Load a built-in dataset (Iris)
iris = datasets.load_iris()

# 2. Convert dataset to DataFrame for readability
df = pd.DataFrame(iris.data, columns=iris.feature_names)
df["target"] = iris.target

# 3. View first few rows
df.head()

# 4. Check data types
df.dtypes

# 5. Split data into features (X) and labels (y)
X = iris.data
y = iris.target

# 6. Split into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 7. Scale features using StandardScaler
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# 8. Encode labels if needed (for categorical labels)
le = LabelEncoder()
y_encoded = le.fit_transform(y)

# 9. Train a logistic regression model
lr = LogisticRegression()
lr.fit(X_train_scaled, y_train)

# 10. Predict on test data
y_pred = lr.predict(X_test_scaled)

# 11. Calculate accuracy
accuracy_score(y_test, y_pred)

# 12. Generate confusion matrix
confusion_matrix(y_test, y_pred)

# 13. Generate classification report
print(classification_report(y_test, y_pred))

# 14. Train a decision tree classifier
dt = DecisionTreeClassifier()
dt.fit(X_train, y_train)

# 15. Predict using decision tree
dt_pred = dt.predict(X_test)

# 16. Train an SVM classifier
svm = SVC()
svm.fit(X_train_scaled, y_train)

# 17. Make prediction with SVM
svm.predict(X_test_scaled)

# 18. Check feature importance (for tree models)
dt.feature_importances_

# 19. Use a different dataset (e.g., digits)
digits = datasets.load_digits()
digits.data.shape  # Check shape (samples, features)

# 20. Use pipeline for scaling + model in one step
from sklearn.pipeline import make_pipeline
pipeline = make_pipeline(StandardScaler(), LogisticRegression())
pipeline.fit(X_train, y_train)
pipeline.predict(X_test)

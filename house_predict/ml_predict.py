import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error

df = pd.read_csv("train.csv")
print("Veri seti boyutu:", df.shape)
print(df.head())

missing = df.isnull().sum()
print("Eksik değerler:\n", missing[missing > 0])

df = df.fillna(df.median(numeric_only=True))

features = ["OverallQual", "GrLivArea", "GarageCars", "TotalBsmtSF", "FullBath", "YearBuilt"]
X = df[features]
y = df["SalePrice"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LinearRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

mae = mean_absolute_error(y_test, y_pred)
rmse = np.sqrt(mean_squared_error(y_test, y_pred))

print(f"MAE: {mae:.2f}")
print(f"RMSE: {rmse:.2f}")

plt.scatter(y_test, y_pred, alpha=0.7, color="blue")
plt.xlabel("Gerçek Fiyat")
plt.ylabel("Tahmin Fiyat")
plt.title("Ev Fiyat Tahminleri")
plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], color="red")  # doğru tahmin çizgisi
plt.show()

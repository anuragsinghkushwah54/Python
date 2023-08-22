 import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import mean_squared_error,accuracy_score
import math

# Load weather data (assuming it is stored in an Excel file)  
weather_data = pd.read_excel('seattle-weather.xlsx')

# Prepare the data by separating features and target variable
features = weather_data[['precipitation', 'temp_max', 'temp_min', 'wind']]

# Extract the target variable
target = weather_data['weather']

# Label encode the target variable
label_encoder = LabelEncoder()
y = label_encoder.fit_transform(target)

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(features, y, test_size=0.15, random_state=42)

# Support Vector Machine (SVM) classification
svm_model = SVC()
svm_model.fit(X_train, y_train)
svm_predictions = svm_model.predict(X_test)
svm_accuracy = accuracy_score(y_test, svm_predictions)
print("Accuracy:", svm_accuracy)

# Linear Regression
linear_model = LinearRegression()
linear_model.fit(X_train, y_train)
linear_predictions = linear_model.predict(X_test)
linear_rmse = math.sqrt(mean_squared_error(y_test, linear_predictions))
print("Linear Regression Root Mean Squared Error:", linear_rmse)

# Prediction on Training data
y_pred_train = linear_model.predict(X_train)

# Create scatterplot with regression line
#sns.regplot(y_test, target, scatter_kws={"color": "green"}, line_kws={"color": "blue"}) 
plt.scatter(y_train, y_pred_train, color='green', label='Actual vs Predicted')
plt.plot(y_train, y_train, color='blue', label='Regression Line')
plt.xlabel('Actual')
plt.ylabel('Predicted')
plt.title('Scatterplot with Regression Line')
plt.legend()
plt.show()
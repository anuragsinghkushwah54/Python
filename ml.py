import pandas as pd
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split

weather_data = pd.read_excel('seattle-weather.xlsx')

# Assuming weather_data is a DataFrame containing the weather data

# Extract the features
features = weather_data[['precipitation', 'temp_max', 'temp_min', 'wind']]

# Extract the target variable
target = weather_data['weather']

# Label encode the target variable
label_encoder = LabelEncoder()
y = label_encoder.fit_transform(target)

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(features, y, test_size=0.15, random_state=42)
print(X_train.size,X_test.size)

# Create an SVM classifier
svm = SVC()

# Train the SVM classifier
svm.fit(X_train, y_train)

# Make predictions on the test set
y_pred = svm.predict(X_test)

# Evaluate the accuracy of the model
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)
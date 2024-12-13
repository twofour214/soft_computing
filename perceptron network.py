from sklearn.datasets import make_classification
from sklearn.linear_model import Perceptron

# Generate a classification dataset
x, y = make_classification(n_samples=1000, n_features=10, n_redundant=0, random_state=1)

# Create and train the Perceptron model
model = Perceptron()
model.fit(x, y)
print(x[0])

# Define a new input row for prediction
row = x[0]

# Make a prediction
y_pred = model.predict([row])

# Display the prediction
print('Predicted:', int(y_pred[0]))

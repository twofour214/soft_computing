# Define a simple linear neural network class
class SimpleLinearNN:
    def __init__(self, weight, bias):
        self.weight = weight
        self.bias = bias

    def predict(self, x):
        # Linear combination of input with weight and bias
        yin = self.bias + (self.weight * x)
        return yin

# Initialize the neural network with weight and bias
weight = float(input("Enter the weight value: "))
bias = float(input("Enter the bias value: "))
model = SimpleLinearNN(weight, bias)

# Test the model with a sample input
input_value = float(input("Enter the input value: "))
output = model.predict(input_value)

print("The net input (yin) for input ",input_value, " is:  ", output)

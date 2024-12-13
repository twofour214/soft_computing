import numpy as np
x = np.zeros([3,])
weights = np.zeros([3,])
desired = np.zeros([3,])
actual = np.zeros([3,])
for i in range(0,3):
  x[i] = float(input("Enter inputs: "))

print("Inputs are: ", x)
for i in range(0,3):
  weights[i] = float(input("Enter initial weights: "))

print("Weights are: ", weights)
for i in range(0,3):
  desired[i] = float(input("Enter desired outputs: "))

print("Desired outputs are: ", desired)
a = float(input("Enter the learning rate: "))
print("Learning rate is ", a)

actual = x * weights
print("Actual output is: ", actual)
print("Desired output is: ", desired)

while True:
  if np.array_equal(actual, desired):
    break
  else:
    for i in range(0, 3):
      weights[i] = weights[i] + a * (desired[i] - actual[i])
  actual = x * weights
print("Final weights are ", weights, " makes predicted output ", actual, " desired output ", desired, " same.")

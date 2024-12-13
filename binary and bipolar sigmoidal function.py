w = []
x = []
n = int(input("Enter the number of input neurons: "))
bias = float(input("Enter the bias: "))

# Input values and weights
for i in range(0, n):
    a = float(input("Enter the input for neuron {i+1}: "))
    x.append(a)
    b = float(input("Enter the weight for neuron {i+1}: "))
    w.append(b)

print("The given inputs are: ", x)
print("The given weights are: ", w)
print("The bias value is: ", bias)

# Calculate net input
yin = bias + sum([w[i] * x[i] for i in range(n)])
print("The net input is: ", yin)

# Binary output calculation
threshold = float(input("Enter the threshold value for binary output: "))
if yin >= threshold:
    output_binary = 1
else:
    output_binary = 0

print("Final Output (binary) is: ", output_binary)

# Bipolar output calculation
threshold = float(input("Enter the threshold value for bipolar output: "))
if yin >= threshold:
    output_bipolar = 1
else:
    output_bipolar = -1

print("Final Output (bipolar) is: ", output_bipolar)

# Get the number of inputs
num_ip = int(input("Enter the number of inputs: "))
theta = 1
x1 = []
x2 = []

# Collect inputs for x1 and x2
for i in range(num_ip):
    a = int(input("Enter the input for x1[{i+1}]: "))
    x1.append(a)
    b = int(input("Enter the input for x2[{i+1}]: "))
    x2.append(b)

# Display the input lists
print('x1:', x1)
print('x2:', x2)

# Case 1: w1 and w2 = 1
print("Case 1: w1 and w2 = 1")
w1 = w2 = 1

case_y1 = []
case_yin1 = []

# Calculate net input (yin) and output (y) for Case 1
for i in range(num_ip):
    yin = (x1[i] * w1) + (x2[i] * w2)
    case_yin1.append(yin)
    case_y1.append(1 if yin >= theta else 0)

# Display results for Case 1
print('Net Inputs (Case 1):', case_yin1)
print('Outputs (Case 1):', case_y1)

# Case 2: w1 = 1 and w2 = -1
print("Case 2: w1 = 1 and w2 = -1")
w1 = 1
w2 = -1
case_y2 = []
case_yin2 = []

# Calculate net input (yin) and output (y) for Case 2
for i in range(num_ip):
    yin = (x1[i] * w1) + (x2[i] * w2)
    case_yin2.append(yin)
    case_y2.append(1 if yin >= theta else 0)

# Display results for Case 2
print('Net Inputs (Case 2):', case_yin2)
print('Outputs (Case 2):', case_y2)

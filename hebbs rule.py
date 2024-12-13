import numpy as np

# Input vectors
x1 = np.array([1, 1, 1, -1, 1, -1, 1, 1, 1])
x2 = np.array([1, 1, 1, 1, -1, 1, 1, 1, 1])

# Target outputs
y = np.array([1, -1])

# Initial weights and bias
wt_old = np.zeros([9,])
wt_new = np.zeros([9,])
b = 0

# Convert weights into integers (if needed, though not usually required)
wt_old = wt_old.astype(int)
wt_new = wt_new.astype(int)

print("Initial weights: ", wt_old)
print("Initial bias: ", b)

# Processing the first pattern (x1, target = 1)
print("\nFor first pattern with target == 1")
for i in range(0, 9):
    wt_old[i] = wt_old[i] + x1[i] * y[0]

wt_new = wt_old.copy()
b = b + y[0]

# Printing updated weights and bias after first pattern
print("Updated weights after first pattern: ", wt_new)
print("Updated bias after first pattern: ", b)

# Processing the second pattern (x2, target = -1)
print("\nFor second pattern with target == -1")
for i in range(0, 9):
    wt_old[i] = wt_old[i] + x2[i] * y[1]

wt_new = wt_old.copy()
b = b + y[1]

# Printing updated weights and bias after second pattern
print("Updated weights after second pattern: ", wt_new)
print("Updated bias after second pattern: ", b)

# Function to check if two lists overlap
list_1 = [1, 2, 3, 4, 5]
list_2 = [6, 7, 8, 9]

def overlapping(list1, list2):
    for i in list1:
        if i in list2:
            return 1
    return 0

if overlapping(list_1, list_2):
    print("Overlapping")
else:
    print("No Overlapping")

x = 5
print("True" if type(x) is int else "False")  # Using `is`
print("True" if type(x) is not int else "False")  # Using `is not`

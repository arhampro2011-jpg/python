import numpy as np

orginal_array = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

print("Original array:")
print(orginal_array)

new_array = np.array([0, -1, 2, -1, 4, -1, 6, -1, 8, -1])

print("New array:")
print(new_array)

two_d_array = orginal_array.reshape(2, 5)

print("2 dimensional array:")
print(two_d_array)

sum_of_eleements = 0

for i in orginal_array:
    sum_of_eleements = sum_of_eleements + i

print("Sum of all elements:", sum_of_eleements)
import numpy as np
import matplotlib.pyplot as plt

list_1d = [1, 2, 3, 4, 5]
array_1d = np.array(list_1d)
print(array_1d)

# 2d array

list_2d = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
array_2d = np.array(list_2d)
print(array_2d)

# 3d array

list_3d = [[[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[10, 11, 12], [13, 14, 15], [16, 17, 18]]]
array_3d = np.array(list_3d)
print(array_3d)


print(type(array_1d), type(array_2d), type(array_3d))

# creating arrays from scratch

# np.arange(start, stop, step)

arange_array = np.arange(1, 10, 2)
print(array_1d)


# np.zeros(shape, dtype)

zeros_array = np.zeros((2, 3), dtype=str)
print(zeros_array)

# np.random.random(shape: tuple)

random_array = np.random.random((2, 3))
print(random_array)

plt.scatter(random_array[:, 0], random_array[:, 1])
plt.show()
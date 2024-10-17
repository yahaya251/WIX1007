import numpy as np
#1
array_2x2 = np.array([[1, 2], [3, 4]])
print("2x2 Array:\n", array_2x2)

#2
random_array_3x4 = np.random.rand(3, 4)
print("Random 3x4 Array:\n", random_array_3x4)

#3
ones_array = np.ones((2, 2))
zeroes_array = np.zeros((2, 2))
print("Array of Ones:\n", ones_array)
print("Array of Zeroes:\n", zeroes_array)

#4
random_array_6x3 = np.random.rand(6, 3)
transposed_array = random_array_6x3.T
print("Random 6x3 Array:\n", random_array_6x3)
print("Transposed Array:\n", transposed_array)

#5
n=3
p=2
m=4

array_np = np.random.rand(n, p)
array_pm = np.random.rand(p, m)

dot_product = np.dot(array_np, array_pm)

print("Random n x p Array:\n", array_np)
print("Random p x m Array:\n", array_pm)
print("Dot Product:\n", dot_product)



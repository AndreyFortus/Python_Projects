# NumPy Exercises
from io import BytesIO
from PIL import Image
from scipy.signal import argrelextrema

import numpy as np
import requests

# level №1
print('\ntask 1\n', np.__version__)

np1 = np.arange(10)
print('\ntask 2\n', np1)

np2 = np.full((3, 3), True)
print('\ntask 3\n', np2)

np3 = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
print('\ntask 4\n', np3[np3 % 2 == 1])

np4 = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
np4[np4 % 2 == 1] = -1
print('\ntask 5\n', np4)

np5 = np.arange(10)
new_np5 = np.where(np5 % 2 == 1, -1, np5)
print('\ntask 6\n', new_np5)

np6 = np.arange(10)
print('\ntask 7\n', np6.reshape(2, 5))  # or use second parameter as -1, auto decide

# level №2
np7_a = np.arange(10).reshape(2, -1)
np7_b = np.repeat(1, 10).reshape(2, -1)
print('\ntask 8\n', np.vstack([np7_a, np7_b]))

np8_a = np.arange(10).reshape(2, -1)
np8_b = np.repeat(1, 10).reshape(2, -1)
print('\ntask 9\n', np.hstack([np8_a, np8_b]))

np.random.seed(100)
np9_a = np.random.uniform(1, 50, 20)
np4[np4 % 2 == 1] = -1
np9_b = np.where(np9_a < 10, 10, np.where(np9_a > 30, 30, np9_a))
print('\ntask 47\n', np9_b)

# this task isn't solved by me, task use as example how to work with links
URL_25 = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
iris = np.genfromtxt(URL_25, delimiter=',', dtype='object')
names = ('sepallength', 'sepalwidth', 'petallength', 'petalwidth', 'species')
print('\ntask №25\n', iris[: 3])

# level №3
URL_34 = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
iris_2d = np.genfromtxt(URL_34, delimiter=',', dtype='float', usecols=[0, 1, 2, 3])
filt_rows = (iris_2d[:, 2] > 1.5) & (iris_2d[:, 0] < 5.0)
print('\ntask №34\n', iris_2d[filt_rows])

np.random.seed(100)
a_58 = np.random.randint(0, 5, 10)
print(f'\ntask №58\n Array: {a_58}')
m = np.zeros_like(a_58, dtype=bool)
m[np.unique(a_58, return_index=True)[1]] = True
print(np.invert(m, dtype=bool))

URL_60 = 'https://upload.wikimedia.org/wikipedia/commons/8/8b/Denali_Mt_McKinley.jpg'
response_60 = requests.get(URL_60, 1)
img_60 = Image.open(BytesIO(response_60.content))
numpydata = np.asarray(img_60)
print('\ntask №60\n', numpydata)

# level №4
a_63 = np.array([1, 3, 7, 1, 2, 6, 0, 1])
print('\ntask №63\n', argrelextrema(a_63, np.greater))

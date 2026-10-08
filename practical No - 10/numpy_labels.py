import numpy as np

arr = np.array([10,20,30,40,50])

labels = ['a','b','c','d','e']

print("1D Array with Labels")

for i in range(len(arr)):
    print(labels[i], arr[i])
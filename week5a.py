import math
import os.path #Python 2
import numpy as np



arr1 = np.arange(0,100, dtype=float)
arr2 = arr1.reshape((10, 10))
print (arr1)
print (arr2)

data = np.genfromtxt('bikeSharing.csv', dtype=float, delimiter =
',')
count = data[:, 12]
total = 0.0
for value in count:
  total += value
print ("Average wind is ", total/len(count)*67)

arr = np.array([[1, 2, 3], [4, 5, 6]],
float)
print (arr)
arr1 = np.append(arr, [[7, 8, 9]])
print (arr1)

arr = np.array([[1, 2, 3], [4, 5, 6]],
float)
print (arr)
arr1 = np.append(arr, [[7, 8, 9]], axis = 0)
print (arr1)

arr = np.array([[1, 2, 3], [4, 5, 6]],
float)
print (arr)
arr1 = np.append(arr, [[7], [8]], axis = 1)
print (arr1)

arr1 = np.array([[10,20,30],[50, 60, 10]], float)
print (arr1)
print (np.amax(arr1))
print (np.amax(arr1, axis=0))
print (np.amax(arr1, axis=1))

arr1 = np.array([[1, 2, 4],[3, 4, 2]], float)
print (arr1)
print (np.sum(arr1))
print (np.product(arr1))
print (np.sum(arr1, axis = 0))
print (np.mean(arr1, axis = 1))

arr1 = np.array([10,20,30], float)
arr2 = np.array([1,2,3], float)
print (arr1*arr2)
print (arr1/arr2)
print (arr1**arr2)

arr1 = np.array([1, 3, 0], float)
arr2 = np.array([1, 2, 3], float)
resultArr = arr1>arr2
print (resultArr)
print (arr1== arr2)

arr1 = np.array([45, 3, 2, 5, 67], float)
boolArr1 = np.array([True, False, True, False, True], bool)
print (arr1[boolArr1])

arr2D = np.array([[45, 3, 67, 34],[12, 43, 73, 36]], float)
boolArr3 = np.array([True, False], bool)
print (arr2D[boolArr3])
arr2D = np.array([[45, 3, 67, 34],[12, 43, 73, 36]], float)
boolArr3 = np.array([[True, False, True, False],[True, True,
False, True]], bool)
print (arr2D[boolArr3])

arr1 = np.array([1, 3, 20, 5, 6, 78], float)
arr2 = np.array([1, 2, 3, 67, 56, 32], float)
resultArr = arr1>arr2
print (arr1[resultArr])

data = np.array([[1, 2, 3], [2, 4, 5],
[4, 5, 7], [6, 2, 3]], float)
resultA = data[:,0]>3
resultB = data[:,2]>6
print ('data[resultA]')
print (data[resultA])
print ('data[resultB]')
print (data[resultB])
print ('data[resultA & resultB]')
print (data[resultA & resultB])

a = np.matrix('1 2; 3 4')
b = np.matrix([[1, 2], [3, 4]])
print(a)
print(b)

d = np.matrix('4, 5, 6 ; 2,3,4 ; 5,6,7')
colNew= np.matrix('2, 3, 4')
print(d)
print(colNew)
#np.insert(d, colNew, axis=0)
print(d)


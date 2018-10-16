'''
Created by: Gabriel E. Rodriguez
'''

#Necessary modules
import time, random, numpy, matplotlib.pyplot as plt

def bubbleSort(arr):
    n = len(arr)
    for i in range(n-1):
        swap = False
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swap = True
        if(not swap):
            break
    return arr

def verifySort(arr):
    n = len(arr)
    for i in range(n-1):
        if arr[i]>arr[i+1]:
            return False
    return True

def testComplexity(n):
    randomArray = list(range(n))
    random.shuffle(randomArray)
    start_time = time.time()
    sortedArray = bubbleSort(randomArray)
    return time.time() - start_time

def plot(x,y,style):
    plt.plot(x,y,style)
    plt.ylabel('Time of execution (s)')
    plt.xlabel('Number of Terms')
    plt.title('Time vs N')
    plt.grid(True)

#Validation of the bubble sort
testArray = [random.randint(0,10000) for i in range(20)]
sortedArray = bubbleSort(testArray.copy())
isCorrect = verifySort(sortedArray)

print("Initial Array: ",testArray)
print("\nSorted Array: ",sortedArray)
print("\nCorrect: ", isCorrect)

#Test of complexity

x_axis = [10,100,1000,10000,20000,30000,40000,50000,60000,70000,80000,90000,100000]

'''This for loop took a huge amount of time executing,the code is commented and the results are hardcoded'''
# for i in range(len(x_axis)):
#     y_axis.append(testComplexity(x_axis[i]))

y_axis = [0.0, 0.0029914379119873047, 0.09278202056884766, 8.54219126701355,
          34.959487199783325, 78.5509865283966, 140.921147108078, 220.76867032051086,
          321.26497316360474,438.34287881851196, 579.560293674469, 740.294429063797, 917.8387105464935]

fit = numpy.polyfit(x_axis,y_axis,2)
print("Polyniomial fit of a*n^2+b*n+c :")
print("\na = " + str(fit[0]))
print("b = " + str(fit[1]))

plot(x_axis,y_axis,'b-')
plot(x_axis,numpy.polyval(fit,x_axis),'ro')

print("\nBlue: Data","\tRed: Fit")

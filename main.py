'''
The objective of this program is to analyze the algorithmic complexity of 4 proposed functions
to develop the following problem:
Find two integers from an unordered list of integers that, added together, obtain an objective value.

We are going to use the graphical method to obtain the execution time behavior of each function
as the number of data in the list increases.

Subsequently, a polynomial adjustment will be made to each data set (execution times)
to find the polynomial equation that best fits each result.
'''

#################### Import libraries #######################
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import time
import random

#################### AUXILIARY FUNCTIONS ####################

# Quicksort function
def quickSort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr.pop()

    items_greater = []
    items_lower = []

    for item in arr:
        if item > pivot:
            items_greater.append(item)
        else:
            items_lower.append(item)

    return quickSort(items_lower) + [pivot] + quickSort(items_greater)

# Binary search function
def binarySearch(arr, x):
    low = 0
    high = len(arr) - 1
    mid = 0

    while low <= high:
        mid = (high + low) // 2

        if arr[mid] < x:
            low = mid + 1

        elif arr[mid] > x:
            high = mid - 1

        else:
            return True

    return False

# Function to generate a list of random integers
def generateRandomList(n):
    arr = []
    for i in range(n):
        arr.append(random.randint(0, 2*n))
    return arr

# function to generate a scatter graph
def scatterGraph(x, y, title, x_label, y_label):
    plt.scatter(x, y)
    plt.title(title)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.grid()
    plt.show()

#################### PRINCIPAL FUNCTIONS ####################

# Function 1
def findPairs1(arr, sum):
    '''
    This function takes in an array and a sum and returns the pairs of numbers that add up to the sum.
    :param arr: List of randomly generated integers
    :param sum: Integer that corresponds to the objective sum
    :return: list of tuples (pair of numbers)
    '''
    pairs = []
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] + arr[j] == sum:
                pairs.append((arr[i], arr[j]))
    return pairs

# Function 2
def findPairs2(arr, sum):
    '''
    This function takes in an array and a sum and returns the pairs of numbers that add up to the sum.
    This function requires an ordered list (by quicksort) and performs a binary search for each element.
    :param arr: ascending sorted list
    :param sum: Integer that corresponds to the objective sum
    :return: list of tuples (pair of numbers)
    '''
    pairs = []
    arr = quickSort(arr)
    for i in range(len(arr)-1):
        if binarySearch(arr[i+1:], sum-arr[i]):
            pairs.append((arr[i], sum-arr[i]))
    return pairs

# Function 3
def findPairs3(arr, sum):
    '''
    This function takes in an array and a sum and returns the pairs of numbers that add up to the sum.
    This function uses the python defined function called sorted to sort the list
    and perform binary search to find one of the addends.
    :param arr: ascending sorted list
    :param sum: Integer that corresponds to the objective sum
    :return: list of tuples (pair of numbers)
    '''
    pairs = []
    arr = sorted(arr)
    for i in range(len(arr)-1):
        if binarySearch(arr[i+1:], sum-arr[i]):
            pairs.append((arr[i], sum-arr[i]))
    return pairs

# Function 4
def findPairs4(arr, sum):
    '''
    This function takes in an array and a sum and returns the pairs of numbers that add up to the sum.
    This function uses a dictionary to store the addends and their complements.
    :param arr: List of randomly generated integers
    :param sum: Integer that corresponds to the objective sum
    :return: list of tuples (pair of numbers)
    '''
    pairs = []
    numbers_seen = {}
    for number in arr:
        missing_number = sum - number
        if missing_number in numbers_seen:
            pairs.append((number, missing_number))
        else:
            numbers_seen[number] = True
    return pairs

def main():
    times1 = []
    times2 = []
    times3 = []
    times4 = []
    n = []

    sum = 0 # Worst of cases
    N = 1000

    for i in range(1,N+1):
        arr = generateRandomList(i)
        n.append(i)

        start = time.perf_counter()
        findPairs1(arr, sum)
        end = time.perf_counter()
        times1.append(end-start)

        start = time.perf_counter()
        findPairs2(arr, sum)
        end = time.perf_counter()
        times2.append(end-start)

        start = time.perf_counter()
        findPairs3(arr, sum)
        end = time.perf_counter()
        times3.append(end-start)

        start = time.perf_counter()
        findPairs4(arr, sum)
        end = time.perf_counter()
        times4.append(end-start)

    # generate dataframe
    df = pd.DataFrame({'n': n, 'times1': times1, 'times2': times2, 'times3': times3, 'times4': times4})
    #save dataframe to excel
    df.to_excel('times.xlsx', index=False)

    # Scatter graph
    scatterGraph(range(1,N+1), times1, 'Function 1', 'Number of data', 'Execution time')
    scatterGraph(range(1,N+1), times2, 'Function 2', 'Number of data', 'Execution time')
    scatterGraph(range(1,N+1), times3, 'Function 3', 'Number of data', 'Execution time')
    scatterGraph(range(1,N+1), times4, 'Function 4', 'Number of data', 'Execution time')



if __name__ == '__main__':
    main()
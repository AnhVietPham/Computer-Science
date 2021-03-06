import sys

MAX = sys.maxsize


def maxBelowSolution(arr, k):
    maxBelow = 0
    minDistance = MAX
    for i in range(0, len(arr)):
        if (0 < arr[k] - arr[i]) and (arr[k] - arr[i] < minDistance):
            minDistance = arr[k] - arr[i]
            maxBelow = arr[i]
    return maxBelow


def maxBelowSolution2(arr, k):
    maxBelow = 0
    for i in range(0, len(arr)):
        if arr[i] < arr[k]:
            maxBelow = arr[i] if maxBelow < arr[i] else maxBelow
    return maxBelow


if __name__ == '__main__':
    arrNumber = [5, 3, 6, 4, 8, 11]
    print(MAX)
    print(maxBelowSolution(arrNumber, 5))
    print(maxBelowSolution2(arrNumber,5))

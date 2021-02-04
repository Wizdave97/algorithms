import random

file = open('integers.txt', 'r')
arr = []

for line in file:
    line = line.lstrip().rstrip().rstrip('\n')
    arr.append(int(line))
file.close()

def choosePivot(start, end):
    return random.randint(start, end)
def partition(arr, start, end, pIndex):
    pivot = arr[pIndex]
    endEl = arr[end]
    arr[end] = pivot
    arr[pIndex] = endEl
    i = start
    for curr in range(start, end):
        if(arr[curr] <= pivot):
            currEL = arr[curr]
            currBoundaryEl = arr[i]
            arr[i] = currEL
            arr[curr] = currBoundaryEl
            i+=1
    boundaryEl = arr[i]
    arr[i] = pivot
    arr[end] = boundaryEl
    return i



def quickSort(arr, start, end):
    if start == end:
        return
    if start == end + 1:
        return
    pivot  = choosePivot(start, end)
    final_index = partition(arr, start, end, pivot)
    quickSort(arr, start, final_index - 1)
    quickSort(arr, final_index + 1, end)

quickSort(arr, 0, len(arr) - 1)
print(arr)
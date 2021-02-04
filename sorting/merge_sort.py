from math import floor

file = open('integers.txt', 'r')
arr = []

for line in file:
    line = line.lstrip().rstrip().rstrip('\n')
    arr.append(int(line))
file.close()

def merge(arr, start, mid, end):
    lp = 0
    rp = 0
    k = start
    lCopy = arr[start : mid + 1]
    rCopy = arr[mid + 1 : end + 1]
    n1 = (mid + 1) - start
    n2 = (end + 1) - (mid + 1)
    while lp < n1 and rp < n2:
        if lCopy[lp] <= rCopy[rp]:
            arr[k] = lCopy[lp]
            k+=1
            lp+=1
        else:
            arr[k] = rCopy[rp]
            k+=1
            rp+=1
    while lp < n1:
        arr[k] = lCopy[lp]
        k+=1
        lp+=1
    while rp < n2:
        arr[k] = rCopy[rp]
        k+=1
        rp+=1

def merge_sort(arr, start, end):
    if start >= end:
        return
    mid = floor(start + (end - start) / 2)
    merge_sort(arr, start, mid)
    merge_sort(arr, mid + 1, end)
    merge(arr, start, mid, end)

merge_sort(arr, 0, len(arr) - 1)
print(arr)
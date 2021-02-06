from math import floor

file = open('integers.txt', 'r')
arr = []

for line in file:
    line = line.lstrip().rstrip().rstrip('\n')
    arr.append(int(line))
file.close()

def insert(arr, val, heap_size):
    arr[heap_size + 1] = val
    i = heap_size + 1
    while i >= 1:
        parentIndex = floor(i / 2)
        if parentIndex >= 1 and arr[parentIndex] > val:
            parentVal = arr[parentIndex]
            arr[parentIndex] = val
            arr[i] = parentVal
        else:
            break
        i = parentIndex
            
def heap_delete_min(arr, heap_size):
    min = arr[1]
    lastEl = arr[heap_size]
    arr[1] = lastEl
    i = 1
    while i < heap_size:
        lci = 2 * i
        rci = (2 * i) + 1
        if lci > (heap_size - 1):
            break
        elif lci <= (heap_size - 1) and rci > (heap_size - 1):
            if(arr[i] > arr[lci]):
                leftChild = arr[lci]
                curr = arr[i]
                arr[i] = leftChild
                arr[lci] = curr
                i = lci
            else:
                break
        elif rci <= (heap_size - 1) and lci <= (heap_size - 1):
            smallest = lci if arr[lci] < arr[rci] else rci
            if (arr[i] > arr[lci]) or (arr[i] > arr[rci]):
                child = arr[smallest]
                el = arr[i]
                arr[smallest] = el
                arr[i] = child
                i = smallest
            else:
                break
        else:
            break
    return min

def heap_sort(arr):
    n = len(arr)
    heap = [None for i in range(n + 1)]
    heap_size = 0
    for i in range(0, n):
        insert(heap, arr[i], heap_size)
        heap_size+=1
    for i in range(0, n):
        min = heap_delete_min(heap, heap_size)
        arr[i] = min
        heap_size-=1

heap_sort(arr)
print(arr)

#Build the heap data structure(Max heap)
def build_heap(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    #Perform swaps to maintain the heap property when building the heap
    if left < n and arr[left] > arr[largest]:
        largest = left

    if right < n and arr[right] > arr[largest]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        build_heap(arr,n,largest)

def heapSort(arr) -> list :
    n = len(arr)

    for i in range(n//2-1,-1,-1):
        build_heap(arr, n, i)

    for i in range(n-1,0,-1):
        arr[i], arr[0] = arr[0], arr[i]
        build_heap(arr, i , 0)

    return arr



if __name__ == "__main__":
    arr = [4,10,3,5,1]
    heapSort(arr)
    print(arr)


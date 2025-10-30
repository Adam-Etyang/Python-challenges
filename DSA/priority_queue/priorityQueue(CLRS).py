# This is based on the CLRS implementation of the Max priorityQueue
# Note that it uses 1 based indexing


class MaxpriorityQueue:
    def __init__(self, arr=None):
        if arr is None:
            arr = []
        self.A = [None] + list(arr)
        self.heapSize = len(arr)
        if self.heapSize:
            self.buildHeap()

    # Helper functions
    def left(self, i):
        return 2 * i

    def right(self, i):
        return 2 * i + 1

    def parent(self, i):
        return i // 2

    def MaxHeapify(self, i):
        """
        Method that helps to maintain the max heap property
        Looks at the node i and compares it to its 2 children: right and left
        if i is not the largest then swap i with either of the larger items and recursively call the function to te rest of its children
        """
        n = self.heapSize
        left = self.left(i)
        right = self.right(i)
        largest = i

        if left <= n and self.A[left] > self.A[largest]:
            largest = left
        if right <= n and self.A[right] > self.A[largest]:
            largest = right
        if largest != i:
            self.A[i], self.A[largest] = self.A[largest], self.A[i]
            self.MaxHeapify(largest)

    def extractMax(self):
        """Remove and return the maximum (the root of the heap)
        Similar to the heapsort procedure
        """
        if self.heapSize < 1:
            raise IndexError("heap underflow")
        maximum = self.A[0]
        self.A[0] = self.A[self.heapSize]
        self.A.pop()
        self.heapSize -= 1
        if self.heapSize >= 0:
            self.MaxHeapify(1)
        return maximum

    def increase_Key(self, i, key):
        """Increate A[i] to key. Must satisfy the property key >= A[i]
        Update the key element A[i] to its new value,
        Traverses a simple path from the noew to the root to find a proper place for the newly increased key.
        As the key traverses the path it repeatedly compares an element to its parent exchanging theur keys and continuing if the element's keys is larger and terminating the element key is smaller since the max heap property holds.
        """
        if i < 1 or i > self.heapSize:
            raise IndexError("Index out of range")
        if key < self.A[i]:
            raise ValueError("The new key is smaller than the current key")

        self.A[i] = key
        # Bubble up the new value
        while i > 1 and self.A[self.parent(i)] < self.A[i]:
            p = self.parent(i)
            self.A[i], self.A[p] = self.A[p], self.A[i]
            i = p

    def insertMax(self, key):
        """Insert key into the heap
        Expands the max heap by adding to the tree w a new leaf whose key is -infinity,
        Then calls the Heap_increase_key to set the key of the new node to its correct value and maintain the heap property
        """

        neg_inf = -float("inf")
        self.A.append(neg_inf)
        self.heapSize += 1
        self.increase_Key(self.heapSize, key)

    def buildHeap(self):
        """Turns an array into a max heap in O(n) time"""
        for i in range(self.heapSize // 2, 0, -1):
            self.MaxHeapify(i)

    def to_list(self):
        """
        Return heap contents as a list
        """
        return self.A[1:].copy()


if __name__ == "__main__":
    pass

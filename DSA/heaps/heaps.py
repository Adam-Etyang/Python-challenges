class Heap:
    """MAX HEAP"""

    def __init__(self):
        self.heap = []

    def parent(self, i):
        """Parent node"""
        return (i - 1) // 2

    def left(self, i):
        """Left element of the node"""
        return 2 * i + 1

    def right(self, i):
        """Right element of the node"""
        return (2 * i) + 2

    # inserting values into the heap array but the heap property must hold true
    def insert(self, key):
        """Insert a value into the heap while
        maintaining the maz heap property"""
        self.heap.append(key)
        i = len(self.heap) - 1

        # bubble up the value being inserted
        while i > 0 and self.heap[self.parent(i)] < self.heap[i]:
            self.heap[i], self.heap[self.parent(i)] = (
                self.heap[self.parent(i)],
                self.heap[i],
            )
            i = self.parent(i)

    # function that helps to maintain the heap property
    def max_heapify(self, i):
        n = len(self.heap)
        l = self.left(i)
        r = self.right(i)
        largest = i

        if l <= n and self.heap[l] > self.heap[largest]:
            largest = l
        if r <= n and self.heap[r] > self.heap[largest]:
            largest = r

        if largest != i:
            self.heap[i], self.heap[largest] = self.heap[largest], self.heap[i]
            self.max_heapify(largest)

    # build a max heap from a given array
    def build_heap(self, A):
        self.heap = A
        n = len(self.heap)

        for i in range(n // 2 - 1, -1, -1):
            self.max_heapify(i)

    def get_max(self):
        return self.heap[0] if self.heap else None


if __name__ == "__main__":
    h = Heap()
    h.insert(3)
    h.insert(4)
    h.insert(7)
    h.insert(8)
    print(f"Heap array: {h.heap}")

    arr = [3, 7, 4, 1, 6, 8, 9]
    h.build_heap(arr)
    print(f"Heap from array: {h.heap}")

    print(f"Max Item: {h.get_max()}")

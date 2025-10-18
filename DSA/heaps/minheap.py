class MinHeap:
    def __init__(self):
        self.heap = []

    def parent(self, i):
        """Parent node"""
        return (i - 1) // 2

    def left(self, i):
        """Left node"""
        return 2*i + 1

    def right(self, i):
        """Right node"""
        return 2*i + 2

    def min_heapify(self, i):
        """Maintaining the heap property"""
        r = self.right(i)
        l = self.left(i)
        n = len(self.heap)
        smallest = i 

        if r < n and self.heap[r] < self.heap[smallest]:
            smallest = r
        if l < n and self.heap[l] < self.heap[smallest]:
            smallest = l
        if smallest != i:
            self.heap[i], self.heap[smallest] = self.heap[smallest], self.heap[i]
            self.min_heapify(smallest)

    def insert(self, key):
        """Inserting an element"""
        self.heap.append(key)
        i = len(self.heap) - 1

        while i > 0 and self.heap[self.parent(i)] > self.heap[i]:
            self.heap[i],self.heap[self.parent(i)] = self.heap[self.parent(i)],self.heap[i]
            i = self.parent(i)

    def build_heap(self,arr):
        self.heap = arr
        n = len(arr)

        for i in range((n // 2)-1, -1, -1):
            self.min_heapify(i)

    def get_min(self):
        return self.heap[0] if self.heap else None

if __name__ == "__main__":
    h = MinHeap()
    h.insert(5)
    h.insert(3)
    h.insert(8)
    h.insert(1)
    print(h.heap)  # Output: [1, 3, 8, 5] or similar

    arr = [9, 4, 7, 1, -2, 6, 5]
    h.build_heap(arr)
    print(h.heap)  # Output: [-2, 1, 5, 4, 9, 6, 7]
    print(h.get_min())  # Output: -2

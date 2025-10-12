class Heap:
    def __init__(self):
        self.heap = []

    def parent(self, i ):
        return (i - 1)//2

    def  left(self,i):
        return 2*i +1

    def right(self,i):
        return (2 * i) +2

    #function that helps to maintain the heap property
    def max_heapify(self,i):
        n = len(self.heap)
        l = self.left(i)
        r = self.right(i)
        largest  = i 

        if l <= n and self.heap(l) > self.heap(i):
            largest = l
        if r <= n and self.heap(r) > self.heap(i):
            largest = r

        if largest != i :
            self.heap[i], self.heap[largest] = self.heap[largest], self.heap[i]
            self.max_heapify(largest)

    def build_heap(self,A):
        pass


if __name__ == "__main__":
    pass


# Priority Queues
A priority queue is a data structure for maintaining a set S of elements, each with an associated value called a key ~ from CLRS.
A priority queue is an abstract data type like a queue but instead of elements coming out in the order they were added (FIFO) the come iut by priority.
Just like heaps there are two types:
- Max priority queue, the highest priority elements is removed first
- Min priority queue, the lowest priority element is removed first.

Each can be built by their corresponding heaps
The max priority queue supports the following operations:
```
Insert(S, x) //inserts the element x into the set S, which is equivalent to the operation S = S \union {X}
Maximum(S) returns the element of S with the largest key.
Extract-Max(s) removes and retunrns the element of S with the largest key
Increase-Key(S,x ,k) Increases the value of the element x's key to the new value k, which is assumed to be at as large as x'x current key value.
```
Max-priority queues are used to schedule jobs on a shared computer. It keeps track of the jobs to be performed and their relative priorities

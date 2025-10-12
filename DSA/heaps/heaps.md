# Heaps
The heap data structure is an array object that can be viewed a s nearly complete binary tree. Each node of the tree corresponsds to an element of the array. The tree is completely filled on all level except the lowest which is filled from the left up to a point.
The root of the tree is A(the array)[1] and given the index $i$ of the node we can easily computer the indices of its parent, left child and right child:

$$
Parent(i)
return \lfloor i/2 \rfloor
$$

$$
left(i)
return 2i
$$

$$
right(i)
return 2i + 1
$$
There are two types of heaps:
- Max heap, every parent node is greater than or equal to its children -> *Max heap property*
- Min heap, every parent node is less than or equal to its children -> *Min heap property*


Heaps are implemented as binary trees but stored as an array
```
Heap as tree:             Stored as array:
     20                     [20, 15, 10, 7, 9, 5]
    /  \
   15    10
  /  \   /
 7   9  5
 ```
 We can access any element of the heaps using index arithmetic so no extra memory is needed for the heap 
 ```


```

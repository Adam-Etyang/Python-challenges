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


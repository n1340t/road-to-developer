We can evaluate the condition (if) first then add/remove element later. It isn't necessary to add/remove element then do if check (Inversion of Control) 
Example: building smallest integer from string  by removing digits problem

### General strategy when solve coding question
 - Solve trival case first (Ex: 1,2,3,4,5), get the solution
 - Solve next case, get the solution
 - Repeat until all cases are clear
 - Optimize solution 

A lot problems are based on properties and characteristic trivial result. Like an ordered list. For example, [0,3,5,7,11,12]. [0,3] [5,7] [11,12] can be think of time interval and the question is that can we attend all intervals? The technique: try to SORT first O(nlogn)

If we want to find element in array, think of binary search first because it's fastest O(log n)

Important mindset when working with recursive algorithm (usually tree algo):
- The actual execuation starts at the end of tree (stack)

### Binary Tree technique
1. inOrder, preOrder, postOrder (recursion)
2. Level Order: using queue to implement.

### Recursion problems
- If you think a problem is a recursive type, express it as **recurrence relation**
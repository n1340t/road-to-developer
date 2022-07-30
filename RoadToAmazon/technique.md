We can evaluate the condition (if) first then add/remove element later. It isn't necessary to add/remove element then do if check (Inversion of Control) 
Example: building smallest integer from string  by removing digits problem

### General strategy when solve coding question
 - Solve trival case first (Ex: 1,2,3,4,5), get the solution
 - Solve next case, get the solution
 - Repeat until all cases are clear
 - Optimize solution 

A lot problems are based on properties and characteristic trivial result. Like an ordered list. For example, [0,3,5,7,11,12]. [0,3] [5,7] [11,12] can be think of time interval and the question is that can we attend all intervals? The technique: try to SORT first O(nlogn)
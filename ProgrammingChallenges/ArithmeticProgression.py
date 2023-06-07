'''
1.) Sort list.  
2.) calculates the difference between the first two elements in the arr.
3.) It then uses a list comprehension and the all() function to iterate over the elements of the list starting from the third element (index 2).
For each element at index i, it checks if the difference between the current element and the previous element is equal to the calculated difference diff. 

 Complexity
- Time complexity:
    Time complexity: O(NlogN) because of sorting 
- Space complexity:
     Space complexity: O(1) using constant space 
'''

class Solution:
    
    def make_arithmetic_progression(self, arry):
        a = sorted(arry)
        diff = a[1] - a[0]
        return all(a[i] - a[i-1] == diff for i in range(2, len(a)))
    

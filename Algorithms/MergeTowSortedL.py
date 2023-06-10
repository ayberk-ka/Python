''' 
    Merge Two Sorted Linked Lists
    -----------------------------
    
    1- p and q, pointing to the heads of the two sorted linked lists.
    2- Check if either p or q is None. 
       If one of them is None, return the other list since there is no need to perform any merging.
    3- new_head will smaller value between p and q. 
        Move the corresponding pointer (p or q) to the next node.
    4- Set a temporary pointer s to new_head. 
        This pointer will be used to traverse the merged list and add nodes to it.
    5- While both p and q are not None, compare their data values. 
        Append the node with the smaller value to s.next, update s to point to the newly added node
        and move the corresponding pointer to the next node.  
    6- After the while loop ends, append the remaining nodes of the non-empty list (p or q) to s.next.  
    7- Finally, return new_head, which is the head of the merged list.
    
    '''


class Node:
    def __init__(self, data):
        
        self.data = data
        self.next=None
        
        
        
class LinkedList:
    def __init__(self):
        
        self.head = None

    def append(self, data):
        
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node 
        
    
    def print_list(self):
        
        cour_node = self.head
        while cour_node:
            print(cour_node.data)
            cour_node = cour_node.next
    
    
    def merge_two_Sorted_list(self,llist):
        p = self.head           # pointer for the linkedlist
        q = llist.head          # pointer for the second linkedlist
        
        if not p: return q      # If the first linkedlist is empty return the second linkedlist
        if not q: return p
        
        new_head = None         # Head of the merged list
        
        # Determine the head of the merged list by comparing the first nodes of the two lists
        if p.data <= q.data:    
            new_head = p        
            p = p.next          
        else:
            new_head = q 
            q = q.next
        
        s = new_head            # Pointer for the merged list
        while p and q:
            if p.data <= q.data:
                s.next = p      # Append the node of the first list to the merged list
                s = p           # Move the pointer of the merged list to the appended node
                p = p.next      # Move the pointer of the first list to the next node
            else:
                s.next = q
                s = q
                q = q.next 
        # Append the remaining nodes of the non-empty list to the merged list
        if not p:              
            s.next = q
        if not q:
            s.next = p
        return new_head         # Return the head of the merged list

# First sorted linked list: 1 -> 3 -> 7    
list1 = LinkedList()
list1.append(1)
list1.append(3)
list1.append(7)

# Second sorted linked list: 2 -> 5 -> 8 -> 9
list2 = LinkedList()
list2.append(2)
list2.append(5)
list2.append(8)
list2.append(9)

# Merge the two sorted linked lists
list1.merge_two_Sorted_list(list2)

# Print
list1.print_list()

# Merged List: 1 -> 2 -> 3 -> 5 -> 7 -> 8 -> 9
                
                
        
        
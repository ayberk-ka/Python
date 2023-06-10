'''
Remove Duplicates

1- Initialize variables cur with the head of the linked list and prev as None.

2- Initialize an empty dictionary dup_values to track encountered values.

3- Iterate through the linked list while cur is not None:

    Check if the data of cur exists in dup_values.

    If it does, remove the duplicate node by updating the next reference of prev to skip cur. Set cur to None.

    If it doesn't, add the data as a key to dup_values with a value of 1.

    Update prev to cur.

    Update cur to the next node using cur = prev.next.

4- The linked list now contains no duplicate nodes.
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
        
        
    def remove_duplicates(self):
        cur = self.head
        prev = None
        dup_values = dict()
        
        while cur:
            if cur.data in dup_values:
                # Remove Node.
                prev.next = cur.next 
                cur = None
            else:
                # Add the data as a key to dup_values with a value of 1.
                dup_values[cur.data] = 1
                prev = cur
            cur = prev.next
        
    
    def print_list(self):
        
        cour_node = self.head
        while cour_node:
            print(cour_node.data)
            cour_node = cour_node.next
            
llist = LinkedList()
llist.append(1)
llist.append(2)
llist.append(2)
llist.append(1)
llist.append(3)
llist.remove_duplicates()
llist.print_list()
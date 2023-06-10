class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def print_list(self):
        cur_node = self.head
        while cur_node:
            print(cur_node.data)
            cur_node = cur_node.next

    def append(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node
        

    '''
    
    '''
    def move_tail_to_head(self):
        
        tail = self.head
        prev = None

        # Traverse the list to find the tail and the second-to-last node
        while tail.next:
            prev = tail
            tail = tail.next

        # Move the tail node to the head
        tail.next = self.head
        self.head = tail

        # Set the next attribute of the previous node to None
        prev.next = None
    
    
    
llist_2 = LinkedList()
llist_2.append("A")
llist_2.append("B")
llist_2.append("C")
llist_2.append("D")
llist_2.append("E")

llist_2.move_tail_to_head()
llist_2.print_list()
# Original:     A -> B -> C -> D -> E
# Updated:      E -> A -> B -> C -> D 

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def print_list(self):
        if self.head is None:
            print("Linked list is empty.")
            return

        cur_node = self.head
        while cur_node:
            print(cur_node.data, end=" ")
            cur_node = cur_node.next
        print()

    def append(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node
        
    def reverse_list(self):
        cur = self.head
        prev = None
        next_node = None
        
        while cur:
            next_node = cur.next
            cur.next = prev
            prev = cur
            cur = next_node
        self.head = prev
        return self
    
    
    def sum_two_list(self, list2):
        p = self.head
        q = list2.head
        sum_list = LinkedList()
        carry = 0
        
        while p or q:
            
            # Get the value of the current node in linkedlists, or 0 if p, q is None
            i = p.data if p else 0
            j = q.data if q else 0
            
            # Compute the sum of the current nodes' values and the carry
            s = i + j + carry
            
            carry = s // 10
            remainder = s % 10
            
            # Append remainder to sum_list
            sum_list.append(remainder)
            
            # Move p and q to the next node
            if p:
                p = p.next
            if q:
                q = q.next
        # If there is a remaining carry append the sum_llist       
        if carry:
            sum_list.append(carry)
            
        return sum_list
    
list1 = LinkedList()
list1.append(9)
list1.append(9)
list1.append(9)


list2 = LinkedList()
list2.append(9)
list2.append(9)
list2.append(9)


sum_list = list1.sum_two_list(list2)
sum_list.reverse_list()
print("Sum of two lists: ")
sum_list.print_list()
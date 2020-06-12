import time

start_time = time.time()

class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node
        
    def get_value(self):
        return self.value
    
    def get_next_node(self):
        return self.next_node
    
    def set_next_node(self, new_next):
        self.next_node = new_next

class LinkedList: 
    def __init__(self):
        self.head = None
        self.tail = None
    
    def insert(self, value):
        new_node = Node(value, None)
        
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.set_next_node(new_node)
            self.tail = new_node
            
    def setList(self, arr):
        for i in range(len(arr)):
            self.insert(arr[i])  
    
    def display(self):
        if not self.head:
            return None
        else:
            current = self.head
            next_curr = current.next_node
            curr_list = []
            while current.next_node is not None:
                curr_list.append(current.value)
                current = current.next_node
        return curr_list
    
    
end_time = time.time()
print (f"LinkedList runtime: {end_time - start_time} seconds")



class Node:
    def __init__(self, value, next_node):
        self.value = value 
        self.next_node = next_node
    
    def get_value(self):
        return self.value

    def get_next_node(self):
        return self.next_node
    
    def set_next_node(self, new_node):
        self.next_node = new_node
        
class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.head = None
        self.tail = None
        self.length = 0

    # def len(self):
    #     count = 0
    #     current_head = self.head
    #     while(current_head):
    #         count += 1
    #         current_head = current_head.next_node
    #     return count

    def append(self, item):
        new_node = Node(item, None);
        
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            if(self.length <= self.capacity):
                self.length += 1
                self.tail.set_next_node(new_node)
                self.tail = new_node
            else:
                pass

    def get(self):
        if not self.head:
            return None
        else:
            current = self.head
            curr_list = []
            while current:
                curr_list.append(current.value)
                current = current.next_node
        return curr_list
    
    


a = RingBuffer(3);
a.append(1)
a.append(2)
a.append(3)
a.append(4)
a.append(5)
a.append(6)

print(a.get())
    

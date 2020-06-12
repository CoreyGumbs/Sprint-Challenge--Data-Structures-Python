
        
class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.storage =  [None]*capacity
        self.count = 0
        
    def append(self, item):    
        self.storage[self.count] = item
        self.count += 1
        
        if self.count == self.capacity:
            self.count = 0
    
    def get(self):
        return self.storage
 
    

class Queue:
    def __init__(self):
        self.queue = list()
    
    def Print(self):
        return print(self.queue)
        
    def enqueue(self,element):
        self.queue.insert(0,element)
          
    def dequeue(self):
        return print(self.queue.pop())
        

# For testing the class 
# l = Queue()
# l.enqueue(3)
# l.enqueue(67)
# l.enqueue(322)
# l.enqueue(627)
# l.enqueue(32)
# l.enqueue(64)
# l.Print()
# l.dequeue()
# l.dequeue()
# l.dequeue()
# l.Print()



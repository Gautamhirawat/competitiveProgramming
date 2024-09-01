class Node:
    def __init__(self,new_data) -> None:
        self.data = new_data
        self.next = None


class queue:

    def __init__(self) -> None:
        self.front = None 
        self.rear = None

    def empty(self):
        return self.front is None and self.rear is None
    
    def enque(self,new_data):
        new_node = Node(new_data)

        if self.rear is None:
            self.front = self.rear = new_node

        self.rear.next = new_node
        self.rear = new_node

    def deque(self):
        if self.empty():
            print("queue is empty")
            return
        
        temp = self.front
        self.front = self.front.next

        if self.front is None:
            self.rear = None

    def get_front(self):
        if self.empty():
            print("queue is empty")
            return float('-inf')
        
        return self.front.data
    
    def get_rear(self):
        if self.empty():
            print("queue is empty")
            return float('-inf')
        
        return self.rear.data



if __name__ == "__main__":
    q = queue()

    # Enqueue elements into the queue
    q.enque(10)
    q.enque(20)

    # Display the front and rear elements of the queue
    print("Queue Front:", q.get_front())
    print("Queue Rear:", q.get_rear())

    # Dequeue elements from the queue
    q.deque()
    q.deque()

    # Enqueue more elements into the queue
    q.enque(30)
    q.enque(40)
    q.enque(50)

    # Dequeue an element from the queue
    q.deque()

    # Display the front and rear elements of the queue
    print("Queue Front:", q.get_front())
    print("Queue Rear:", q.get_rear())

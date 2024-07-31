class Node:
    def __init__(self, data = None , next = None):
        self.data = data
        self.next = next



class singly:
    def __init__(self):
        self.head = None

    def insert_at_begining(self,data):
        node = Node(data,self.head)
        self.head = node

    def insert_at_end(self,data):
        if self.head is None:
            self.head = Node(data, None)
            return
        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = Node(data , None)

    def insert_values(self,data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)

    def get_length(self):
        count = 0 
        itr = self.head
        while itr:
            count+=1
            itr = itr.next

        return count
    
    def remove_at(self,index):
        if index < 0 or index >= self.get_length():
            raise Exception("Invalid Index")
        
        if index == 0:
            self.head = self.head.next
            return
        
        count = 0
        itr = self.head

        while itr:
            if count == index-1:
                itr.next = itr.next.next
                break

            itr = itr.next
            count+=1

    def insert_at(self,index,data):
        if index < 0 or index >= self.get_length():
            raise Exception("Invalid Index")
        
        if index == 0:
            self.insert_at_begining(data)
            return
        
        count = 0 
        itr = self.head
        while itr:
            if count == index -1:
                node = Node(data , itr.next)
                itr.next = node
                break
            itr = itr.next
            count+=1

    def Print(self):
        if self.head is None:
            print("linked list is empty")
            return
        itr = self.head
        llstr = ''

        while itr:
            llstr += str(itr.data) + ' -->'
            itr = itr.next

        print(llstr)

# ----------------------------------------------------
# TESTING AREA 

# Make a new file text.py and make sure this linkedList.py in same directory
"""

import linkedList

ll = linkedList.singly()
ll.insert_at_begining(7)
ll.Print()

"""

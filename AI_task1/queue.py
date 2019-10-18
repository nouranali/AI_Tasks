class queue:
    def __init__(self):
        self.items=[]
    #is_empty function 
    def is_Empty(self):
        return self.items==[]
    #inserting elements in the queue at index 0
    def enqueue(self,item):
        self.items.insert(0,item)
    #getting elements out of the queue    
    def dequeue(self):
       return self.items.pop()    
    #Get the queue size aka number of elements currently in it
    def size(self):
        return len(self.items)

##using the queue
q= queue()
q.enqueue(5)
q.enqueue(10)
q.enqueue(15)
print("Is the queue empty?",q.is_Empty())        
print("Queue size = " ,q.size())
print("dequeued item",q.dequeue())
print("Queue size = " ,q.size())


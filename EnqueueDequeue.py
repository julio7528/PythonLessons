import os
os.system('cls')

#Enqueue and Dequeue
class queue:
    def __init__(self):
        self.queue = []
    def enqueue(self, item):
        self.queue.append(item)
    def dequeue(self):
        if len(self.queue) > 0:
            return self.queue.pop(0)
        else:
            return None
    def size(self):
        return len(self.queue)

q = queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
print(q.size())
q.dequeue()
q.dequeue()
print(q.size())
print(q.queue)
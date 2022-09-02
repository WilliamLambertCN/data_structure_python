# Bradley N. Miller, David L. Ranum
# Introduction to Data Structures and Algorithms in Python
# Copyright 2005
# 
#queue.py

class Queue:
    def __init__(self,items=[]):
        self.items = items

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        return self.items.pop(0)

    def size(self):
        return len(self.items)
    
    def __str__(self):
        return str(self.items)

if __name__=="__main__":
    s = Queue([1,2,3,4])
    print(s)
    s.enqueue(5)
    print(s)

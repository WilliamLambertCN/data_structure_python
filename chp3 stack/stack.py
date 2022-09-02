class Stack:
    def __init__(self,items=[]):
        self.items = items

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        return self.items.pop()
    
    def peek(self):
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)

    def __str__(self):
        return str(self.items)

if __name__=="__main__":
    s = Stack([1,2,3,4])
    print(s)

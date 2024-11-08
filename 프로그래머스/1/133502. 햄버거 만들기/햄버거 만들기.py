class Stack:
    def __init__(self):
        self.list = []

    def insert(self, data):
        self.list.append(data)

    def pops(self):
        if not self.is_empty(): 
            return self.list.pop()
        return None

    def last(self):
        if not self.is_empty():
            return self.list[-1]
        return None

    def is_empty(self):
        return len(self.list) == 0

def solution(arr):
    a = Stack()
    burger_count = 0
    
    for item in arr:
        a.insert(item)
        
        if len(a.list) >= 4 and a.list[-4:] == [1, 2, 3, 1]:
            burger_count += 1
            for _ in range(4):
                a.pops()
    
    return burger_count

class Node:
    def __init__(self, data):
    self.data = data 
    self.next = None 
    self.prev = None
 

class List:
    def __init__(self): 
    self.head = Node(None)
    self.head.next = self.head
    self.head.prev = self.head
    self.n = 0  


 def get(self,ind):
    if ind >= self.size() : 
        raise Exception('Out of list')
    x = self.head.next
    for i in range(ind) :
        x=x.next
    return x  


 def insert_after(self, x, data):
    y = Node(data)
    self.n += 1
    y.prev = x
    y.next = x.next
    x.next = y
    y.next.prev = y
    return y 


 def delete(self, x):
    if self.size()==0:
        raise Exception('List is empty')
    self.n -= 1
        x.prev.next = x.next
        x.next.prev = x.prev
    return x  


 def find(self, val):
    x = self.head.next
    for i in range(self.size()) :
        if x.data == val :
    return x
        x=x.next
    return  none  

 def size(self):
    return self.n  

 def is_empty(self):
    return self.n==0 


def multiply_polynomials(poly1, poly2):
    result = [0] * (len(poly1) + len(poly2) - 1)
    for i in range(len(poly1)):
        for j in range(len(poly2)):
            result[i + j] += poly1[i] * poly2[j] 
            
    return result  


def sum_polynomials(poly1, poly2):
    result = []
    max_len = max(len(poly1), len(poly2))
    poly1 += [0] * (max_len - len(poly1))
    poly2 += [0] * (max_len - len(poly2)) 

    for i in range(max_len):
        result.append(poly1[i] + poly2[i])  

    return result 



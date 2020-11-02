class Queue:
    def __init__(self):
        self.items =[]
    def enQueue(self,item):
        self.items.append(item)
    def deQueue(self):
        return self.items.pop(0)
    def isEmpty(self):
        return self.items == []
    def size(self):
        return len(self.items)

x,y=input('Enter Input : ').split('/')
a=x.split()
b=y.split(',')
q=Queue()
for i in range(len(a)):
    q.enQueue(a[i])
for i in range(len(b)):
    b[i]=b[i].split()
for j in b:
    if j[0]=='E':
        q.enQueue(j[1])
    elif j[0]=='D':
        if not q.isEmpty():
            q.deQueue()
q_set=set(q.items)
if len(q_set) != len(q.items):
    print('Duplicate')
else:
    print('NO Duplicate')
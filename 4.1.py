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

x=input('Enter Input : ').split(',')
q=Queue()
deq=Queue()
for i in range(len(x)):
    x[i]=x[i].split()       
for j in x:
    if j[0]=='E':
        q.enQueue(j[1])
        for k in range(len(q.items)):
            print(q.items[k],end='')
            if(k != len(q.items)-1):
                print(', ',end='')
        print('')
    elif j[0]=='D':
        if not q.isEmpty():
            deq.enQueue(q.items[0])
            print(q.deQueue() ,'<- ',end='')
            if not q.isEmpty():
                for k in range(len(q.items)):
                    print(q.items[k],end='')
                    if(k != len(q.items)-1):
                        print(', ',end='')
                print('')
            else:
                print('Empty')
        else:
            print('Empty')
if not deq.isEmpty():
    for v in range(len(deq.items)):
        print(deq.items[v],end='')
        if(v != len(deq.items)-1):
            print(', ',end='')
else:
    print('Empty',end='')
print(' : ',end='')
if not q.isEmpty():
    for u in range(len(q.items)):
        print(q.items[u],end='')
        if(u != len(q.items)-1):
            print(', ',end='')
else:
    print('Empty')
  
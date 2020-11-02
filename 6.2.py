class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.previous = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __str__(self):
        if self.isEmpty():
            return "Empty"
        cur, s = self.head, str(self.head.value) + " "
        while cur.next != None:
            s += str(cur.next.value) + " "
            cur = cur.next
        return s

    def reverse(self):
        if self.isEmpty():
            return "Empty"
        cur, s = self.tail, str(self.tail.value) + " "
        while cur.previous != None:
            s += str(cur.previous.value) + " "
            cur = cur.previous
        return s

    def isEmpty(self):
        return self.head == None

    def append(self, item):
        if self.head is None:
            new_node = Node(item)
            self.head = new_node
            return
        n = self.head
        while n.next is not None:
            n = n.next
        new_node = Node(data)
        n.next = new_node
        new_node.previous = n
        
    def addHead(self, item):
        newNode = Node(item)
        newNode.next = self.head
        self.head = newNode

    def insert(self, pos, item):
        count=0   
        if self.head is None or pos-1==0:
            self.addHead(item)
        elif pos-1 <= self.size() and pos-1 > 0:
            cur=self.head
            if count==pos-1:
                new_node = Node(item)
                new_node.next = cur
                new_node.previous = cur.previous
            else:
                count+=1
                cur=cur.next
        elif pos-1<0 and abs(pos)<=self.size():
            cur=self.tail
            if count==pos:
                new_node = Node(item)
                new_node.previous = cur
                new_node.next = cur.next
            else:
                count-=1
                cur=cur.previous
                
    def search(self, item):
        current = self.head
        while current != None :
            if current.data == item :
                return 'Found'
            current = current.next
        if current == None :
            return 'Not Found'
   
    def index(self, item):
        current = self.head
        count = 0
        while current != None :
            if current.data == item :
                return count
            count += 1
            current = current.next
        if current == None :
            return '-1'

    def size(self):
        current = self.head
        count = 0
        while current != None :
            current = current.next
            count += 1
        return count

    def pop(self, item):
        current = self.head
        if item == 0:
            if not self.isEmpty():
                self.head = self.head.next
                return "Success"
            else:
                return "Out of Range"
        else:
            previous = None
            index = 0
            while current is not None:
                if index == item:
                    previous.next = current.next
                    return "Success"
                index += 1
                previous = current
                current = current.next
            return "Out of Range"

L = LinkedList()
inp = input('Enter Input : ').split(',')
for i in inp:
    if i[:2] == "AP":
        L.append(i[3:])
    elif i[:2] == "AH":
        L.addHead(i[3:])
    elif i[:2] == "SE":
        print("{0} {1} in {2}".format(L.search(i[3:]), i[3:], L))
    elif i[:2] == "SI":
        print("Linked List size = {0} : {1}".format(L.size(), L))
    elif i[:2] == "ID":
        print("Index ({0}) = {1} : {2}".format(i[3:], L.index(i[3:]), L))
    elif i[:2] == "PO":
        before = "{}".format(L)
        k = L.pop(int(i[3:]))
        print(("{0} | {1}-> {2}".format(k, before, L)) if k == "Success" else ("{0} | {1}".format(k, L)))
    elif i[:2] == "IS":
        data = i[3:].split()
        L.insert(int(data[0]), data[1])
print("Linked List :", L)
print("Linked List Reverse :", L.reverse())
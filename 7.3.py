class Node:
    def __init__(self, data): 
        self.data = data  
        self.left = None  
        self.right = None 
        self.level = None 

    def __str__(self):
        return str(self.data) 

class BinarySearchTree:
    def __init__(self): 
        self.root = None

    def create(self, val):  
        if self.root == None:
            self.root = Node(val)
        else:
            current = self.root
         
            while True:
                if val < current.data:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        break
                elif val > current.data:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        break
                else:
                    break
                
def printTree90(node, level = 0):
    if node != None:
        printTree90(node.right, level + 1)
        print('     ' * level, node)
        printTree90(node.left, level + 1)

def father(r,data):
    curr=r
    while curr.left != None or curr.right != None:
        if data == r.data:
            return 'None Because'+' '+ data +' '+'is Root'
        elif curr.left==None and curr.right==None:
            return '1Not Found Data'
        elif curr.left == data or curr.right == data:
            return curr.data
        elif data >= curr.data:
            if curr.right != None:
                curr=curr.right
            else:
                if curr.left == None:
                    return '2Not Found Data'        
        elif data < curr.data:
            if curr.left != None:
                curr=curr.left
            else:
                if curr.right == None:
                    return '3Not Found Data'
            
        print(curr,'and',curr.left,'and',curr.right)



tree = BinarySearchTree()
data = input("Enter Input : ").split("/")
for e in data[0].split():
    tree.create(e)
printTree90(tree.root)
print(father(tree.root,data[1]))
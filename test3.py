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

    def insert(self, val):  
        if root == None :
            root = Node(val)
        else :
            cur = root
            state = False
            while not state:
                if cur.val >= val:
                    if cur.left == None:
                        cur.left = Node(val)
                        state = True
                    else :
                        cur = cur.left    
                else :
                    if cur.right == None:
                        cur.right = Node(val)
                        state = True
                    else :
                        cur = cur.right 
        return root
    
    def delete(self,root, val):
        if not root:
            return root
        if val > root.val:
            root.right = self.delete(root.right, val)
        elif val < root.val:
            root.left = self.delete(root.left, val)
        else:
            if not root.right:
                temp = root.left
                root.left = None
                return temp
            if not root.left:
                temp = root.right
                root.right = None
                return temp
            temp = miniValueNadode(root.right)
            root.val = temp.val
            root.right = self.delete(root.right, temp.val)
        root.height = 1 + max(self.getHeight(root.left), self.getHeight(root.right))
        balance = self.getBalance(root)
        if balance > 1 and self.getBalance(root.left) >= 0:
            return self.rotateRight(root)
        if balance < -1 and self.getBalance(root.right) <= 0:
            return self.rotateLeft(root)
        if balance > 1 and self.getBalance(root.left) < 0:
            root.right = self.rotateRight(root.right)
            return self.rotateLeft(root)
        if balance < -1 and self.getBalance(root.right) > 0:
            root.left = self.rotateLeft(root.left)
            return self.rotateRight(root)
        return root
                
def printTree90(node, level = 0):
    if node != None:
        printTree90(node.right, level + 1)
        print('     ' * level, node)
        printTree90(node.left, level + 1)


tree = BinarySearchTree()
data = input("Enter Input : ").split(",")
for inp in data:
    if inp[0] == 'i':
        print ('insert',inp[2])
        tree.insert(inp[2])
        printTree90(tree.root)
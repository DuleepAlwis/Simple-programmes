#Binary search tree implementaion using LinkedList
class node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

class BST:
    def __init__(self):
        self.root=None
        self.left=None
        self.right=None

    def insert(self,i):
        a=node(i)
        if self.root==None:
            self.root=a
        else:
            c=self.root
            t=True
            i=1 #i=1 go to left of the tree , i=0 go to right of the tree
            while t:
                if c.data>a.data:
                    if c.left==None:
                        c.left=a
                        return
                    else:
                        i=1
                else:
                    if c.data<=a.data:
                        if c.right==None:
                            c.right=a
                            return
                        else:
                            i=0
                if i==0:
                    c=c.right
                else:
                    c=c.left
    def search(self,t):
        if t==self.root.data:
            print("Found",t)
        else:
            c=self.root
            found=False
            while(found==False):
                try:
                    if c.data>t:
                        c=c.left
                    else:
                        c=c.right
                except:
                    print("Can't find")
                    return
                try:
                    if c.data==t:
                        print("Found",t)
                        return
                except:
                    print("")
                        
                        
                            
    def preor(self,t):
        if t!=None:
            print(t.data)
            self.preor(t.left)
            self.preor(t.right)

    def posto(self,t):
        if t!=None:
            self.posto(t.left)
            self.posto(t.right)
            print(t.data)

    def inorder(self,t):
        if t!=None:
            self.inorder(t.left)
            print(t.data)
            self.inorder(t.right)

    def count(self,t):
        c=0
        if t!=None:
            return 1+self.count(t.left)+self.count(t.right)
        else:
            return 0

    def height(self,t):
        h=0
        if t!=None:
            return max(self.height(t.left)+1,self.height(t.right)+1)
        else:
            return 0

    def maximum(self,t):
        while t.right!=None:
            t=t.right
        print("Maximum is",t.data)

    def minimum(self,t):
        while t.left!=None:
            t=t.left
        print("Minimum is",t.data)
    
            
            
#a=BST();a.preor(a.root)
        
        

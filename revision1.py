class stack:
    def __init__(self):
        self.l=[]

    def push(self,i):
        self.l.append(i)

    def pop(self):
        return self.l.pop()

    def peek(self):
        return self.l[-1]

    def size(self):
        return len(self.l)

    def isempty(self):
        return self.l==[]

class queue:
    def __init__(self):
        self.l=[]

    def enque(self,i):
        self.l.append(i)

    def deque(self):
        return self.l.pop(0)

    def size(self):
        return len(self.l)

    def isempty(self):
        return self.l==[]

#Queue is implemented from stacks
class queuefstack:
    def __init__(self):
        self.a=stack()
        self.b=stack()
        self.l=0

    def enque(self,i):
        self.a.push(i)
        self.l=self.l+1

    def deque(self):
        self.l=self.l-1
        while not self.a.isempty():
            self.b.push(self.a.pop())

        return self.b.pop()

    def isempty(self):
        return self.l==0

    def size(self):
        return self.l
    
#Singly Linked List
    
class node:
    def __init__(self,data):
        self.data=data
        self.next=None

class LinkedList:           
    def __init__(self):
        self.head=None

    def insert(self,i):
        a=node(i)
        if self.head==None:
            self.head=a
        else:
            c=self.head
            while c.next!=None:
                c=c.next
            c.next=a

    def removel(self):
        c=self.head
        while c.next!=None:
            c=c.next
        c=None

    def removef(self):
        a=self.head
        self.head=a.next

    def search(self,t):
        c=self.head
        while c!=None:
            if c.data==t:
                print(t)
                return True
            else:
                c=c.next

    def remove(self,i):             #Remove from any place
        if self.head.data==i:
            self.removef()
            return
        c=self.head
        while c.next!=None:
            if c.next.data==i:
                c.next=c.next.next
                return
            else:
                c=c.next

        print("Can't find")

    def printl(self):
        c=self.head
        while c!=None:
            print(c.data)
            c=c.next

        print("=================================================")


#Doubly Linked List

class nodes:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.pre=None
        
class DlinkedList:
    def __init__(self):
        self.head=None
        self.tail=None

    def insert(self,i):
        a=nodes(i)
        if self.head==None:
            self.head=a
        else:
            c=self.head
            while c.next!=None:
                c=c.next
            c.next=a
            a.pre=c
        self.tail=a

    def search(self,t):
        c=self.head
        while c!=None:
            if c.data==t:
                print("Found"," ",t)
                return True
            else:
                c=c.next

        print("Can't find")

    def remove(self,i):
        c=self.head
        
        if self.head.data==i:
            c.next.pre=None
            self.head=c.next
            return
        else:
            while c.next!=None:
                if c.next.data==i:
                    c.next=c.next.next
                    if c.next==None:
                        self.tail=c
                    else:
                        c.next.pre=c
                    return
                else:
                    c=c.next
        print("Can't find it")

    def printl(self):
        c=self.head
        while c!=None:
            print(c.data)
            c=c.next
        print("==============================================")

    def printrev(self): #Print reverse order
        c=self.tail
        while c!=None:
            print(c.data)
            c=c.pre
        print("--------------------------------------------------")

                
                
        

    
    

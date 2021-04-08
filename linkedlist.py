class Node:                            #node class creates node
    def __init__(self, data):          #__init__ method is called when an object is created from a class and it allows the class to initialize the attributes of the class.
        self.data = data               #data part of a node
        self.ref = None                #refrence part of a node

class linked_list:
    def __init__(self):                #"self" keyword we access the attributes and methods of the class in python.
        self.head = None               #if head points to None then -> linked list is empty
    
    def printll(self):                 #this function traverse all the nodes and print data part of each node
        if self.head == None:
            print("Linked list is empty")
        else:
            while self.head is not None:
                print(self.head.data, end = ' --> ')
                self.head = self.head.ref
                #print(self.head)
                
    def add_beg(self, data):           #this function addes a node to the begning of the linked list
        new_node = Node(data)          #new node is created using Node class having ref part as null
        new_node.ref = self.head       #ref part of new node now contains whatever ref in head(if head points to null then ref part of newnode becomes null)
        self.head = new_node           #now head points to new node and it contains address of the new node
        
    def add_end(self, data):           #this function adds a node at the end of the list
        new_node = Node(data)          #creating new node using Node class having ref part as null
        
        if self.head is None:          #if list is empty then
            self.head = new_node       #new node becomes the first node and head points to it
        else:
            tmp = self.head            #storing head value into a tmp variable and tmp.ref conatins the ref part of the respective node tmp is pointing
            while tmp.ref is not None: #loop stops when tmp.ref = None which is the last node
                tmp = tmp.ref          #update tmp to reach the last node
            tmp.ref = new_node         #if we reaches the last node then tmp.ref now points the new_node
            
        
LL1 = linked_list()    #creating object of linked_list class
LL1.add_beg(100)
LL1.add_beg(200)
LL1.add_beg(300)
LL1.add_end(500)
LL1.printll()

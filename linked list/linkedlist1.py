class node:
    def __init__(self,data):
        self.data=data
        self.ref=None
class linkedlist:
    def __init__(self):
        self.head=None
    def print_ll(self):
        if self.head is None:
            print("list is empty")
        else:
            n=self.head
            while n is not None:
                print(n.data)
                n=n.ref
    def add_begin(self,data):
        new_node=node(data)
        new_node.ref=self.head
        self.head=new_node
    def add_end(self,data):
        new_node=node(data)
        if self.head is None:
            self.head=new_node
        else:
            temp=self.head
            while temp.ref is not None:
                temp=temp.ref
            temp.ref=new_node
    def add_middle(self,data,pos):
        new_node=node(data)
        if pos==1:
            new_node.ref=self.head
            self.head=new_node
            return
        i=1
        temp=self.head
        while i<pos-1 and temp is not None:
            temp=temp.ref
            i+=1
        if temp is None:
            print("invalied pos")  
        else:
            new_node.ref=temp.ref
            temp.ref=new_node
    def delete_begin(self):
        if self.head is None:
            print("list is empty")
        else:
            self.head=self.head.ref
    def delete_end(self):
        if self.head is None:
            print("underflow")
        elif self.head.ref is None:
            self.head=None
        else:
            temp=self.head
            while temp.ref.ref is not None:
                temp=temp.ref
            temp.ref=None
    def del_value(self,val):
        if self.head is None:
            print("underflow")
            return 
        elif self.head.data == val:
            self.head=self.head.ref
            return
        else:
            temp=self.head
            reff=None
            while temp is not None:
                if temp.data == val:
                    break
                reff=temp
                temp=temp.ref
            if temp is None:
                print("val not found ")
                return 
        reff.ref=temp.ref
    def del_pos(self,pos):
        if self.head is None:
            print("underflow")
            return
        elif pos==1:
            self.head=self.head.ref
            return
        else:
            i=1
            temp=self.head
            while i<pos-1 and temp is not None:
                temp=temp.ref
                i+=1
            if temp is None or temp.ref is None:
                print("in valid")
                return
        temp.ref=temp.ref.ref
ll1=linkedlist()
ll1.add_begin(10)
ll1.add_begin(11)
ll1.add_end(15)
ll1.add_end(21)
ll1.add_middle(20,3)
ll1.print_ll()
print("---------")
ll1.delete_begin()
ll1.delete_end()
ll1.print_ll()
ll1.del_value(10)
ll1.print_ll()
ll2=linkedlist()
ll2.add_begin(100)
ll2.print_ll()
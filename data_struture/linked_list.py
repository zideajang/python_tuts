class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = Node()

    def append(self,data):
        new_node = Node(data)
        cur = self.head
        while cur.next != None:
            cur = cur.next
        cur.next = new_node
        
    def length(self):
        cur = self.head
        total = 0
        while cur.next!=None:
            total += 1
            cur = cur.next
        return total
    
    def display(self):
        elems = []
        cur_node = self.head
        while cur_node.next != None:
            cur_node=cur_node.next
            elems.append(cur_node.data)
        print(elems)
    
    def get(self,index):
        if index>=self.length():
            print("ERROR:'GET' Index out of range!")
            return None
        cur_idx=0
        cur_node = self.head
        while True:
            cur_node=cur_node.next
            if cur_idx==index:return cur_node.data
            cur_idx+=1
    
    def delete(self,index):
        if index>=self.length():
            print("ERROR:'Delete' Index out of range!")
            return
        cur_idx=0
        cur_node = self.head
        while True:
            last_node=cur_node
            cur_node = cur_node.next
            if cur_idx==index:
                last_node.next = cur_node.next
                return
            cur_idx+=1

    def update(self,index,data):
        if index>=self.length():
            print("ERROR:'Update' Index out of range!")
            return
        cur_idx = 0
        cur_node = self.head
        while True:
            cur_node=cur_node.next
            if cur_idx==index:
                cur_node.data = data
                return
            cur_idx+=1
if __name__ == "__main__":
    my_list = LinkedList()
    my_list.append(1)
    my_list.append(2)
    my_list.append(3)
    my_list.append(4)
    my_list.append(5)
    my_list.update(2,6)
    print(my_list.get(0))
    my_list.delete(3)
    my_list.display()
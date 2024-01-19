class Node:
    def __init__(self, data, next):
        self.data = data 
        self.next = next 

class LinkedList:
    def __init__(self):
        self.head = None
    
    def insert_at_beginning(self, data):
        node = Node(data, self.head)
        self.head = node
    
    def list_print(self):
        if self.head is None:
            print("Linked list exists, but it is empty")
            return

        iterator = self.head
        llstring = ""
        while iterator:
            llstring += str(iterator.data) + " => "
            iterator = iterator.next
        
        print(llstring)

if __name__ == '__main__':
    ll = LinkedList()
    ll.list_print()
    ll.insert_at_beginning("First Data Point")
    ll.list_print()
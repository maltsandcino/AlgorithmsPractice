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

    def insert_at_end(self, data):
        if self.head is None:
            ###Next here is none, because we are creating the head node in this instance
            self.head = Node(data, None)
            return
        
        ###Iterate through nodes to the last node in list below
        iterator = self.head
        while iterator.next:
            iterator = iterator.next
        ##Here we have reached the last node, and are going to insert our new ending node
        iterator.next = Node(data, None)


if __name__ == '__main__':
    ll = LinkedList()
    ll.list_print()
    ll.insert_at_beginning("First Data Point")
    ll.list_print()
    ll.insert_at_end("Second Data Point")
    ll.insert_at_beginning("Zeroth Data Point")
    ll.list_print()
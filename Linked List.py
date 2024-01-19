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

        current_node = self.head
        llstring = ""
        while current_node:
            llstring += str(current_node.data) + " => "
            current_node = current_node.next
        
        print(llstring)

    def insert_at_end(self, data):
        if self.head is None:
            ###Next here is none, because we are creating the head node in this instance
            self.head = Node(data, None)
            return
        
        ###Iterate through nodes to the last node in list below
        current_node = self.head
        while current_node.next:
            current_node = current_node.next
        ##Here we have reached the last node, and are going to insert our new ending node
        current_node.next = Node(data, None)
    
    ##Adding multiple values via iteration and calling insert at end function.
    def insert_values(self, data_list):
        
        for element in data_list:
            self.insert_at_end(element)
    
    def get_length(self):
        count = 0
        current_node = self.head
        while current_node:
            count += 1
            current_node = current_node.next
        
        return count
    



if __name__ == '__main__':
    ll = LinkedList()
    print(ll.get_length())
    # ll.insert_at_beginning("First Data Point")
    # ll.insert_at_end("Second Data Point")
    # ll.insert_at_beginning("Zeroth Data Point")
    ll.list_print()
    ll.insert_values(["New", "Also New", "Also New Again"])
    print(ll.get_length())

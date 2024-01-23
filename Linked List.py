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
    
    def remove_at_index(self, index):
        ###Basic edge case calls covered
        if index < 0 or index > self.get_length() - 1:
            raise Exception("Invalid index for this list")
        
        if index == 0:
            self.head = self.head.next
            return
        
        ##Begin iterating. Stop at node before desired index, and change pointer to next node's pointer.
        count = 0
        current_node = self.head
        
        while current_node:
            if count == index - 1:
                current_node.next = current_node.next.next
                break
            current_node = current_node.next
            count += 1
    
    def insert_after_value(self, data_after, data_to_insert):

        current_node = self.head
        while current_node:
            if current_node.data == data_after:
                temp = current_node.next
                current_node.next = Node(data_to_insert, temp)
            
            current_node = current_node.next
    
    def remove_by_value(self, data):

        current_node = self.head

        if current_node.data == data:
            self.head = current_node.next
            return

        while current_node:
            temp_node = current_node
            current_node = current_node.next
         
            if current_node.data == data:
                temp_next = current_node.next
                current_node = temp_node
                current_node.next = temp_next
                break
            
            

    def insert_at_index(self, index, data):
        ##Handle errors and case of entry at 0th index, i.e. beginning of list
        if index < 0 or index > self.get_length():
            raise Exception("Invalid index for this list")
        
        if index == 0:
            self.insert_at_beginning(data)

        ##Iterate through list until desired index point
            
        count = 0
        current_node = self.head
        ##When at node before desired index, we point to a new node we create
        while current_node:
            if count == index - 1:
                current_node.next = Node(data, current_node.next)
                break
            current_node = current_node.next
            count += 1            
        
    

if __name__ == '__main__':
    ll = LinkedList()

    # ll.insert_at_beginning("First Data Point")
    # ll.insert_at_end("Second Data Point")
    # ll.insert_at_beginning("Zeroth Data Point")
    
    ll.insert_values(["New", "Also New", "Insert after this", "Also New Again", "More Entries"])
    ll.insert_at_index(3, "Also New")
    ll.list_print()
    ll.remove_by_value("Also New")

    ll.list_print()
    

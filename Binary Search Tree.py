class BinarySearchTreeNode:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

    def add_child(self, data):
        if data == self.data:
            return
        if data < self.data:
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BinarySearchTreeNode(data)
        else:
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BinarySearchTreeNode(data)
    
    def in_order_traversal(self):
        elements = []
        #Visit Left Tree
        if self.left:
            elements += self.left.in_order_traversal()
        
        #Visit Node
        elements.append(self.data)

        #Visit Right Tree
        if self.right:
            elements += self.right.in_order_traversal()

        return elements
    
    def search(self, val):
      
        if self.data == val:
            return True
        
        if val < self.data:
            if self.left:
                return self.left.search(val)
            else:
                return False
        
        if val > self.data:
            if self.right:
                return self.right.search(val)
            else:
                return False
        
    def find_max(self):
            if self.right is None:
                return self.data
            return self.right.find_max()
    
    def find_min(self):
            if self.left is None:
                return self.data
            return self.left.find_min()
    
    def delete(self, val):
        if val < self.data:
            if self.left:
                self.left = self.left.delete(val)
        elif val > self.data:
            if self.right:
                 self.right = self.right.delete(val)
        else:
            if self.left is None and self.right is None:
                return None
            if self.left is None:
                return self.right
            if self.right is None:
                return self.left
            
            min_val = self.right.find_min()
            self.data = min_val
            ####Line below will recursively remove and update the rest of this branch to reorder the tree after deletion
            self.right = self.right.delete(min_val)
        
        return self

    def delete_left(self, val):
            if val < self.data:
                if self.left:
                    self.left = self.left.delete(val)
            elif val > self.data:
                if self.right:
                    self.right = self.right.delete(val)
            else:
                if self.left is None and self.right is None:
                    return None
                elif self.left is None:
                    return self.right
                elif self.right is None:
                    return self.right

                max_val = self.left.find_max()
                self.data = max_val
                ####Line below will recursively remove and update the rest of this branch to reorder the tree after deletion
                self.left = self.left.delete(max_val)
            
def height(node):
    if node is None:
        return 0
    return 1 + max(height(node.left), height(node.right))

def size(node):
    if node is None:
        return 0
    return 1 + size(node.left) + size(node.right)

def build_tree(elements):
    root = BinarySearchTreeNode(elements[0])

    for i in range(1,len(elements)):
        root.add_child(elements[i])
    
    return root

if __name__ == '__main__':
    numbers = [17, 4, 1, 20, 9, 2, 3, 4, 5, 6, 7, 70]
    numbers_tree = build_tree(numbers)
    print(numbers_tree.in_order_traversal())
    numbers_tree.delete(4)
    numbers_tree.deleteleft(17)
    print(numbers_tree.in_order_traversal())
    
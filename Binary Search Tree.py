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
    
    def is_BST(self):
               
        def valid(node, left, right):
            if not node:
                return True
            if not (node.data < right and node.data > left):
                return False
            
            return (valid(node.left, left, node.data) and valid(node.right, node.data, right))
        
        return valid(self, float("-inf"), float("inf"))
                    
def make_balanced_bst(data, lo=0, hi=None, parent=None):
    ###This takes a SORTED list of elements with no repeating values, otherwise the tree will not fit the correct Criteria
    if hi is None:
        hi = len(data) - 1

    if lo > hi:
        return None
    
    ##Getting Middle Value from data set
    mid = (lo + hi) // 2
    value = data[mid]

    root = BinarySearchTreeNode(value)
    ## Add Parent pointer for easier traversal
    root.parent = parent
    root.left = make_balanced_bst(data, lo, mid-1, root)
    root.right = make_balanced_bst(data, mid+1, hi, root)

    return root

def height(node):
    if node is None:
        return 0
    return 1 + max(height(node.left), height(node.right))

def is_balanced(node):
        if node is None:
            return True, 0
        balanced_l, height_l = is_balanced(node.left)
        balanced_r, height_r = is_balanced(node.right)
        balanced = balanced_l and balanced_r and abs(height_l - height_r) <= 1
        height = 1 + max(height_l, height_r)
        return balanced, height

def balance_check(node):

    if other_is_balanced(node) > 0:
        print(True)
    else:
        print(False)

def other_is_balanced(node):
    if node is None:
        return 1
    
    lh = other_is_balanced(node.left)

    if lh == 0:
        return 0
    
    rh = other_is_balanced(node.right)

    if rh == 0:
        return 0
    
    if (abs(lh - rh) > 1):
        return 0
    
    else:
        return max(lh, rh) + 1

def size(node):
    if node is None:
        return 0
    return 1 + size(node.left) + size(node.right)

def build_tree(elements):
    if not elements:
            print("Please Ensure there is data in the set")
            return
    root = BinarySearchTreeNode(elements[0])

    for i in range(1,len(elements)):
        root.add_child(elements[i])
    
    return root

if __name__ == '__main__':
    numbers = [8, 2, 11, 1, 5, 9, 13, 15, 4]
    numbers_tree = build_tree(numbers)

    numbers_unsorted = [8, 2, 11, 1, 5, 9, 13, 15, 4, 12, 15, 21, 1, 21, 17, 4, 4, 5, 17, 32, 37, 15, 21, 1, 21, 17, 4, 4, 5, 17, 32]
    x = sorted(numbers_unsorted)
    new_numset = set(x)
    newest_numlist = sorted(list(new_numset))
    bbst = make_balanced_bst(newest_numlist)
    bbst2 = make_balanced_bst(x)
    
    print(numbers_tree.in_order_traversal())
    # numbers_tree.delete(4)
    # numbers_tree.delete_left(17)
    print(numbers_tree.in_order_traversal())
    print(numbers_tree.is_BST())
    print(is_balanced(numbers_tree))
    test = [1]
    test_tree = build_tree(test)
    bbst3 = build_tree(newest_numlist)
    print(is_balanced(test_tree))
    print(other_is_balanced(numbers_tree))
    balance_check(numbers_tree)
    balance_check(bbst)
    print(is_balanced(bbst))
    print(is_balanced(bbst2))
    print(is_balanced(bbst3))
    ###In order traverse throuhg all elements then just call make balanced bst on these to balance unbalanced tree.
    print(bbst.in_order_traversal())
    bbst3 = make_balanced_bst(bbst3.in_order_traversal())
    print(is_balanced(bbst3))
    print(bbst3.is_BST())

    
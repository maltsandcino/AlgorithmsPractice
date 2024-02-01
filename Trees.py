class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None
    
    def add_child(self, child):
        child.parent = self
        self.children.append(child)
    
    def get_level(self):
        count = 0
        p = self.parent
        while p:
            count += 1
            p = p.parent
        return count
       
    
    def print_tree(self):
        spaces = "  " * self.get_level() * 3
        prefix = spaces + "|__" if self.parent else ""
        print(prefix + self.data)
        if self.children:
            for child in self.children:
                child.print_tree()



def build_product_tree():
    root = TreeNode("Electronics")

    laptop = TreeNode("Laptop")
    laptop.add_child(TreeNode("Mac"))
    laptop.add_child(TreeNode("Surface"))
    laptop.add_child(TreeNode("Thinkpad"))

    cellphone = TreeNode("Cell Phone")
    cellphone.add_child(TreeNode("iPhone"))
    cellphone.add_child(TreeNode("Pixel"))
    cellphone.add_child(TreeNode("Vivo"))

    tv = TreeNode("TV")
    tv.add_child(TreeNode("Samsung"))
    tv.add_child(TreeNode("LG"))
    tv.add_child(TreeNode("SONY"))

    root.add_child(laptop)
    root.add_child(cellphone)
    root.add_child(tv)

    return root
    

if __name__ == '__main__':
    root = build_product_tree()
    root.print_tree()
    print(root.children[0].get_level())
    p
    pass
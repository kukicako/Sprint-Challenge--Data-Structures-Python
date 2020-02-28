class BinarySearchTree:
    def __init__(self, key):
        self.value = key
        self.left = None
        self.right = None
        

    # Insert the given value into the tree
    def insert(self, value):
        if value is None:
            return
        # BST was empty
        elif self.value is None:
            self.value = BinarySearchTree(value)
        # insert into RIGHT subtree 
        elif value >= self.value: 
            if self.right is None:
                self.right = BinarySearchTree(value)
            else:
                self.right.insert(value)
        # insert into LEFT subtree:
        else: 
            if self.left is None:
                self.left = BinarySearchTree(value)
            else:
                self.left.insert(value)

    # Return True if the tree contains the value
    # False if it does not
    # Mistake here was not accounting for if the left/right node does not exist - explicitly returning False if it doesn't 
        # remember to use RETURN for recursive calls 
    def contains(self, target):
        if target == self.value:
            return True
        if target > self.value:
            if self.right is None:
                return False 
            else: 
                return self.right.contains(target)
        if target < self.value:
            if self.left is None:
                return False 
            else: 
                return self.left.contains(target)

        

    # Return the maximum value found in the tree
    def get_max(self):
        if self.right is None:
            return self.value
        else:
            return self.right.get_max()

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        if self.value is not None:
            cb(self.value)
            if self.left is not None:
                self.left.for_each(cb)
            if self.right is not None:
                self.right.for_each(cb)

    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self,node):
        if self.left is not None:
            self.left.in_order_print(node)
        if self.value is not None:
            print(self.value)
        if self.right is not None:
            self.right.in_order_print(node)
        else:
            return
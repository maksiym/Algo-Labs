class RBNode:
    def __init__(self, item):
        self.item = item
        self.parent = None
        self.left = None
        self.right = None
        self.color = 1


class RedBlackTree:

    def __init__(self, root=None):
        self.root = root
        self.ll = False
        self.rr = False
        self.rl = False
        self.lr = False

    def r_rotate(self, curr_elem):
        x = curr_elem.left
        y = x.right
        x.right = curr_elem
        curr_elem.left = y
        curr_elem.parent = x
        if y is not None:
            y.parent = curr_elem
        return x

    def l_rotate(self, curr_elem):
        x = curr_elem.right
        y = x.left
        x.left = curr_elem
        curr_elem.right = y
        curr_elem.parent = x
        if y is not None:
            y.parent = curr_elem
        return x

    def insert_balance(self, root, item):

        # Inserting as in BST
        rr_conflict: bool = False
        if root is None:
            return RBNode(item)
        elif item < root.item:
            root.left = self.insert_balance(root.left, item)
            root.left.parent = root
            if root is not self.root:
                if root.color == 1 and root.left.color == 1:
                    rr_conflict = True
        else:
            root.right = self.insert_balance(root.right, item)
            root.right.parent = root
            if root is not self.root:
                if root.color == 1 and root.right.color == 1:
                    rr_conflict = True

        # Rotating cases
        if self.ll:
            root = self.l_rotate(root)
            root.color = 0
            root.left.color = 1
            self.ll = False

        elif self.rr:

            root = self.r_rotate(root)
            root.color = 0
            root.right.color = 1
            self.rr = False

        elif self.rl:

            root.right = self.r_rotate(root.right)
            root.right.parent = root
            root = self.l_rotate(root)
            root.color = 0
            root.left.color = 1
            self.rl = False

        elif self.lr:

            root.left = self.l_rotate(root.left)
            root.left.parent = root
            root = self.r_rotate(root)
            root.color = 0
            root.right.color = 1
            self.lr = False

        # Recoloring cases
        if rr_conflict:
            if root.parent.right == root:

                if root.parent.left is None or root.parent.left.color == 0:
                    if root.left is not None and root.left.color == 1:
                        self.rl = True
                    elif root.right is not None and root.right.color == 1:
                        self.ll = True
                else:
                    root.parent.left.color = 0
                    root.color = 0
                    if root.parent is not self.root:
                        root.parent.color = 1
            else:
                if root.parent.right is None or root.parent.right.color == 0:
                    if root.left is not None and root.left.color == 1:
                        self.rr = True
                    elif root.right is not None and root.right.color == 1:
                        self.lr = True
                else:
                    root.parent.right.color = 0
                    root.color = 0
                    if root.parent is not self.root:
                        root.parent.color = 1

        return root

    def insert(self, item):
        if self.root is None:
            self.root = RBNode(item)
            self.root.color = 0
        else:
            self.root = self.insert_balance(self.root, item)

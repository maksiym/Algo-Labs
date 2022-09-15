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

    def insert_balance(self, node, item):

        # Inserting as in BST
        rr_conflict: bool = False
        if node is None:
            return RBNode(item)
        elif item < node.item:
            node.left = self.insert_balance(node.left, item)
            node.left.parent = node
            if node is not self.root:
                if node.color == 1 and node.left.color == 1:
                    rr_conflict = True
        else:
            node.right = self.insert_balance(node.right, item)
            node.right.parent = node
            if node is not self.root:
                if node.color == 1 and node.right.color == 1:
                    rr_conflict = True

        # Rotating cases
        if self.ll:
            node = self.l_rotate(node)
            node.color = 0
            node.left.color = 1
            self.ll = False

        elif self.rr:

            node = self.r_rotate(node)
            node.color = 0
            node.right.color = 1
            self.rr = False

        elif self.rl:

            node.right = self.r_rotate(node.right)
            node.right.parent = node
            node = self.l_rotate(node)
            node.color = 0
            node.left.color = 1
            self.rl = False

        elif self.lr:

            node.left = self.l_rotate(node.left)
            node.left.parent = node
            node = self.r_rotate(node)
            node.color = 0
            node.right.color = 1
            self.lr = False

        # Recoloring cases
        if rr_conflict:
            if node.parent.right == node:

                if node.parent.left is None or node.parent.left.color == 0:
                    if node.left is not None and node.left.color == 1:
                        self.rl = True
                    elif node.right is not None and node.right.color == 1:
                        self.ll = True
                else:
                    node.parent.left.color = 0
                    node.color = 0
                    if node.parent is not self.root:
                        node.parent.color = 1
            else:
                if node.parent.right is None or node.parent.right.color == 0:
                    if node.left is not None and node.left.color == 1:
                        self.rr = True
                    elif node.right is not None and node.right.color == 1:
                        self.lr = True
                else:
                    node.parent.right.color = 0
                    node.color = 0
                    if node.parent is not self.root:
                        node.parent.color = 1

        return node

    def insert(self, item):
        if self.root is None:
            self.root = RBNode(item)
            self.root.color = 0
        else:
            self.root = self.insert_balance(self.root, item)

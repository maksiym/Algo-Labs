class AVLNode:

    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1


class AVLTree:

    def delete_node(self, root, key):

        if not root:
            return root
        elif key < root.key:
            root.left = self.delete_node(root.left, key)
        elif key > root.key:
            root.right = self.delete_node(root.right, key)
        else:
            if root.left is None:
                temp = root.right
                del root
                return temp
            elif root.right is None:
                temp = root.left
                del root
                return temp

            temp = self.get_min_left_subtree(root.right)
            root.key = temp.key
            root.right = self.delete_node(root.right, temp.key)

        if root is None:
            return root

        root.height = 1 + max(self.get_height(root.left),
                              self.get_height(root.right))

        balance_factor = self.get_balance(root)

        if balance_factor > 1:
            # LL case
            if self.get_balance(root.left) >= 0:
                return self.right_rotate(root)
            # LR case
            else:
                root.left = self.left_rotate(root.left)
                return self.right_rotate(root)
        if balance_factor < -1:
            # RR case
            if self.get_balance(root.right) <= 0:
                return self.left_rotate(root)
            # RL case
            else:
                root.right = self.right_rotate(root.right)
                return self.left_rotate(root)
        return root

    def left_rotate(self, cur_elem):
        y = cur_elem.right
        y_left = y.left

        y.left = cur_elem
        cur_elem.right = y_left

        cur_elem.height = 1 + max(self.get_height(cur_elem.left), self.get_height(cur_elem.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))

        return y

    def right_rotate(self, cur_elem):
        y = cur_elem.left
        y_right = y.right

        y.right = cur_elem
        cur_elem.left = y_right

        cur_elem.height = 1 + max(self.get_height(cur_elem.left), self.get_height(cur_elem.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))

        return y

    @staticmethod
    def get_height(root):
        if not root:
            return 0
        return root.height

    def get_balance(self, root):
        if not root:
            return 0
        return self.get_height(root.left) - self.get_height(root.right)

    def get_min_left_subtree(self, root):
        if root is None or root.left is None:
            return root
        return self.get_min_left_subtree(root.left)

    def insert_node(self, root, key):
        """
        Not my insert function, needed only to implement deletion due to the task
        """

        if not root:
            return AVLNode(key)
        elif key < root.key:
            root.left = self.insert_node(root.left, key)
        else:
            root.right = self.insert_node(root.right, key)

        root.height = 1 + max(self.get_height(root.left),
                              self.get_height(root.right))

        balance_factor = self.get_balance(root)

        if balance_factor > 1:
            if key < root.left.key:
                return self.right_rotate(root)
            else:
                root.left = self.left_rotate(root.left)
                return self.right_rotate(root)

        if balance_factor < -1:
            if key > root.right.key:
                return self.left_rotate(root)
            else:
                root.right = self.right_rotate(root.right)
                return self.left_rotate(root)

        return root

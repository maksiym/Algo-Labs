from avl_tree_impl import AVLTree
from lab1.printer import printer


def main():
    avl_tree = AVLTree()
    root = None
    insert_nums = [33, 13, 52, 9, 21, 61, 8, 11]
    for num in insert_nums:
        root = avl_tree.insert_node(root, num)
    printer(root, None, False, False)
    print()
    avl_tree.delete_node(root, 13)
    printer(root, None, False, False)


if __name__ == '__main__':
    main()

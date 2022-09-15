from avl_tree_impl import AVLTree
from lab1.printer import printer


def main():
    avl_tree = AVLTree()
    root = None
    insert_nums = [14, 17, 11, 7, 53, 4, 13, 12, 8, 60, 19, 16, 20]
    for num in insert_nums:
        root = avl_tree.insert_node(root, num)
    printer(root, None, False, False)
    print()
    avl_tree.delete_node(root, 60)
    printer(root, None, False, False)


if __name__ == '__main__':
    main()

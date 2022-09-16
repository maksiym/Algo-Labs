from lab1.printer import printer
from rb_tree_impl import RedBlackTree


def main():
    rbt = RedBlackTree()

    rbt.insert(10)
    printer(rbt.root, None, False, True)
    rbt.insert(18)
    printer(rbt.root, None, False, True)
    rbt.insert(7)
    printer(rbt.root, None, False, True)
    rbt.insert(15)
    printer(rbt.root, None, False, True)
    rbt.insert(16)
    printer(rbt.root, None, False, True)
    rbt.insert(30)
    printer(rbt.root, None, False, True)
    rbt.insert(25)
    printer(rbt.root, None, False, True)
    rbt.insert(40)
    printer(rbt.root, None, False, True)
    rbt.insert(60)
    printer(rbt.root, None, False, True)
    rbt.insert(2)
    printer(rbt.root, None, False, True)
    rbt.insert(1)
    printer(rbt.root, None, False, True)
    rbt.insert(70)
    printer(rbt.root, None, False, True)


if __name__ == '__main__':
    main()

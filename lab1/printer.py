class Trunk:
    def __init__(self, prev=None, str_trunk=None):
        self.prev = prev
        self.str = str_trunk


def show_trunks(p):
    if p is None:
        return
    show_trunks(p.prev)
    print(p.str, end='')


def printer(root, prev, is_left, is_rb):
    """
    Not my print function, needed only for visualization tree
    """
    if root is None:
        return

    prev_str = '    '
    trunk = Trunk(prev, prev_str)
    printer(root.right, trunk, True, is_rb)

    if prev is None:
        trunk.str = '———'
    elif is_left:
        trunk.str = '.———'
        prev_str = '   |'
    else:
        trunk.str = '`———'
        prev.str = prev_str

    show_trunks(trunk)

    # Need some conditions to visualize only needed tree
    if is_rb:
        print(' ' + str(root.item) + '-' + str(root.color))
    else:
        print(' ' + str(root.key) + '-' + str(root.height))
    if prev:
        prev.str = prev_str
    trunk.str = '   |'
    printer(root.left, trunk, False, is_rb)

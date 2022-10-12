class XPNode:
    def __init__(self, xp, l_root=None, r_root=None):
        self.xp = xp
        self.l_root = l_root
        self.r_root = r_root

    def __str__(self):
        return f'{self.xp}'


class DFS:

    def __init__(self):
        self.res = 0

    def find_path_sum_by_dfs(self, root: XPNode) -> int:
        if not root:
            return 0

        left_max = 0
        right_max = 0

        if root.l_root is not None:
            left_max = self.find_path_sum_by_dfs(root.l_root)
        if root.r_root is not None:
            if root.l_root is None:
                right_max = self.find_path_sum_by_dfs(root.r_root)

            elif root.l_root.r_root is not None:
                right_max = max(left_max - root.l_root.xp,
                                self.find_path_sum_by_dfs(root.r_root.r_root) + root.r_root.xp)

        self.res = max(self.res, root.xp + left_max, root.xp + right_max)

        return root.xp + max(left_max, right_max)

    def dfs_xp_nodes(self, xp_nodes):
        res = []
        for xp in xp_nodes:
            res.append(self.find_path_sum_by_dfs(xp))

        return max(res)

class XPNode:
    def __init__(self, xp, l_root=None, r_root=None):
        self.xp = xp
        self.l_root = l_root
        self.r_root = r_root

    def __str__(self):
        return f'{self.xp}'


class DFS:
    def find_path_sum_by_dfs(self, root: XPNode) -> int:
        res = [root.xp]
        if not root:
            return 0

        def dfs(root):
            left_max = 0
            right_max = 0
            if root.l_root is not None:
                left_max = dfs(root.l_root)
            if root.r_root is not None:
                right_max = dfs(root.r_root)

            res[0] = max(res[0], root.xp + left_max, root.xp + right_max)

            return root.xp + max(left_max, right_max)

        dfs(root)
        return res[0]

    def do_xp_nodes(self, xp_nodes):
        res = []
        for xp in xp_nodes:
            for x in xp:
                result = self.find_path_sum_by_dfs(x)
                res.append(result)

        return max(res)

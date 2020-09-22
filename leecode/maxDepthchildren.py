"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        """
            给定一个 N 叉树，找到其最大深度。

            最大深度是指从根节点到最远叶子节点的最长路径上的节点总数。

            例如，给定一个 3叉树 :
            我们应返回其最大深度，3。

            说明:

            树的深度不会超过 1000。
            树的节点总不会超过 5000。


            来源：力扣（LeetCode）
            链接：https://leetcode-cn.com/problems/maximum-depth-of-n-ary-tree
            著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
        """
        if not root:
            return 0
        def tree(rt):
            q = [rt]
            dp = 0
            while q:
                _q = []
                for _root in q:
                    
                    if _root and _root.children:
                        if type(_root.children) is list:
                            for _j in _root.children:
                                _q.append(_j)
                        else:
                            _q.append(_root.children)
                q = _q
                dp+=1

            return dp
        return tree(root)
    
    def maxDepth_eg(self, root: 'Node') -> int:
        """
        法1，递归法，dfs
        时间复杂度：我们访问每个节点一次，时间复杂度为 O(N) 。
        空间复杂度：最坏情况下，整棵树是非平衡的，例如每个节点都只有一个孩子，递归会调用 N（树的高度）次，因此栈的空间开销是 O(N)。
        但在最好情况下，树是完全平衡的，高度只有 log(N)，因此在这种情况下空间复杂度只有 O(log(N)) 。
        """
        # if not root: return 0
        # if root.children:
        #     depth_children = [self.maxDepth(node) for node in root.children]
        # else:
        #     return 1
        # return max(depth_children) + 1
        """
        法3 迭代法 DFS
        时间O(N) 空间O(N)
        """
        if not root: return 0
        depth=1
        queue=[(root,depth)]
        while queue:
            root,depth=queue.pop(0)
            if root.children:
                for node in root.children: 
                    queue.append((node,depth+1))
        return depth

        """
        法3 迭代法 BFS
        时间O(N) 空间O(N)
        """
        # if not root: return 0
        # from collections import deque
        # final_depth = 1
        # q = deque([(root,1)])
        # while q:
        #     root, depth = q.popleft()
        #     final_depth = max(final_depth, depth)
        #     if root.children:
        #         for node in root.children:
        #             q.append([node, depth + 1])
        # return final_depth

        # if not root: return 0
        # final_depth=1
        # stack=[(root,final_depth)]
        # while stack:
        #     root,depth=stack.pop()
        #     final_depth=max(final_depth,depth)
        #     if root.children:
        #         for node in root.children: 
        #             stack.append((node,depth+1))
        # return final_depth
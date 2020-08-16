# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        if root == None:
            return 'null,'
        left_serialize = self.serialize(root.left)
        right_serialize = self.serialize(root.right)
        return str(root.val) + ',' + left_serialize + right_serialize

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        def dfs(queue):
            val = queue.popleft()
            if val == 'null':
                return None
            node =  TreeNode(val)
            node.left = dfs(queue)
            node.right = dfs(queue)
            return node
        
        from collections import deque

        queue = deque(data.split(','))

        return dfs(queue)
    
    def _serialize_eg(self, root):
        if not root:
            return
        l=[root]
        l_copy=[]
        a,ans=[],[root.val]
        while True:
            for i in l:
                if i.left:
                    l_copy.append(i.left)
                    a.append(i.left.val)
                else:
                    a.append(None)
                if i.right:
                    l_copy.append(i.right)
                    a.append(i.right.val)
                else:
                    a.append(None)
            if a==[]:
                break
            l=l_copy.copy()
            ans+=a
            l_copy,a=[],[]
        while ans[-1]!=0 and not ans[-1]:
            ans.pop()
        return self._deserialize_eg(ans)

    def _deserialize_eg(self,data):
        return data
        

    def _serialize_37(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return []
        q = [root]
        res = [root.val]
        while q:
            _tmp = []
            for i in q:
                if i is None:
                 
                    continue
               
                if i.left:
                    _tmp.append(i.left)
                    res.append(i.left.val)
                else:
                    _tmp.append(i.left)
                    res.append(None)

                if i.right:
                    _tmp.append(i.right)
                    res.append(i.right.val)
                else:
                    _tmp.append(i.right)
                    res.append(None)
            if _tmp:
                while _tmp :
                    if _tmp[-1] is None:
                        _tmp.pop()
                    else:
                        break
                q = _tmp
            else:
                q = []
       
        while res:
            if res[-1] is None:
                res.pop()
            else:
                break
        return self.deserialize(res)

    def _deserialize_37(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        return data

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
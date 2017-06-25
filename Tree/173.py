"""
    173. Binary Search Tree Iterator

    @date: 2017/05/11
"""
# Definition for a  binary tree node
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator(object):
    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.root = root
        self.order = []
        def inorder(node):
            if not node:
                return
            inorder(node.left)
            self.order.append(node.val)
            inorder(node.right)
        inorder(root)
        self.index = -1
        
    def hasNext(self):
        """
        :rtype: bool
        """
        if self.index < len(self.order) - 1:
            return True
        else:
            return False

    def next(self):
        """
        :rtype: int
        """
        if self.hasNext():
            self.index += 1
            return self.order[self.index]
        else:
            return None

# Your BSTIterator will be called like this:
# i, v = BSTIterator(root), []
# while i.hasNext(): v.append(i.next())
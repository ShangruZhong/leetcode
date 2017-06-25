"""
    116. Populating Next Right Pointers in Each Node
    
    1：Perfect binary tree + pre-order dfs
    2：Refer to discussion, iterative + level-traverse
    @date: 2017/05/11
"""
# Definition for binary tree with next pointer.
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution:
    # @param root, a tree link node
    # @return nothing

    # solution 1
    def connect(self, root):
        if not root:
            return 
        if root.left:
            root.left.next = root.right
            if root.next:
                root.right.next = root.next.left
        
        self.connect(root.left)
        self.connect(root.right)

    # solution 2
    def connect(self, root):
        if not root:
            return
        prev = root
        cur = None
        while prev.left:
            cur = prev
            while cur: 
                cur.left.next = cur.right
                if cur.next:
                    cur.right.next = cur.next.left
                cur = cur.next
            prev = prev.left
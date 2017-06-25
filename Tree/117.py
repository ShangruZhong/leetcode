"""
    117. Populating Next Right Pointers in Each Node II

    Linked-list + level traverse

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
    def connect(self, root):
        dummy = TreeLinkNode(0)
        child = dummy
        while root:
            child.next = root.left
            if child.next:
                child = child.next
            child.next = root.right
            if child.next:
                child = child.next
            root = root.next
            if not root:
                child = dummy # ensure child point to dummy
                root = dummy.next # current root.left assign to root
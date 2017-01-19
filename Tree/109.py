"""
    109. Convert Sorted List to Binary Search Tree

    Set slow and fast pointer to locate middle node recursively
    @date: 2016/10/20
"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        if not head:
            return
        if not head.next: # only one node
            return TreeNode(head.val)
        # more than two nodes, set slow & fast pointer to locate the middle node
        slow = head
        fast = head.next.next
        while fast and fast.next: # if 'fast' == None, 0 and any = 0
            slow = slow.next
            fast = fast.next.next
        
        tmp = slow.next # tmp refers to 'root' (slow.next)
        slow.next = None # sub linked list as leftchild of 'tmp'
        
        root = TreeNode(tmp.val)
        root.left = self.sortedListToBST(head)
        root.right = self.sortedListToBST(tmp.next)
        return root
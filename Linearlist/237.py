"""
    237. Delete Node in a Linked List

    Foolish question...
    @date: 2017/01/21
"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        while node and node.next:
            prev = node
            node.val = node.next.val
            node = node.next
        prev.next = None

    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        prev = node
        node.val = node.next.val
        node = node.next
        prev.next = node.next
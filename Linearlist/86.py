"""
    86. Partition List

    use two dummy nodes
    @date: 2017/01/05
"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        h1 = ListNode(0)
        h2 = ListNode(0)
        t1 = h1
        t2 = h2
        
        while head:
            if head.val < x:
                t1.next = head 
                t1 = t1.next
            else:
                t2.next = head
                t2 = t2.next
            head = head.next

        t2.next = None # Do remember!
        t1.next = h2.next
        return h1.next
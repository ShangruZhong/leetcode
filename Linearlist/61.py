# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if head == None or head.next == None or k == 0:#notice!! k=0, return head instead of none
            return head
        cur1 = head
        len = 1
        while cur1.next:
            len += 1
            cur1 = cur1.next
        if k%len==0: #notice!!
            return head
        if k>len: #notice!! circular operation
            index = len-k%len
        else:
            index = len-k
        cur2 = head
        while index>1:
            cur2 = cur2.next
            index -=1
        dummy = cur2.next
        cur2.next = None
        cur1.next = head
        return dummy



# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None:
            return None
        cur = head
        pend = cur.next
        while pend:
            while cur.val == pend.val:
                pend = pend.next
                if pend == None:
                    break
            cur.next = pend
            cur = cur.next
            if pend != None:
                pend = pend.next
        return head



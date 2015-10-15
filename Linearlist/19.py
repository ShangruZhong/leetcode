# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        if head == None:
            return None
        cur = head
        index = 1
        while cur.next:
            index = index+1
            cur = cur.next
        if n==index:
            return head.next
        else:
            last = head
            for i in range(index-n-1):
                last = last.next
            remove = last.next
            if remove.next:
                last.next = remove.next
            else:
                last.next = None
        return head


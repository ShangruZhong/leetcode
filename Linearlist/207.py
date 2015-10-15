# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None:
            return None
        cur = head
        last = cur
        pend = cur.next
        while pend:
            if cur == head:
                pend = pend.next
                cur = cur.next
                head.next = None
            else:
                cur.next = last
                last = cur
                cur = pend
                pend = pend.next
        cur.next = last
        return cur

head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)

obj = Solution()
a = obj.reverseList(head)
while a:
    print a.val
    a =a.next
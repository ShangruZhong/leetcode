# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        carry = 0
        head = ListNode(0)
        cur = head
        while l1 and l2:
            sum = l1.val+l2.val+carry
            carry = sum/10
            cur.next = ListNode(sum%10)
            l1 = l1.next
            l2 = l2.next
            cur = cur.next
        while l1:
            sum = l1.val+carry
            carry = sum/10
            cur.next = ListNode(sum%10)
            l1 = l1.next
            cur = cur.next
        while l2:
            sum =  l2.val+carry
            carry = sum/10
            cur.next = ListNode(sum%10)
            l2 = l2.next
            cur = cur.next
        if carry:
            cur.next = ListNode(carry)
        return head.next



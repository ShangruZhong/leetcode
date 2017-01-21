"""
    445. Add Two Numbers II

    Based on 2. addTwoNumbers + reverseList
    @date: 2017/01/21
"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        l1 = self.reverseList(l1)
        l2 = self.reverseList(l2)
        res = self.addTwoNums(l1, l2)
        return self.reverseList(res)
    
    def reverseList(self, head):
        prev = None
        next = None
        while head:
            next = head.next
            head.next = prev
            prev = head
            head = next
        return prev
    
    def addTwoNums(self, l1, l2):
        head = ListNode(-1)
        cur = head
        carry = 0
        while True:
            if l1:
                carry += l1.val
                l1 = l1.next
            if l2:
                carry += l2.val
                l2 = l2.next
            cur.val = carry % 10
            carry = carry / 10
            if l1 or l2 or carry:
                cur.next = ListNode(-1)
                cur = cur.next
            else:
                break
        return head
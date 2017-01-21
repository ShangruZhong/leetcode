"""
    2. Add Two Numbers

    From now on, start linked-list practice

    @author: Shangru
    @date: 2015/10/11
"""
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


"""
	Update solution

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
            carry /= 10
            if l1 or l2 or carry:
                cur.next = ListNode(-1)
                cur = cur.next
            else:
                break
        return head
                
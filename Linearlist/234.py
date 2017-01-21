"""
    234. Palindrome Linked List

    Find middle pointer & reverse list
    Compare two half part
    @date: 2017/01/21
"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head == None:
            return True
        mid = self.findMiddle(head)
        tail = self.reverseList(mid)
        while head:
            if head.val != tail.val:
                return False
            head = head.next
            tail = tail.next
        return True
    
    def findMiddle(self, head):
        slow = head
        fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        return slow
    
    def reverseList(self, head):
        prev = None
        next = None
        while head:
            next = head.next
            head.next = prev
            prev = head
            head = next
        return prev
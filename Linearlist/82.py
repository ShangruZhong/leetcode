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
        if head == None or head.next == None:
            return head
        dummy = ListNode(0)
        dummy.next = head
        head = dummy
        flag = 0
        while head:
            if (head.next and head.next.next and head.next.next.val == head.next.val):
                head.next = head.next.next
                flag = 1
            elif flag and head.next:
                head.next = head.next.next #notice!
                flag = 0
            else:
                head = head.next
        return dummy.next

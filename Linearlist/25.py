"""
    25. Reverse Nodes in k-Group

    Similar to 24.Swap Nodes in Pairs, while k=2.
    Reverse once every k nodes.
    Remain while number of resting node < k.

    @author: Shangru
    @date: 2015/10/20
"""
"""
    25. Reverse Nodes in k-Group

    Update solution
    @date: 2017/01/22
"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if k < 2: 
            return head
        
        cur = head
        next = None
        group_start = None
        prev_last = None
        
        count = 1
        while cur:
            next = cur.next
            if count == k:
                # initialize group_start & head !!!!
                if prev_last == None:
                    group_start = head
                    head = cur
                else:
                    group_start = prev_last.next # update group_start before grouping
                self.reverse(prev_last, group_start, cur, next)
                prev_last = group_start # update prev_last after grouping
                count = 0
            count += 1
            cur = next
        return head
    
    def reverse(self, prev_last, group_start, group_end, next_first):
        
        prev = group_start
        cur = group_start.next
        next = None
        
        while cur != next_first:
            next = cur.next
            cur.next = prev
            prev = cur
            cur = next
        # after reverse, group_end->new head, group_start->new tail
        if prev_last:
            prev_last.next = group_end
        group_start.next = next_first
    
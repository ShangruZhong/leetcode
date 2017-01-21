"""
	138. Copy List with Random Pointer

	@date: 2017/01/21
"""
# Definition for singly-linked list with a random pointer.
# class RandomListNode(object):
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        if head == None:
            return 
        map = {}
        cur = head
        while cur:
            map[cur] = RandomListNode(cur.label)
            cur = cur.next
        cur = head
        while cur:
            if cur.next:
                map[cur].next = map[cur.next]
            if cur.random:
                map[cur].random = map[cur.random]
            cur = cur.next
        return map[head]
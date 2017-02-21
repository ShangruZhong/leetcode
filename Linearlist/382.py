"""
    382. Linked List Random Node

    @date: 2017/02/21
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):

    def __init__(self, head):
        """
        @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node.
        :type head: ListNode
        """
        self.head = head
        self.count = 0
        self.val = []
        while self.head:
            self.val.append(self.head.val)
            self.count += 1
            self.head = self.head.next
            
    def getRandom(self):
        """
        Returns a random node's value.
        :rtype: int
        """
        import random
        return self.val[random.randint(0, self.count - 1)]

# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()
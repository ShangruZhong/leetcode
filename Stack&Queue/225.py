"""
    225. Implement Stack using Queues

    This is my 200th algorithm problem on Leetcode!
    @date: 2017/06/10
"""
class MyStack(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.queue = []

    def push(self, x):
        """
        Push element x onto stack.
        :type x: int
        :rtype: void
        """
        self.queue.append(x)
        size = len(self.queue)
        for i in xrange(size-1):
            self.queue.append(self.queue.pop(0))

    def pop(self):
        """
        Removes the element on top of the stack and returns that element.
        :rtype: int
        """
        return self.queue.pop(0) if not self.empty() else None

    def top(self):
        """
        Get the top element.
        :rtype: int
        """
        return self.queue[0] if not self.empty() else None
        

    def empty(self):
        """
        Returns whether the stack is empty.
        :rtype: bool
        """
        return len(self.queue) == 0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
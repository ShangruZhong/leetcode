"""
    71. Simplify Path

    '/a/../b/c/d/../e'=>'/b/c/e'

    Drop when meet '..' next,
    very effective use stack,
    notice bound case: '/../*' or '../*'
    @date: 2017/02/04
"""
class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        simple_path = [p for p in path.split("/") if p != "." and p != ""]
        stack = []
        for p in simple_path:
            if p == "..":
                if stack: # deal with "/../*","../*"
                    stack.pop()
            else:
                stack.append(p)
        return "/" + "/".join(stack)
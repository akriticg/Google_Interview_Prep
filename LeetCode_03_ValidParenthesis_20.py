'''
valid parenthesis
Given a string containing just the characters '(', ')', '{', '}',
'[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.
https://leetcode.com/problems/valid-parentheses/description/
'''


class Solution(object):
    def isValid(self, s):

        valid = {')': '(', ']': '[', '}': '{'}

        stack = []
        
        for c in s:
            if c in valid:
                top_element = stack.pop() if stack else '#'
                if top_element != valid[c]:
                    return False
            else:
                stack.append(c)

        return not stack

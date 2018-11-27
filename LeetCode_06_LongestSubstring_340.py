'''
340. Longest Substring with At Most K Distinct Characters

Given a string, find the length of the longest substring T
that contains at most k distinct characters.

Example 1:

Input: s = "eceba", k = 2
Output: 3
Explanation: T is "ece" which its length is 3.
Example 2:

Input: s = "aa", k = 1
Output: 2
Explanation: T is "aa" which its length is 2.
https://leetcode.com/problems/longest-substring-with-at-most-k-distinct-characters/description/
'''


class Solution(object):
    def lengthOfLongestSubstringKDistinct(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        if not s or k == 0:
            return 0

        dic = {}
        ans, l = 0, 0

        for i in range(len(s)):
            dic[s[i]] = i
            print("i =", i)
            print(dic)
            if len(dic) > k:
                print("entered loop with k = ", k)
                r = min(dic.values())
                print("r = ", r)
                c = s[r]
                print("c = ", c)
                ans = max(ans, i-l)
                print("ans = ", ans)
                l = r+1
                print("l = ", l)
                print("deleting : ", dic[c])

                del dic[c]

                print("remaining: ", dic)

        print("final ans = ", ans)
        print("final l = ", l)
        ans = max(ans, len(s)-l)
        print(ans)

        return ans


c = Solution()
c.lengthOfLongestSubstringKDistinct("eeecebbbbaaaaaaaaaa", 3)

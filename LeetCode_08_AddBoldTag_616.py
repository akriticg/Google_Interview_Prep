'''
616. Add Bold Tag in String
Given a string s and a list of strings dict, you need to add a closed pair of bold tag <b> and </b> to wrap the substrings in s that exist in dict. If two such substrings overlap, you need to wrap them together by only one pair of closed bold tag. Also, if two substrings wrapped by bold tags are consecutive, you need to combine them.
https://leetcode.com/problems/add-bold-tag-in-string/description/
'''

def addBoldTag(s, dict):
        """
        :type s: str
        :type dict: List[str]
        :rtype: str
        """

        status = [False]*len(s)
        final = ""

        for word in dict:
            start = s.find(word)
            print(start)
            last = len(word)
            while start != -1:
                for i in range(start, last+start):
                    status[i] = True
                start = s.find(word,start+1)
        print(status)
        i = 0
        i = 0
        while i < len(s):
            if status[i]:
                final += "<b>"
                while i < len(s) and status[i]:
                    final += s[i]
                    i += 1

                final += "</b>"

            else:
                final += s[i]
                i += 1

        return final

print(addBoldTag("abcxyz123", ["abc","123"]))
'''
76. Minimum Window Substring
Given a string S and a string T, find the minimum window in S which will contain all the characters in T in complexity O(n).

Example:

Input: S = "ADOBECODEBANC", T = "ABC"
Output: "BANC"
Note:

If there is no such window in S that covers all characters in T, return the empty string "".
If there is such window, you are guaranteed that there will always be only one unique minimum window in S.

https://leetcode.com/problems/minimum-window-substring/description/
'''
import collections


def minWindow(s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        # Defaultdict is very useful in this problem, though i don't like to import modules

        target_count_dict = collections.defaultdict(int)
        for ch in t:
            target_count_dict[ch] += 1

        remain_missing = len(t)
        start_pos, end_pos = 0, float('inf')
        current_start = 0

        # Enumerate function makes current_end indexes from 1
        for current_end, ch in enumerate(s, 1):
            print(current_end, ch)
            # Whenever we encounter a character, no matter ch in target or not, we minus 1 in count dictionary
            # But, only when ch is in target, we minus the length of remain_missing
            # When the remain_missing is 0, we find a potential solution.
            if target_count_dict[ch] > 0:
                remain_missing -= 1
                # print(remain_missing)
            target_count_dict[ch] -= 1
            # print(target_count_dict)

            if remain_missing == 0:
                # Remove redundant character
                # Try to find the fist position in s that makes target_count_dict value equals 0
                # Which means we can't skip this character in s when returning answer
                while target_count_dict[s[current_start]] < 0:
                    print(s[current_start])
                    target_count_dict[s[current_start]] += 1
                    current_start += 1
                if current_end - current_start < end_pos - start_pos:
                    start_pos, end_pos = current_start, current_end

                # We need to add 1 to current_start, and the correspondence value in dictionary, is because
                # this is the first character of the potential answer. So, in future iteration, when we encounter this character,
                # We can remove this currently first character to try to find a shorter answer.
                target_count_dict[s[current_start]] += 1
                remain_missing += 1
                current_start += 1

        return s[start_pos:end_pos] if end_pos != float('inf') else ""


print(minWindow("ADOBECODEBANC", "ABC"))
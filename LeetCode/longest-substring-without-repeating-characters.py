# problem Link https://leetcode.com/problems/longest-substring-without-repeating-characters/
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        ch = ''
        i = 0
        count = []
        a = 0
        # track is used to store the last index of any repeated char found
        track = {}
        # coz is to keep track how many times an alphabet i have passed through
        coz = {}
        while i < len(s):

            if s[i] in ch:
                if (s[i] not in coz.keys()) or (s[i] in coz.keys() and coz[s[i]] < s.count(s[i])):
                    b = i
                    i = track[s[i]] + 1
                    ch = ''
                    # new line
                    track[s[i]] = b
                    if s[i] in coz.keys():
                        coz[s[i]] += 1
                    else:
                        coz[s[i]] = 0
                    count.append(a)
                    a = 0
                    continue
                ch = '' + s[i]
                count.append(a)
                a = 1
            elif s[i] not in ch:
                a += 1
                track[s[i]] = i
                ch += s[i]
            if i == (len(s) - 1):
                count.append(a)
            # print('----',ch)
            i += 1
        # print(count)
        track.clear()
        coz.clear()
        count.sort()
        # print(count)
        if len(count) > 0:
            return count[-1]
        else:
            return 0


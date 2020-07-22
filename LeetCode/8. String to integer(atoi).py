class Solution:
    # question link- https://leetcode.com/problems/string-to-integer-atoi/
    def myAtoi(self, str: str) -> int:
        pos_lim = 2 ** (31) - 1
        neg_lim = 0 - 2 ** (31)
        # space=ord(" ")
        # tab=ord("   ")
        # neg=ord("-")
        # pos=ord("+")
        result = ""
        if len(str) == 0:
            return 0
        negative = False
        positive = False
        # reject=[space,tab]
        # print("str is ",str)
        for i in range(len(str)):
            # print("in iteration",str[i],"ascii val is",ord(str[i]),"i=",i)
            if str[i] == " " and len(result) == 0 and (not positive and not negative):
                continue
            if str[i] == "-" and len(result) == 0 and (not negative and not positive):
                negative = True
                continue
            elif str[i] == "+" and len(result) == 0 and (not negative and not positive):
                positive = True
                continue
            elif ord(str[i]) >= 48 and ord(str[i]) <= 57:
                result += str[i]
                # print(str[i])
            elif (ord(str[i]) > 57 or ord(str[i]) < 48) and str[i] != " ":
                if len(result) > 0:
                    break
                else:
                    result = "0"
                    break
            elif str[i] == "+" and len(result) != 0 and (negative or positive):
                result = "0"
                break
            elif str[i] == "-" and len(result) != 0 and (negative or positive):
                result = "0"
                break
            elif str[i] == " " and (len(result) > 0 or negative or positive):
                break
            else:
                continue

        if len(result) == 0:
            return 0
        new_result = int(result)
        if not negative:
            if new_result > pos_lim:
                return pos_lim
            else:
                return new_result
        elif negative:
            # print(new_result,"pos_limit is",pos_lim)
            if new_result > pos_lim:
                return neg_lim
            else:
                return 0 - new_result



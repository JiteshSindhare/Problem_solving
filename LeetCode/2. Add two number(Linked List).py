"""Problem Link https://leetcode.com/problems/add-two-numbers/
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        a1 = []
        c = 0
        d = 0
        z = 0
        a2 = []
        b = l1
        r = 0
        lt = []
        root = 0
        while (True):
            if b == None:
                break
            else:
                a1.append(b.val)
            b = b.next
        b = l2
        a1.reverse()
        for i in a1:
            c = c * 10 + i
        while (True):
            if b == None:
                break
            else:
                a2.append(b.val)
            b = b.next
        a2.reverse()
        for i in a2:
            d = d * 10 + i
        # print('d',d)
        z = c + d
        z = str(z)
        for i in range(len(z) - 1, -1, -1):
            if i == (len(z) - 1):
                res = ListNode(int(z[i]))
                root = res
                lt.append(z[i])
            else:
                res.next = ListNode(int(z[i]))
                res = res.next
                lt.append(z[i])

        res = root
        # print('resulted ',lt)
        return res

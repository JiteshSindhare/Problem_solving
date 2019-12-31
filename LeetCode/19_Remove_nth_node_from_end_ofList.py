"""
Remove Nth Node from End of List
Problem link- https://leetcode.com/problems/remove-nth-node-from-end-of-list/
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        li = []
        while head != None:
            li.append(head.val)
            head = head.next
        z = li[-n]
        d = len(li) - n
        li.pop(d)
        if len(li) != 0:
            res_head = ListNode(li[0])
            a = self.makeList(li, 0)
            return a
        else:
            return None
        # for i in range(1,len(li)):
        #     res_head.next=ListNode(li[i])
        #     a=ListNode(li[i])

    def makeList(self, li, i):
        res_head = ListNode(li[i])
        if i + 1 < len(li):
            b = i + 1
            res_head.next = self.makeList(li, b)

        return res_head



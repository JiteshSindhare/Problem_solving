#Problem link- https://leetcode.com/problems/median-of-two-sorted-arrays/
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        result = []
        i, j = 0, 0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                result.append(nums1[i])
                i += 1
            else:
                result.append(nums2[j])
                j += 1

        while i < len(nums1):
            result.append(nums1[i])
            i += 1

        while j < len(nums2):
            result.append(nums2[j])
            j += 1

        print(result)
        if len(result) % 2 == 0:
            mid = round(len(result) / 2)
            return (result[mid] + result[mid - 1]) / 2
        else:
            mid = len(result) / 2 - 0.5
            return result[round(mid)]


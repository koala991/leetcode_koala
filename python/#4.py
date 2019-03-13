# class Solution:
#     def findMedianSortedArrays(self, nums1, nums2):
#         snums = sorted(nums1 + nums2)
#         ll = len(snums)
#         return snums[int(ll/2)] if ll % 2 else sum(snums[int(ll/2) - 1 : int(ll/2) + 1])/2


class Solution:
    def nextNum(self, nums1, nums2):
            return


    def findMedianSortedArrays(self, nums1, nums2):
        t_len = len(nums1) + len(nums2)
        count = 0
        while count <= t_len/2:
            pass
        return

print(Solution().findMedianSortedArrays([1, 2], [3, 4]))
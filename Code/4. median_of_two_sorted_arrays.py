class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        num = sorted(nums1 + nums2)
        if len(num) % 2 == 0: # odd
            midian = (num[len(num)//2-1] + num[len(num)//2]) / 2
        else: # even
            midian = num[len(num)//2]
        
        return midian

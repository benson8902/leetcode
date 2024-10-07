class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            search_num = target - nums[i]
            if search_num in nums and nums.index(search_num) != i:
                return [i, nums.index(search_num)]    

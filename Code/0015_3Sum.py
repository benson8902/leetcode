from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        output = []
        nums.sort()
        for i in range(len(nums) - 2):
            # remove duplicate
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            # two side: head and tail
            left, right = i + 1, len(nums) - 1
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                if total == 0:
                    output.append([nums[i], nums[left], nums[right]])
                    # find new element
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    # didn't get new element so we need to do it again to let us get a new element
                    left += 1
                    right -= 1
                elif total < 0: 
                    left += 1
                else:
                    right -= 1
        return output

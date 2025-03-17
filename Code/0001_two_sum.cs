public class Solution {
    public int[] TwoSum(int[] nums, int target) {
        // save numebr and indices
        Dictionary<int, int> numMap = new Dictionary<int, int>(); 
        for (int i = 0; i < nums.Length; i++) {
            // check 'complement' whether in nums
            int complement = target - nums[i]; 
            if (numMap.ContainsKey(complement)) {
                // Return indices of the complement and current number
                return new int[] { numMap[complement], i }; 
            }
            // store number in dictionary
            numMap[nums[i]] = i; 
        }
        // can't find any number match target
        return new int[] {}; 
    }
}

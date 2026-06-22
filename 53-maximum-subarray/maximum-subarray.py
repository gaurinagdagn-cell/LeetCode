class Solution:
    def maxSubArray(self, nums: List[int]) -> int: 
        #initialize variables with first element
        max_global = nums[0]
        current_sum = nums[0]
        
        #iteration thru array
        for num in nums[1:]:
            #decide whether to add curr no to the existing subarray
            # or start a new subarray from the curr nor
            current_sum = max(num, current_sum + num)
            
            #update max sum 
            if current_sum > max_global:
                max_global = current_sum
                
        return max_global
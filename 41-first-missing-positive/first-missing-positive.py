class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
  
        n = len(nums)

        #number x is placed at index x - 1
        for i in range(n):
            while (
                1 <= nums[i] <= n and # number is within valid range
                nums[nums[i] - 1] != nums[i]       
            ):
                correct = nums[i] - 1    # correct index for nums[i]
                nums[i], nums[correct] = nums[correct], nums[i]

        # the first index where number is not in its correct pos
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1

        #if all nums from 1 to n are present 
        # then the missing positive is n + 1
        return n + 1
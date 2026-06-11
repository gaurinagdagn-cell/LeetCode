class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # in place = constant extra memory

        l = 1

        for r in range(1 ,len(nums)):  #right ptr increments
            if nums[r] != nums[r - 1]:  #comparing curr val to prev val
                nums[l] = nums[r]
                l += 1

        return  l


        
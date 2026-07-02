class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        # atmost 2 elements
        if len(nums) <= 2:
            return len(nums)

        # ptr for the position to place the next valid ele
        k = 2

        # checking from the third ele
        for i in range(2, len(nums)):
            #keep element only if its diff from the ele two positions before k
            if nums[i] != nums[k - 2]:
                nums[k] = nums[i]
                k += 1

        return k
        
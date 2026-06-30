class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        low = 0
        mid = 0
        high = len(nums) - 1

        while mid <= high:
            if nums[mid] == 0:   #no = 0 place at start
                nums[low], nums[mid] = nums[mid], nums[low]
                low += 1
                mid += 1
            elif nums[mid] == 1:  #no= 1 place after all 0s
                mid += 1
            else:  #no = 2
                nums[mid], nums[high] = nums[high], nums[mid]
                high -= 1
        
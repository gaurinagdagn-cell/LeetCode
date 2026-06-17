class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        #tc = O(logn) = binary search
        l , r = 0 , len(nums) - 1

        while l <= r :
            mid = (l + r) // 2

            if target == nums[mid]:
                return mid

            if target > nums[mid]:
                l = mid + 1

            else:  #target < nums[mid]
                r = mid - 1

        return l

        
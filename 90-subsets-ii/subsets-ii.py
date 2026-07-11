
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        # sort the array 
        nums.sort()

        result = []

        # backtracking function
        def backtrack(start, subset):
            result.append(subset[:])

            # generate remaining subsets
            for i in range(start, len(nums)):
                # skip duplicate ele
                if i > start and nums[i] == nums[i - 1]:
                    continue

                subset.append(nums[i])

                # recurse for the next ele
                backtrack(i + 1, subset)

                # remove the last ele
                subset.pop()

        backtrack(0, [])
        return result
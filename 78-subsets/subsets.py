class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        #backtracking problem

        ans = []       
        subset = []       

        def backtrack(index):
            #add the curr subset
            ans.append(subset[:])

            # adding each remaining element
            for i in range(index, len(nums)):
                subset.append(nums[i])      
                backtrack(i + 1)            
                subset.pop()               
        backtrack(0)
        return ans
        
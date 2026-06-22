class Solution:
    def canJump(self, nums: List[int]) -> bool:
        farthest = 0
        
        for i, jump in enumerate(nums):
            # stuck check
            if i > farthest:
                return False
            
            # max reach update
            farthest = max(farthest, i + jump)
            
            #reached end
            if farthest >= len(nums) - 1:
                return True
                
        return True
        
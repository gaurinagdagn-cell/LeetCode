class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
     #backtracking method 
        res = []

        def backtrack(i: int, cur_combination: List[int], total: int):
            #base case 1: found a valid combination
            if total == target:
                res.append(list(cur_combination))
                return
            
            # base case 2
            if total > target or i >= len(candidates):
                return
            #choice 1
            cur_combination.append(candidates[i])
            backtrack(i, cur_combination, total + candidates[i])
            
            #backtrack step
            cur_combination.pop()

            #choice 2
            backtrack(i + 1, cur_combination, total)

        backtrack(0, [], 0)
        return res
        
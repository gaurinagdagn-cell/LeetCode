class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()  #duplicate control 

        res = []
        def backtrack(curr , i , target):
            if target == 0:
                res.append(curr.copy())
            if target <= 0:
                return

            prev = -1  #hamdles skipping duplicates
            for i in range(i, len(candidates)):
                if candidates[i] == prev:
                    continue

                curr.append(candidates[i])  #adding candidate to list
                backtrack(curr , i + 1 , target - candidates[i] )  #move forward to next level of recursion
                curr.pop()  #removing the number
                prev = candidates[i]
        backtrack([] , 0 , target)
        return res
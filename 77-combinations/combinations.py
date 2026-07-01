class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        #backtracking problem

        result = []      
        combination = [] 

        def backtrack(start):
            #if the comb has k ele, add a copy 
            if len(combination) == k:
                result.append(combination[:])
                return

            # every number from start to n
            for num in range(start, n + 1):
                #choosing  curr number
                combination.append(num)

                #recur for  next nos
                backtrack(num + 1)

                combination.pop()

        #building combs from 1
        backtrack(1)

        return result
        
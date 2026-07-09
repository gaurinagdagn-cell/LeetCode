class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        #storing numbers from 1 to n
        nums = [str(i) for i in range(1, n + 1)]

        fact = 1
        for i in range(1, n + 1):
            fact *= i

        k -= 1

        ans = []

        # building the permutation one digit at a time
        for i in range(n, 0, -1):
            fact //= i                  # (i-1)!

            index = k // fact           # selecting the correct digit
            ans.append(nums[index])     # adding it to the answer

            nums.pop(index)             # remove the used digit

            k %= fact                   # remaining position within the block

        return "".join(ans)
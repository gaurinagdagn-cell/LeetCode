from typing import List

class Solution:
    def grayCode(self, n: int) -> List[int]:
        # store the gray code sequence
        result = []

        # generate all numbers from 0 to 2^n - 1
        for i in range(1 << n):
            # convert binary number to gray code
            result.append(i ^ (i >> 1))

        return result
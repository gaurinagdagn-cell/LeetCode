class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        #start from the last digit and move backwards
        for i in range(len(digits) - 1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits 
            
            #if its a 9 it goes over to 0
            digits[i] = 0
            
        return [1] + digits
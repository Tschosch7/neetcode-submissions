class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_consecutive_ones = 0
        counter = 0
        for num in nums:
            if num == 1:
                counter += 1
                if counter >= max_consecutive_ones:
                    max_consecutive_ones = counter
            else: 
                counter = 0
        return max_consecutive_ones
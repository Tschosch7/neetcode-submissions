class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        values_to_keep = []
        for num in nums:
            if num != val:
                values_to_keep.append(num)
        for i in range(len(values_to_keep)):
            nums[i] = values_to_keep[i]
        return len(values_to_keep)
class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        for i in range(len(arr)):
            max_el_to_right = -1
            for j in range(i + 1, len(arr)):
                max_el_to_right = max(max_el_to_right, arr[j])
            arr[i] = max_el_to_right
        return arr
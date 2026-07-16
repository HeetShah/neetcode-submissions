class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        freq = Counter(nums)

        result = freq.values()
        for num in result:
            if num > 1:
                return True

        return False


        
        
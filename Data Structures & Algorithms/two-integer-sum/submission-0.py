class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        complement_index = {}

        for i, num in enumerate(nums):
            complement = target - num

            if complement in complement_index:
                return [complement_index[complement], i]
            else:
                complement_index[num] = i

        return []
        
        
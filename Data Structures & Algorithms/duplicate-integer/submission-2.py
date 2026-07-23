nums = []

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        validation = []
        for i in nums:
            if i in validation: return True
            validation.append(i)
        return False

class Solution(object):
    def numIdenticalPairs(self, nums):
        count = {}
        result = 0
        for num in nums:
            result += count.get(num,0)
            count[num] = count.get(num,0)+1
        return result
        # i = 0
        # count = {}
        # for j in range(len(nums)):
        #     if nums[i] == nums[j] and i < j:
        #         i+=1
        #         count 

        """
        :type nums: List[int]
        :rtype: int
        """
        
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        count = {}
        frequency = [[] for i in range(len(nums)+1)]

        for i in nums:
            count[i] = 1 + count.get(i, 0)
        for number, count in count.items():
            frequency[count].append(number)

        results = []
        for i in range(len(frequency)-1, 0, -1):
            for number in frequency[i]:
                results.append(number)
                if len(results) == k:
                    return results

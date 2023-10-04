class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        pairs = []
        pairsDictionary = {}

        for i in range(len(strs)):
            sortedStrs = "".join(sorted(strs[i]))
            if sortedStrs in pairsDictionary:
                group = pairsDictionary[sortedStrs]
                group.append(strs[i])
                pairsDictionary.update({sortedStrs: group})
            else:
                pairsDictionary.update({sortedStrs: [strs[i]]})

        for i in pairsDictionary:
            pairs.append(pairsDictionary[i])

        return pairs

class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        solutions = {}

        def StepTree(target, count):
            if count == target:
                return 1
            elif count > target:
                return 0
            if solutions.has_key(count) == False:
                solutions[count] = StepTree(
                    target, count+1) + StepTree(target, count+2)
            return solutions[count]

        return StepTree(n, 0)

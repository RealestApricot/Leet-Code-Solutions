class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        combined = []
        left = 0
        right = 0
        while len(combined) < (m+n):
            if left >= m and right >= n:
                break
            if n <= right or ((left < m) and nums1[left] < nums2[right]):
                combined.append(nums1[left])
                left += 1
            else:
                combined.append(nums2[right])
                right += 1
        nums1[:] = combined

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # when tc in log use binary search

        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1  #binary search on smaller array

        m, n = len(nums1), len(nums2)

        left, right = 0, m

        while left <= right:
            i = (left + right) // 2

            # index for nums2
            #left half elements
            j = (m + n + 1) // 2 - i

            #elem just left and right of the partition in nums1
            left1 = float("-inf") if i == 0 else nums1[i - 1]
            right1 = float("inf") if i == m else nums1[i]

            #elem just left and right of the partition in nums2
            left2 = float("-inf") if j == 0 else nums2[j - 1]
            right2 = float("inf") if j == n else nums2[j]

            if left1 <= right2 and left2 <= right1:
                # no of ele is even
                if (m + n) % 2 == 0:
                    return (max(left1, left2) + min(right1, right2)) / 2.0
                #no of ele is odd
                else:
                    return float(max(left1, left2))

            elif left1 > right2:
                right = i - 1

            else:
                left = i + 1
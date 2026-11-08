class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        m = len(nums1)
        n = len(nums2)
        #this guarantees after this nums1 is smaller fs

        l, r = 0, m #

        while l <= r:
            i = (l + r) // 2
            j = (n + m + 1) // 2 - i

            left1 = nums1[i - 1] if i > 0 else float("-inf")
            right1 = nums1[i] if i < m else float("inf")

            left2 = nums2[j - 1] if j > 0 else float("-inf")
            right2 = nums2[j] if j < n else float("inf")

            if left1 <= right2 and left2 <= right1:
                #now we can return either even or odd
                #odd
                if (n + m) % 2 == 1:
                    return max(left1, left2)
                
                else:
                    return (max(left1, left2) + min(right1, right2)) / 2
            elif left1 > right2:
                r = i - 1
            else:
                l = i + 1
        
        return -1
            
'''
Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.
The overall run time complexity should be O(log (m+n)).


Example 1:
Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.

Example 2:
Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
'''

def findMedianSortedArrays(nums1, nums2):
    if len(nums1) >= len(nums2):
        left, right = nums1, nums2
    else:
        left, right = nums2, nums1

    m, n = len(left), len(right)
    single = True if (m+n) % 2 != 0 else False
    ls = (m+n)/2 if single else (m+n+1)/2

    l, r = 0, 0
    result = []
    while ls >= 0:
        if r == n:
            result.append(left[l])
            l += 1
        elif l == m:
            result.append(right[r])
            r += 1
        else:
            if left[l] <= right[r]:
                result.append(left[l])
                l += 1
            else:
                result.append(right[r])
                r += 1

        ls -= 1

    median = result[-1] if single else (result[-1] + result[-2])/2

    return median
nums1=[1,3]
nums2=[2]
print(findMedianSortedArrays(nums1, nums2))

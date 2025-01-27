def findMedianSortedArrays(nums1, nums2):
    import math
    combine = nums1 + nums2
    length = len(combine)
    combine.sort()
    median = 0

    if length % 2 == 0:
        ind = length // 2
        median = (combine[ind - 1] + combine[ind]) / 2
    else:
        ind = math.floor(length / 2)
        median = combine[ind]

    return median

print(findMedianSortedArrays([1,3], [2]))
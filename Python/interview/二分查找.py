# -*- coding: UTF-8 -*-
"""二分查找，适用于已经排序好的数组，适合在排序好的数组中找到一个数字，利用排序的优势
最坏情况是O(logN)"""

def binarySearch(l, t):
    low, high = 0, len(l) - 1
    while low < high:
        # print low, high
        mid = (low + high) / 2
        if l[mid] > t:
            high = mid
        elif l[mid] < t:
            low = mid + 1
        else:
            return mid
    return low if l[low] == t else False

if __name__ == '__main__':
    l = [1, 4, 12, 45, 66, 99, 120, 444]
    print binarySearch(l, 12)
    print binarySearch(l, 1)
    print binarySearch(l, 13)
    print binarySearch(l, 444)
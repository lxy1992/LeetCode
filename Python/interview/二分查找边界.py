def bin_search(tar, l):
    low, high = 0, len(l) - 1
    while low <= high:
        mid = (low + high) / 2
        if l[mid] == tar:
            right, left = bin_search_right(tar, l, low=mid, high=high), bin_search_left(tar, l, low=low, high=mid)
            if right < left:
                return -1
            else:
                return [left, right]
        elif l[mid] < tar:
            low = mid + 1
        else:
            high = mid - 1


def bin_search_left(tar, l, low, high):
    while low <= high:
        mid = (low + high) / 2
        if l[mid] == tar:
            high = mid - 1
        else:
            low = mid + 1
    l_range = [low, high]
    print "left: {__range}" .format(__range=l_range)
    return low


def bin_search_right(tar, l, low, high):
    while low <= high:
        mid = (low + high) / 2
        if l[mid] > tar:
            high = mid - 1
        else:
            low = mid + 1
    r_range = [low, high]
    print "right: {rrange}".format(rrange=r_range)
    return high


if __name__ == '__main__':
    A = [1,1]
    print("Input:", A)
    print("Output:", bin_search(1, A))


    # Input: [1, 4, 4, 4, 4, 4, 6, 6]
    # Output: (1, 5)
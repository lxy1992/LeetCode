def single(arr):
    for i in xrange(0, len(arr), 2):
        print arr[i], arr[i+1]
        if arr[i] != arr[i+1]:
            return arr[i]


if __name__ == '__main__':
    a1 = [1, 1, 2, 3, 3, 4, 4, 8, 8]
    print single(a1)

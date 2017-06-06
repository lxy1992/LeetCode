
import sys


if __name__ == '__main__':
    numbers = (str(sys.stdin.readline().strip())).split(' ')
    # number = numbers.split(' ')
    sum_of_numbers = int(numbers[0])
    length = int(numbers[1])
    out = ""
    for i in xrange(length, 101):
        print i
        a = (2*sum_of_numbers)-(i*i)+i
        b = 2*i
        print a % b
        if a % b is 0:
            a1 = a/b
            for j in xrange(a1, a1+i):
                out = out.__add__(str(j))
                out = out.__add__(" ")

            out = out[:-1]
            print out
            break
    if out is "":
        print "No"






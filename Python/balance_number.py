#coding = utf-8
import sys

if __name__ == "__main__":

    line = sys.stdin.readline().strip()
    numbers = [int(line[item:item + 1]) for item in range(0, len(line))]
    lft = numbers[0]
    rit = numbers[len(numbers) - 1]
    if len(line) < 4:
        print "NO"
    for j in range(1, len(numbers) - 2):
        lft *= numbers[j]
        for k in range(len(numbers) - 1, j, -1):
            rit *= numbers[k]
    if lft == rit:
        print "YES"
    else:
        print "NO"








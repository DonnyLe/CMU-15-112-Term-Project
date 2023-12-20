import random, copy, time

def merge(a, i, j, k, step):
    index1 = i
    index2 = j
    length = k - i
    b = [None] * length
    for index in range(length):
        if index1 == j:
            b[index] = a[index2]
            index2 += 1
        elif (index2 != k and (a[index1] > a[index2])):
            b[index] = a[index2]
            index2 += 1
        elif index1 != j:
            b[index] = a[index1]
            index1 += 1
    for index in range(i, k):
        a[index] = b[index - i]

def mergeSort(a):
    n = 1
    while (n < len(a)):
        for start1 in range(0, len(a), 2*n):
            start2 = min(start1 + n, len(a))
            end = min(start1 + 2*n, len(a))
            merge(a, start1, start2, end, n)
        n *= 2

def testSort(sortFn, n):
    a = [random.randint(0,2**31) for i in range(n)]
    sortedA = sorted(a)
    sortFn(a)
    assert(a == sortedA)


def testSorts():
    n = 2**13
    print("Testing...", end = '')
    for i in range(10):
        testSort(mergeSort, n)
    print("Passed!")

testSorts()
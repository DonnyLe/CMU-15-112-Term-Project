import copy

def merge1(a, start1, start2, end):
    index1 = start1
    index2 = start2
    length = end - start1
    aux = [None] * length
    for i in range(length):
        if ((index1 == start2) or
            ((index2 != end) and (a[index1] > a[index2]))):
            aux[i] = a[index2]
            index2 += 1
        else:
            aux[i] = a[index1]
            index1 += 1
    for i in range(start1, end):
        a[i] = aux[i - start1]

def mergeSort1(a):
    n = len(a)
    step = 1
    while (step < n - 1):
        for start1 in range(0, n, 2*step):
            start2 = min(start1 + step, n)
            end = min(start1 + 2*step, n)
            merge1(a, start1, start2, end)
        step *= 2

def merge2(a, start1, start2, end):
    index1 = start1
    index2 = start2
    length = end - start1
    aux = [None] * length
    for i in range(length):
        if ((index1 == start2) or
            ((index2 != end) and (a[index1] > a[index2]))):
            aux[i] = a[index2]
            index2 += 1
        else:
            aux[i] = a[index1]
            index1 += 1
    for i in range(start1, end):
        a[i] = aux[i - start1]

def mergeSort2(a):
    n = len(a)
    step = 1
    while (step < n):
        for start1 in range(1, n, 2*step):
            start2 = min(start1 + step, n)
            end = min(start1 + 2*step, n)
            merge2(a, start1, start2, end)
        step *= 2

def merge3(a, start1, start2, end):
    index1 = start1
    index2 = start2
    length = end - start1
    aux = [None] * length
    for i in range(length):
        if ((index1 == start2) or
            ((index2 != end) and (a[index1] > a[index2]))):
            aux[i] = a[index2]
            index2 += 1
        else:
            aux[i] = a[index1]
            index1 += 1
    for i in range(start1, end):
        a[i] = aux[i - start1]

def mergeSort3(a):
    n = len(a)
    step = 1
    while (step < n):
        s = 0
        while s < n:
            end = min(s + 2*step, n)
            start2 = min(s + step, n)
            merge3(a, s, start2, end)
            s += step + step
        step *= 2

def merge4(a, start1, start2, end):
    index1 = start1
    index2 = start2
    length = end - start1
    aux = [None] * length
    for i in range(length):
        if (index1 == start2 - 1 and index2 == end - 1):
            aux[i] = a[index1]
            index1 += 1
        elif ((index1 == start2) or
            ((index2 != end) and (a[index1] > a[index2]))):
            aux[i] = a[index2]
            index2 += 1
        else:
            aux[i] = a[index1]
            index1 += 1
    for i in range(start1, end):
        a[i] = aux[i - start1]

def mergeSort4(a):
    n = len(a)
    step = 1
    while (step < n):
        for start1 in range(0, n, 2*step):
            start2 = min(start1 + step, n)
            end = min(start1 + 2*step, n)
            merge4(a, start1, start2, end)
        step *= 2

def swap(a, i, j):
    (a[i], a[j]) = (a[j], a[i])

def selectionSort1(a):
    n = len(a)
    for startIndex in range(n - 1):
        minIndex = startIndex
        for i in range(startIndex, n):
            if (a[i] < a[minIndex]):
                minIndex = i
        swap(a, startIndex, minIndex)

def quickSort1(L,i,j):
    if j-i<1: return
    k=L[i]
    L[i]=L[j]
    m,n=i,j
    while i-j:
        while L[i]<=k and i<=n and i<j: i+=1
        L[j]=L[i]
        while L[j]>=k and j>=m and j>i: j-=1
        L[i]=L[j]
    L[i]=k
    quickSort1(L,m,i)
    quickSort1(L,i+1,n)

def quickSortLoop1(L):
    index=[]
    index.append((0,len(L)-1))
    while index!=[]:
        i,j=index.pop()
        if i>=j: continue
        m,n=i,j
        k=L[i]
        L[i]=L[j]
        while i-j:
            while L[i]<k and i<=n and i<j: i+=1
            L[j]=L[i]
            while L[j]>=k and j>=m and j>i: j-=1
            L[i]=L[j]
        L[i]=k
        index.append((m,i))
        index.append((i+1,n))

def quickSort2(L,i,j):
    if j-i<3: return
    k=L[i]
    L[i]=L[j]
    m,n=i,j
    while i-j:
        while L[i]<k and i<=n and i<j: i+=1
        L[j]=L[i]
        while L[j]>=k and j>=m and j>i: j-=1
        L[i]=L[j]
    L[i]=k
    quickSort2(L,m,i)
    quickSort2(L,i+1,n)

def quickSortLoop2(L):
    index=[]
    index.append((0,min(10, len(L)-1)))
    while index!=[]:
        i,j=index.pop()
        if i>=j: continue
        m,n=i,j
        k=L[i]
        L[i]=L[j]
        while i-j:
            while L[i]<k and i<=n and i<j: i+=1
            L[j]=L[i]
            while L[j]>=k and j>=m and j>i: j-=1
            L[i]=L[j]
        L[i]=k
        index.append((m,i))
        index.append((i+1,n))

def quickSortLoop3(L):
    flag = True
    lst = copy.deepcopy(L)
    index=[]
    index.append((0,len(L)-1))
    while index!=[]:
        i,j=index.pop()
        if i>=j: continue
        m,n=i,j
        k=L[i]
        L[i]=L[j]
        while i-j:
            while L[i]<k and i<=n and i<j: i+=1
            L[j]=L[i]
            while L[j]>=k and j>=m and j>i: j-=1
            L[i]=L[j]
        L[i]=k
        if L != lst:
            flag = False
        index.append((m,i))
        index.append((i+1,n))
    if flag: L.pop()

def testSort(lst):
    if lst == []:
        print("You need to add test cases!")
        return
    check = [True] * 10
    for i in range(len(lst)):
        L = copy.deepcopy(lst[i])
        sortedL = sorted(L)
        mergeSort1(L)
        if (L != sortedL):
            check[0] = False
            print(f"sort1 failed on test case #{i + 1}!")
        L = copy.deepcopy(lst[i])
        mergeSort2(L)
        if (L != sortedL):
            check[1] = False
            print(f"sort2 failed on test case #{i + 1}!")
        L = copy.deepcopy(lst[i])
        mergeSort3(L)
        if (L != sortedL):
            check[2] = False
            print(f"sort3 failed on test case #{i + 1}!")
        L = copy.deepcopy(lst[i])
        mergeSort4(L)
        if (L != sortedL):
            check[3] = False
            print(f"sort4 failed on test case #{i + 1}!")
        L = copy.deepcopy(lst[i])
        selectionSort1(L)
        if (L != sortedL):
            check[4] = False
            print(f"sort5 failed on test case #{i + 1}!")
        L = copy.deepcopy(lst[i])
        try:
            quickSort1(L, 0, len(L) - 1)
        except:
            check[5] = False
            print(f"sort6 failed on test case #{i + 1}!")
        if (L != sortedL):
            check[5] = False
            print(f"sort6 failed on test case #{i + 1}!")
        L = copy.deepcopy(lst[i])
        quickSortLoop1(L)
        if (L != sortedL):
            check[6] = False
            print(f"sort7 failed on test case #{i + 1}!")
        L = copy.deepcopy(lst[i])
        quickSort2(L, 0, len(L) - 1)
        if (L != sortedL):
            check[7] = False
            print(f"sort8 failed on test case #{i + 1}!")
        L = copy.deepcopy(lst[i])
        quickSortLoop2(L)
        if (L != sortedL):
            check[8] = False
            print(f"sort9 failed on test case #{i + 1}!")
        L = copy.deepcopy(lst[i])
        quickSortLoop3(L)
        if (L != sortedL):
            check[9] = False
            print(f"sort10 failed on test case #{i + 1}!")
    print("Testing finished. Your overall testing result:")
    print(check)

def test():
    # add your test cases as lists in a 2d list here!
    L = [] 
    testSort(L)
    print("End.")

test()
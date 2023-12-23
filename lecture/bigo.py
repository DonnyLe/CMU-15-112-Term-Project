#O(n)
def linearSearch(L,n):
    for item in L:
        if item == n:
            return True
    return False

#O(n)
def linearSearch(L,n):
    return n in L

#binary search 

L = [1,6,7,9, 11, 14, 17, 20]

#sorting takes O(n * log(n))

#sort + binary search 
#O(n logn + n) == O(nlogn), slower than linear search 

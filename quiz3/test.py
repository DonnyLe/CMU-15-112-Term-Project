import copy

M = [[1,2,3],[1,2,3]]
N = [[4,5,6], [7,8,9]]

M[0] = N[1]
print(f'M = {M}, N = {N}')

N[1][0] = "hello"
print(f'M = {M}, N = {N}')



# #*shallow
# M = [[1,2,3],[1,2,3]]
# A = copy.copy(M)
# M[0]= [2]
# print(A)
# print(M)
# M[1][0] = 4
# print(A)
# print(M)
# M[0][0] = 4
# print(A)
# print(M).pop()
# print(A)
# print(M)


# #*deep
# M = [[1,2,3]]
# A = copy.deepcopy(M)
# M[0][0] = 2
# print(A)

# M = [[1,2,3]]
# A = [M[0]]
# M[0][0] = 2
# print(A)

# M = [[1,2,3]]
# A = [M[0]]
# M[0][0] = 2
# print(A)

# M = [[1,2,3]]
# A = M[:]
# M[0][0] = 2
# print(A)

# M = [[1,2,3]]
# A = M*1
# M[0][0] = 2
# print(A)


# M = [1,2, 3]
# N = M
# M +=  [1]


# print(N)





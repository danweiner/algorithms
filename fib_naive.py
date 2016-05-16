# uses Python3

# naive slow algorithm
# def FibRecurs(n):
#     if n <= 1:
#         return n
#     else:
#         return FibRecurs(n - 1) + FibRecurs(n - 2)
#
# print(FibRecurs(20))


# faster algorithm

def FibList(n):
    F = list(range(0,n+1))
    if n <= 1:
        F.append(n)
    for i in range(2 , n + 1):
        F[i] = F[i - 1] + F[i - 2]
    return F[n]


print(FibList(4))
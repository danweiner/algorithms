# uses python3

# naive algorithm

# def NaiveGCD(a,b):
#     best = 0
#     total = a + b
#     for d in range(1, total + 1):
#         if a % d == 0 and b % d == 0:
#             best = d
#     return best
#
#
# print(NaiveGCD(4,24))


# Euclidean Algorithm

def EuclidGCD(a,b):
    if b == 0:
        return a

    a_prime = a % b
    print(a_prime)

    return EuclidGCD(b, a_prime)

print(EuclidGCD(357,234))

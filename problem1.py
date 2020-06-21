M = 1000
printrange = 10**10
allsum = sum(pow(n, n) for n in range(1, M+1))

print("Solution is : ", allsum % printrange)



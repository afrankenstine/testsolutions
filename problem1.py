M = 1000    
allsum = sum(pow(n, n) for n in range(1, M+1))
sol = str(allsum)
sol = sol[len(sol)-10:len(sol)]

print("Solution is : ",sol)
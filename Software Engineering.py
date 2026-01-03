arr=list(map(int,input().split()))
even=[x for x in arr if x % 2 == 0]
odd = [x for x in arr if x % 2!=0]
result=even+odd
print(result)
print(*result)

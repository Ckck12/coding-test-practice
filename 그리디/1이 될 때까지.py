n , k = map(int,input().split())

result = 0

n=7
k=3

6  2    
1  2
while n >= k:
    while n%k != 0:
        n = n-1
        result += 1
    n = n//k
    result += 1
    
while n >1:
    n= n-1
    result += 1
    
print(result)
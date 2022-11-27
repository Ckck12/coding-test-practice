n, k = map(int,input().split())

result = 0

n=7  11  19
k=3  4   4

7//3*3 = 6
11//4*4 = 8
19//4*4 = 16

7-6 = 1
3
3

while True:
    target = (n//k)*k
    result = result + (n-target)
    n = target
    
    if n<k:
        break
    result = result +1
    n = n//k
    
result = result + 1
print(result)
    
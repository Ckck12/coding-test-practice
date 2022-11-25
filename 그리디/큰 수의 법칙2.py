# n = 배열의 크기 m = 숫자가 더해지는 횟수 k = 같은 수가 최대 더해질 수 있는 횟수 
n, m ,k = map(int,input().split())
data = list(map(int,input().split()))

data.sort()

first = data[n-1]
second = data[n-2]
# 가장 큰 수가 더해지는 횟수 계산 

count_first = int((m/(k+1))*k+m%(k+1))
print(count_first)
count_second = int(m-count_first)
print(count_second)
result = 0
result = result + count_first*first + count_second*second

print(result)
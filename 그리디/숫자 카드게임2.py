n ,m = map(int,input().split())

result = 0

for i in range(n):
    data = list(map(int,input().split()))
    #현재 줄에서 가장 작은 수 찾기
    min_value = 10001 #10000까지 입력 가능하기때문에 10001을 기저값으로 둔다
    for a in data: #각 행의 원소들을 min_value와 비교하면서 변경해간다.
        min_value = min(min_value,a)
        print("최소값",min_value)

    result = max(result, min_value)
        
print(result)
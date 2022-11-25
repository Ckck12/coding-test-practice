#n,m,k  공백으로 구분하여 입력받기
n, m ,k  = map(int,input().split())
#n 개의 숫자를 공백으로 구분하여 입력 받기
data = list(map(int,input().split()))
data.sort()

first = data[n-1] #가장 큰수 선언
second = data[n-2] #두번째로 큰수 선언

result = 0

while True:
    for i in range(k): #가장 큰 수를 k번 더하기
        if m == 0: # m(더하는 횟수)가 0이면 ㅂ반복문 탈출
            break
        result += first 
        m= m-1 #더하는 횟수 하나씩 줄이기
    if m == 0: #m이 0이면 종료
        break
    
    result += second #2번째로 큰 수 더하기
    m= m-1
print(result)
#현재 나이트의 위치 입력받기
input_data = input()
row = int(input_data[1])
column = int(ord(input_data[0])) - int(ord('a'))+1

steps = [(-2,-1), (-1,-2), (1,-2),(2,-1),(2,1),(1,2),(-1,2),(-2,1)]

result = 0

for step in steps:
    nrow = row + step[0]
    ncolumn = column + step[1]
    if nrow >=1 and nrow <=8 and ncolumn >=1 and ncolumn <=8:
        result +=1
        
print(result)
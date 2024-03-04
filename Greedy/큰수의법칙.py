# N, M, K를 공백으로 구분하여 입력받기
n, m, k = map(int, input().split())
# N개의 수를 공백으로 구분하여 입력받기
data = list(map(int, input().split()))

data.sort() # 입력받은 수를 정렬하기
first = data[n-1] # 가장 큰 수
second = data[n-2]

result = 0

while True:
    for i in range(k):
      if m == 0:
        	break
      result += first
      m -= 1
    if m == 0:
    	break
    result += second # 두 번째로 큰 수를 한 번 더하기
    m -= 1

print(result)

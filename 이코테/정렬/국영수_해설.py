n = int(input())
students = []

for _ in range(n):
    students.append(input().split())

'''
[정렬 기준]
1) 두 번째 원소를 기준으로 내림차순 정렬
2) 두 번째 원소가 같은 경우, 세 번째 원소를 기준으로 오름차순 정렬
3) 세 번째 원소가 같은 경우, 네 번째 원소를 기준으로 내림차순 정렬
4) 네 번째 원소가 같은 경우, 첫 번째 원소를 기준으로 오름차순 정렬
'''
students.sort(key = lambda x: (-int(x[1]), int(x[2]), -int(x[3]), x[0])

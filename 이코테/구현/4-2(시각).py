# H를 입력받기
h = int(input())

count = 0
for i in range(h + 1):
    for h in range(60):
        for k in range(60):
            if '3' in str(i) + str(j) + str(k):
                count += 1

print(count)
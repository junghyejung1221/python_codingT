n = int(input())

print(n)

count = 0

for h in range(n+1):
    for m in range(60):
        for s in range(60):
            # 숫자를 더하는 것이 아닌 시간 처럼 합쳐서 그 중 3 이 있는 지 검사
            if '3' in str(h) + str(m) + str(s):
                print(f'{str(h)}시 + {str(m)}분 + {str(s)}초')
                count +=1
print(count)
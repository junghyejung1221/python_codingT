
# 큰수의 법칙
# n개의 주어진 수를 총 m번 더할때 주어진 수중 가장 큰 합
# 하지만 수가 k번 연속 되면 안된다.

n,m,k = map(int, input().split())

data = list(map(int, input().split()))
# for i in range(n):
#     print(f'{i}입력')

data.sort()

first = data[n-1]
second = data[n-2]

print(f'{first},  {second}')

sum = 0
count = 0
for i in range(m):
    if count != k:
        sum += first
        count +=1
        print(f'sum {i}, count{count},  {first}더한 합은 {sum}')
    else:
        count = 0
        sum += second
        print(f'sum {i}, count{count},  {second}더한 합은 {sum}')

print(data)

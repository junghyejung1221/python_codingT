# 숫자가 쓰인 카드 N X M 형태
# 각행 마다 가장 작은 수를 뽑고 그중 가장 큰수를 찾아내기
n,m = map(int, input().split())

list1 = []
result = 0

for i in range(n):
    list1.append(list(map(int, input().split())))

    min_value = min(list1[i])
    # print(f'min, {min_value}')
    result = max(min_value,result)

print(f'result, {result}')



# 어떠한 수 N이 1이 될때까지 두과정 중 하나를 반복 하려고 할때
# 1. N에서 1을 뺀다
# 2. N을 K로 나눈다 (N이 나누어 떨어져야 함)
# N을 1로 만드는 최소 횟수를 구해라

n,k = map(int, input().split())

count = 0

while n >= k:
    while (n % k) != 0:
        n -=1
        count += 1
        print(f'1빼기, {n}  count,{count}')
    n =  n/k
    count +=1
    print(f'k로 나누기, {n}  count,{count}')

while n>1:
    n -= 1
    count +=1
    print(f'1빼기, {n}  count,{count}')
print(count)

n = 2420
count = 0

# 큰 단위의 화폐부터 차례대로 확인?
list1 = [500,100,50,10]

for coin in list1:
    print(f'{n}원 일 대 거스름 개수 coin, {coin}  count ,{count}')
    count +=     n // coin  # 해당 화폐로 거슬러 줄 수 있는 동전의 개수 새기
    n %= coin


print(count)
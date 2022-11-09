data = input()
# ord a 는 97이다
# print(ord(data[0]))



datax = data[1]
datay = ord(data[0]) - 96

count = 0

# print(datax, datay)

# 8방향 다확인
x = int(datax) + 2
y = int(datay) + 1
if  1<= x<= 8 and 1<=y<=8 :
    count += 1

x = int(datax) + 2
y = int(datay) - 1
if  1<= x<= 8 and 1<=y<=8 :
    count += 1

x = int(datax) - 2
y = int(datay) + 1
if 1 <= x <= 8 and 1 <= y <= 8:
    count += 1

x = int(datax) - 2
y = int(datay) - 1
if 1 <= x <= 8 and 1 <= y <= 8:
    count += 1

x = int(datax) + 1
y = int(datay) + 2
if 1 <= x <= 8 and 1 <= y <= 8:
    count += 1

x = int(datax) + 1
y = int(datay) - 2
if 1 <= x <= 8 and 1 <= y <= 8:
    count += 1

x = int(datax) - 1
y = int(datay) + 2
if 1 <= x <= 8 and 1 <= y <= 8:
    count += 1

x = int(datax) - 1
y = int(datay) - 2
if 1 <= x <= 8 and 1 <= y <= 8:
    count += 1

print(count)
n = int(input())

print(n)

data = input().split()

print(data)

run = ['L', 'R', 'U', 'D']
dx = 1
dy = 1

print(len(data))

for i in range(len(data)):
        if data[i] == run[0]:
            if dy != 1:
                dy -=1
            print(f'{i+1}번째 {dx} {dy}')
        elif data[i] == run[1]:
            if dy != n:
                dy +=1
            print(f'{i+1}번째 {dx} {dy}')
        elif data[i] == run[2]:
            if dx != 1:
                dx -= 1
            print(f'{i+1}번째 {dx} {dy}')
        elif data[i] == run[3]:
            if dx != n:
                dx += 1
            print(f'{i+1}번째 {dx} {dy}')

print(f'{dx} {dy}')

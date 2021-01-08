# n이 주어졌울 때, 1부터 n까지 합을 구하기
n = int(input())
sum = 0

for i in range(1, n+1):
    sum += i
print(sum)
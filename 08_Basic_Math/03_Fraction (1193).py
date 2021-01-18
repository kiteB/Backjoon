# 무한히 큰 배열에 분수들이 적혀져 있을 때, 지그재그 순서로 차례대로 1번, 2번, ... 분수라고 하자.
# X가 주어졌을 때, X번째 분수를 구하는 프로그램을 작성하시오.
X = int(input())
line = 1

while X > line:
    X -= line
    line += 1

# line이 짝수일 때,
if line % 2 == 0:
    # 분자 오름차순, 분모 내림차순
    a = X
    b = line-X+1
# line이 홀수일 때,
else:
    # 분자 내림차순, 분모 오름차순
    a = line-X+1
    b = X

print('{}/{}'.format(a, b))



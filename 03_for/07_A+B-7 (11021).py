# 두 정수 A, B를 입력받ㅇ느 다음, A+B를 출력하는 프로그램 작성
n = int(input())

for i in range(1, n+1):
    a, b = map(int, input().split())
    print('Case #{0}: {1}'.format(i, a+b))
# 두 정수 A, B가 주어졌을 때, A와 B를 비교하는 프로그램 작성하기

a, b = map(int, input().split())

if a < b:
    print('<')
elif a > b:
    print('>')
else:
    print('==')
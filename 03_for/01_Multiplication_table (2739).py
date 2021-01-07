# N을 입력받은 뒤, 구구단 N단을 출력하는 프로그램 만들기
n = int(input())

for i in range(1, 10):
    print('{0} * {1} = {2}'.format(n, i, n*i))
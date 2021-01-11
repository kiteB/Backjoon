# 두 정수 A, B를 입력받은 다음, A+B를 출력하는 프로그램 작성하기
# 입력이 끝날 때까지 출력하라
while True:
    try:
        a, b = map(int, input().split())
        print(a+b)
    except EOFError:
        break
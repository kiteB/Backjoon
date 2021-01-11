# 두 정수 A, B를 입력받은 다음, A+B를 출력하는 프로그램 작성하기
# 입력의 마지막에는 0이 두 개가 들어온다. 0이 두 개 들어오기 전까지 두 수의 합을 출력하라
while True:
    a, b = map(int, input().split())

    if a == 0 and b == 0:
        break
    else:
        print(a+b)
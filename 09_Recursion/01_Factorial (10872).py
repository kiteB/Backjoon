# 0보다 크거나 같은 정수 N이 주어진다. 이때 N!을 출력하는 프로그램을 작성하시오.
def factorial(N):
    if N == 0 or N == 1:
        return 1
    else:
        return factorial(N-1) * N


print(factorial(int(input())))
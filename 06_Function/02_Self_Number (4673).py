# 양의 정수 n에 대해서 d(n)을 n과 n의 각 자릿수를 더하는 함수.
# 양의 정수 n이 주어졌을 때, 이 수를 시작해서 n, d(n), d(d(n)), ... 과 같은 무한 수열을 만들 수 있다.
# n을 d(n)의 생성자라고 한다. 생성자가 없는 숫자를 셀프 넘버라고 한다.
# 100보다 작은 셀프 넘버는 총 13개가 있다. (1, 3, 5, 7, 9, 20, 31, 42, 53, 64, 75, 86, 97)
# 10000보다 작거나 같은 셀프 넘버를 한 줄에 하나씩 출력하는 프로그램을 작성하시오.
def d(n):
    result = n

    while n != 0:
        result += n%10  # 10으로 나눈 나머지
        n //= 10        # 10으로 나누었을 때 몫
    return result

numbers = []    # Self Number를 저장할 리스트
for i in range(1, 10001):
    numbers.append(d(i))
    if i not in numbers:
        print(i)
# 두 수 A, B가 주어질 때, 두 수는 같지 않은 세 자리 수이며 0이 포함되어 있지 않다.
# 상수는 수를 다른 사람과 다르게 거꾸로 읽는다. Ex. 734 -> 437, 893 -> 398
# 상수는 두 수가 주어졌을 때, 바꿔읽은 수의 크기를 비교해서 대답한다. 상수의 대답을 출력하는 프로그램일 작성하라.
A, B = map(list, map(str, input().split()))
A.reverse()
B.reverse()

strA = ''.join(A)
strB = ''.join(B)

print(max(strA, strB))
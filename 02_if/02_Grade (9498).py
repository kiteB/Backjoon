# 시험 점수를 입력받을 때, 시험 성적을 출력하기
a = int(input())

if a >= 90:
    print('A')
elif a >= 80:
    print('B')
elif a >= 70:
    print('C')
elif a >= 60:
    print('D')
else:
    print('F')
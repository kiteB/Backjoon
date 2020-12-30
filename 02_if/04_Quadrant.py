# 좌표를 입력받을 때, 사분면 번호를 출력하기
x = int(input())
y = int(input())

if x > 0 and y > 0:
    print('1')
elif x < 0 and y > 0:
    print('2')
elif x < 0 and y < 0:
    print('3')
else:
    print('4')
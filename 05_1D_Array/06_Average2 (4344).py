# 첫째 줄에는 테스트 케이스 개수 C가 주어진다.
# 입력: 둘째 줄부터 각 테스트 케이스마다 학생의 수가 첫 수로 주어지고, 이어서 N명의 점수가 주어진다.
# 점수는 0보다 크거나 같고, 100보다 작거나 같은 정수이다.
# 출력: 각 케이스마다 한 줄씩 평균을 넘는 학생들의 비율을 반올림하여 소수점 셋째 자리까지 출력하라.
C = int(input())

for i in range(C):
    case = list(map(int, input().split()))
    count = 0

    # 학생 수와 성적 분리
    student = case[0]
    score = case[1:len(case)]

    avg = sum(score) / len(score)

    for i in range(len(score)):
        if score[i] > avg:
            count += 1

    print('{:.3f}%'.format(count / student * 100))
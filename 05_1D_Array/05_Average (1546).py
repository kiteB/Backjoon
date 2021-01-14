# 첫째 줄에 시험 본 과목의 개수 N이 주어진다. (이 값은 1000보다 작거나 같다.)
# 둘째 줄에 현재 성적이 주어진다. (이 값은 100보다 작거나 같은 음이 아닌 정수이며, 적어도 하나의 값은 0보다 크다.)
# 현재 성적 중 최댓값을 M이라고 하고, 모든 점수를 점수/M*100으로 고친다.
N = int(input())
score = list(map(int, input().split()))
best = max(score)
result = []

for i in range(len(score)):
    result.append(score[i] / best * 100)

print(sum(result) / N)
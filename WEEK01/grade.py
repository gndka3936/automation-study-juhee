# 과제 2 성적 처리
# 학생 5명의 점수를 관리
# 점수에 따라 A / B / C / D 등급 출력

stu_score = [90, 40, 60, 20, 100]

for score in stu_score:
    if score >= 90:
        print(score, "점: A")
    elif score >= 80:
        print(score, "점: B")
    elif score >= 70:
        print(score, "점: C")
    else:
        print(score, "점: D")

# 전체 평균 계산
print("전체 평균:",sum(stu_score) / len(stu_score))

# 최고점 / 최저점 출력
print("최저점:",min(stu_score))
print("최고점:",max(stu_score))
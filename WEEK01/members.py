# 과제 3 회원 정보 관리
# 요구사항 회원 3명의 다음 정보를 관리합니다.

members = [
    {"name": "케로로", "age": 25, "region": "대전"},
    {"name": "도로로", "age": 32, "region": "부산"},
    {"name": "타마마", "age": 11, "region": "제주"}
]

# 전체 회원 정보 출력
print("전체 회원 정보")
for member in members:
    print(member["name"], member["age"], member["region"])

# 30세 이상 회원만 별도로 출력
print("30세 이상 회원")
for member in members:
    if member["age"] >= 30:
        print(member["name"], member["age"], member["region"])
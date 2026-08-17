# 과제 1 사직연산 계산기
# 사용자에게 숫자 2개 입력받기
# 프로그램이 오류로 종료되지 않도록 구현

try:
    x = int(input("숫자를 입력하세요: "))
    y = int(input("숫자를 입력하세요: ")) 
except:
    print("숫자 이외의 문자는 입력할 수 없습니다.")
    exit()

def cal_plus(x, y):
    return x + y

def cal_minus(x, y):
    return x - y

def cal_multiple(x, y):
    return x * y

def cal_division(x, y):
    # 0으로 나누는 상황 처리
    if y == 0:
        return "0으로 나눌 수 없습니다."
    return x / y

# 더하기 빼기 곱하기 나누기 결과 출력
print(cal_plus(x, y))
print(cal_minus(x, y))
print(cal_multiple(x, y))
print(cal_division(x, y))
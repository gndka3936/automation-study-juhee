import gugudan
import palindrome
import frequency
import password
import name
import menu

# 구구단 출력
number = int(input("구구단 몇단?: "))
result = gugudan.gugudan(number)

# 회문 판별
text = input("회문인지 확인할 단어 입력: ")
result2 = palindrome.palindrome(text)
print(result2)

# 단어 빈도 계산
text = input("단어 목록 입력: ")
result3 = frequency.frequency(text)

# 비밀번호 검증
PW = input("비밀번호 입력: ")
result4 = password.password(PW)
print(result4)

# 이름 목록 정리
text = input("이름 목록 입력: ").split(",")
result5 = name.names(text)
print(result5)

# 간단한 메뉴 프로그램
menu.menu()
#문자열을 처리하는 공통 기능을 별도의 모듈로 작성합니다.

# 문자열 앞뒤 공백 제거 및 소문자 변환
def utils1(text): 
    text = text.strip()
    text = text.lower()
    return text

# 이메일 형태 확인
def utils2(email):
    is_email = "@" in email
    return is_email

# 이메일 일부 마스킹
def utils3(email):
    email = email.replace("abc", "###")
    return email

# 문장의 단어 개수 계산
def utils4(text):
    text = text.split()
    return len(text)

# 문자열을 반대로 변환
def utils5(text):
    return text[::-1]
import string_utils

text = input("문자열을 입력하세요: ")
email = input("이메일을 입력하세요: ")

result1 = string_utils.utils1(text)
result2 = string_utils.utils2(email)
result3 = string_utils.utils3(email)
result4 = string_utils.utils4(text)
result5 = string_utils.utils5(text)

print(result1, result2, result3, result4, result5)
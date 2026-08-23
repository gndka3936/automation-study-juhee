def password(PW):
    if len(PW) < 8:
        return "8자리 이상 입력해주세요"

    has_number = False
    has_letter = False

    for char in PW:
        if char in "0123456789":
            has_number = True

    for char in PW:
        if char in "abcdefghijklmnopqrstuvwz":
            has_letter = True

    if has_number and has_letter:
        return "사용 가능한 비밀번호"

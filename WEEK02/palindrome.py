def palindrome(text):
    if text == text[::-1]:
        return True
    else:
        return False
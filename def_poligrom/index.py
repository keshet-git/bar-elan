def is_palindrome(s):
    cleaned_s = ''.join(s.split()).lower()
    return cleaned_s == cleaned_s[::-1]

print(is_palindrome("radafffr"))
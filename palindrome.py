
# def is_palindrome(s):
#     return 1 if s == s[::-1] else 0

# s = "madam"
# print(is_palindrome(s))        # 1
# print(is_palindrome("hello"))  # 0


# def is_palindrome(s):
#     if s == s[::-1]:
#         return 1
#     else:
#         return 0
    
# print(is_palindrome("hello"))  # 0
# print(is_palindrome("madam"))  # 1


def is_palindrome(s):
     return s == s[::-1]

s = "madam"
print(is_palindrome(s))  #True
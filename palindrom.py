def isPalindrome(s):
    rev = ''.join(reversed(s))
    if (s == rev):
        return True
    return False
s = input("type any value")
ans = isPalindrome(s)

if (ans):
    print("this is a palindrom")
else:
    print("this is not a palindrom")

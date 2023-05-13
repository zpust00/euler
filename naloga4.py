
stevilka1 = 999
stevilka2 = 999

def isPalindrome(num):
    return str(num) == str(num)[::-1]

palindrome = 0
while stevilka1 >= 100 and stevilka2 >= 100:
    num = stevilka1 * stevilka2
    if isPalindrome(num) and num > palindrome:
        palindrome = num
    if stevilka1 == 100:
        stevilka2 -= 1
        stevilka1 = 999
    else:
        stevilka1 -= 1

print(palindrome)
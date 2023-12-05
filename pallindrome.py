# def isPalindrome(s):
#     return s == s[::-1]
#
# # Driver code
# s = "malayalam"
# ans = isPalindrome(s)
#
# if ans:
#     print("Yes")
# else:
#     print("No")

#************
x = "malayalam"

w = ""
for i in x:
    w = i + w

if (x == w):
    print("Yes")
else:
    print("No")
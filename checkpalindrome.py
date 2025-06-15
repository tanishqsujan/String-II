def reverse(s):
    n= len(s)
    #converting string to list
    li= list(s)
    for i in range(n//2):
        #swapping first and last, second and second last ans so on
        li[i], li[n-i-1] = li[n-i-1], li[i]
    return "".join(li)


def check_palindrome(s):
    #ignoring the case
    s= s.lower()
    rev_string= reverse(s)
    if s == rev_string:
        return True
    else:
        return False
    
inp= input("Enter String: ")
print(check_palindrome(inp))
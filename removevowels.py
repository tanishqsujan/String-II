def remove_vowel(s):
    result = ""
    #list containing vowels
    li = ['a', 'e', 'i', 'o', 'u']
    for i in range(len(s)):
        #checking the presence of vowel in the string
        if s[i] in li:
            #removing vowels
            result = result + ""
        else:
            result = result + s[i]
    
    return result

inp = input("Enter the String: ")
print("Result: ", remove_vowel(inp))
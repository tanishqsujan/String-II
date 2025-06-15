def change_the_case(s):
    result = ""
    
    for i in s:
        #changing from lower to upper case
        if i.islower():
            result = result + i.upper()
        #change from upper to lower case    
        if i.isupper():
            result = result + i.lower()
            
    return result
            
inp= input("Enter the String: ")
print("String after change:\n")
print(change_the_case(inp))
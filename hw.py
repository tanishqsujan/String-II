def clean_string(input_string):
    cleaned = input_string.replace(" ", "").replace("\n", "").replace("\t", "")
    return cleaned

input_text = """  Hello,  
    this is a  test
string with    spaces, tabs\tand newlines.\n"""
print("Original string:")
print(repr(input_text))

cleaned_text = clean_string(input_text)
print("\nCleaned string:")
print(repr(cleaned_text))

#1. Remove first n characters from a string. ( use functionremove_chars()) 
def functionremove_char(string,n):
    return string[n:]
text = "hello World"
hello =text[:1]
result = functionremove_char(text,1)
print(result)
print(hello)
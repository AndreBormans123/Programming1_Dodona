def remove(string):
    newstring = ""
    for ch in string:
        if ch >= 'a' and ch <= 'z' or ch >= 'A' and ch <= 'Z':
            newstring += ch
        else:
            newstring += " "
        
    return newstring

string = "ph@t l00t"
print(remove(string))
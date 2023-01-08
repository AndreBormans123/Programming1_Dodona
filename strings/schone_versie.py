def clean_string(string):
    clean_string = ""
    for ch in string:
        if ch >= 'a' and ch <= 'z' or ch >= 'A' and ch <= 'Z':
            clean_string += ch.lower()
    return clean_string

def print_words(string):
    words = string.split()
    for word in words:
        print(clean_string(word))

string = "Ik heb zo'n honger."
print_words(string)

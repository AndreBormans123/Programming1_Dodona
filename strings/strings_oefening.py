string1 = "The Holy Grail"
string2 = "Life of Brian"

common_chars = ""

for i in range(0, len(string1)):
    for x in range(0, len(string2)):
        if string1[i] == string2[x]:
            common_chars += string1[i].strip()

print(common_chars)

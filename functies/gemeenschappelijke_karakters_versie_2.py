# https://dodona.ugent.be/nl/courses/1286/series/14349/activities/1590800482


def gemeenschappelijke_karakters(str1, str2):
    for i in str1:
        for x in str2:
            if i == x:
                gem = 1
                break
  
    return gem


if __name__ == '__main__':
    print(gemeenschappelijke_karakters("een", "twee"))
    


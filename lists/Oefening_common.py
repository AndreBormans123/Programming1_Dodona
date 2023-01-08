list1 = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
list2 =  ['Green', 'White', 'Black']

for word in range(0, len(list1)):
    for word2 in range(0, len(list2)):
        if list1[word] == list2[word2]:
            common = True
            print(common)
            exit()
        else:
            common = False

            

            
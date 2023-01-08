beginwaarde = int(input("Beginwaarde:"))
eindwaarde = int(input("Endwaarde:"))
optelling = int(input("OpTell:"))

for i in range(beginwaarde, eindwaarde, optelling):
    print(i)
    eindwaarde += 1


#float in range gaat niet
#Bij for gaat ge geen oneindige lus genereren
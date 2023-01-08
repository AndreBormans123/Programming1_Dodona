# https://dodona.ugent.be/nl/courses/1286/series/14358/activities/2128064180

numlist = [ 100, 101, 0, "103", 104 ]
try:
    i1 = int( input( "Give an index: " ) )
    print( "100 /", numlist[i1], "=", 100 / numlist[i1] )
except ZeroDivisionError:
    print("Fout: Je kunt niet delen door 0")
except ValueError:
    print("Fout: Gebruik alleen integers")
except IndexError:
    print("Fout: Index buiten list")
except:
    print("Fout: Er is iets anders fout gegaan")



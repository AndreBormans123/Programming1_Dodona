from os import listdir, getcwd
from os.path import join
from os.path import getsize

grootte = 0
bestandslist = listdir( "." )
for naam in bestandslist:
    pad = join( getcwd(), naam )
    print( pad )
    grootte += getsize(pad)
print(f"De totale grootte van deze bestanden is {grootte} kilobytes.")
from os import system
from sys import path
from color import set
print(set('installing','white',style='bold'),set('colorcli','white'),'please wait ..')
p=path
system('cp color.py '+p[-1])
print(set('installed sucessfully ..','green',style='bold'))

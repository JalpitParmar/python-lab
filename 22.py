import mymodule
mymodule.print_name('jalpit')
print('='*20)

import mymodule as my
my.print_name('jalpit')
print('='*20)


from mymodule import print_name
print_name('jalpit')
print('='*20)


from mymodule import *
print_name('jalpit')
print_roll(29)
print('='*20)


from mymodule import print_name as pn
pn('jalpit')

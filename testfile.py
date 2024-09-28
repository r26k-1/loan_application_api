import PackageA

from PackageA import f1
from PackageA import f2

print(f1.print_something())
print(f2.print_something())


#Using Sub package
from PackageA.SubpackageA import f3
from PackageA.SubpackageA import f4
print(f3.print_something())
print(f4.print_something())

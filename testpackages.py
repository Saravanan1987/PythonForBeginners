""" if you import an package/module, only the name of the package/module 
will be imported from module/package private symbol into local symbol table.
You need to use package/module name to access it's variables. 
For example: package.module1.varibale1"""

""" Only package is initialized with the below import statement, 
in order to to use the modules inside the packages, 
you need to do an import in __init__.py dunder file inside packages"""

""" you can use "." relative import inside __init__.py dunder file, 
it works even we change the package name in future as dot refers the current directory """

""" if use from <module_name> import * , it won't do anything in case of packages 
but it imports all the functions in case of using it in a module, 
For packages , you need to use __all__ dunder as a list to define what can be imported in case of  "*" """
""" In summary, __all__ is used by both packages and modules to control what is imported when import * is specified. But the default behavior differs:

For a package, when __all__ is not defined, import * does not import anything.
For a module, when __all__ is not defined, import * imports everything (except—you guessed it—names starting with an underscore). """

import sys
import packages
print('After "packages" file import, members of "packages" object:{}'.format(dir(packages)))

try:
    print('packages.animals.dog() - {}'.format(packages.animals.dog()))
    print('packages.animals.cat() - {}'.format(packages.animals.cat()))
except:
    print("{}".format(sys.exc_info()))

try:
    print('packages.mypython() - {}'.format(packages.mypython()))
    print('packages.mypython() - {}'.format(packages.myclang()))
except:
    print("{}".format(sys.exc_info()))
    print("Failed because of __all__ dunder, accessing 'packages.module2.proglang.myclang()' directly works - {}".format(packages.module2.proglang.myclang()))



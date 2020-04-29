import os
print("Package contents - Demo Start")
from .module1 import animals,fileread
from .module2.proglang import *
path = os.path.abspath(os.getcwd())
fileread.fileread('packages/__init__.py')
print("Package contents - Demo End")

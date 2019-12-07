# Adds ProjectFolder Into SystemPath.
# This turns the project into a package, 
# so import can find thing easily.
from os.path import dirname
from sys import path
path.insert(0, dirname(dirname(__file__)))

# Imports the Need Modules to create a package.
from Interface.AppWindow import *
from Interface.CardPage import *
from Interface.PinPage import *
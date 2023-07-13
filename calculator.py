from importlib import import_module
from commands import __all__ as modules 
import math

variables = {
    "PI" : math.pi,
    "ans" : 0,
    "res": 0
}


commands = {}
# fill 'commands' dict with functions from commands package 
for c in modules:
    m = import_module("commands." + c)
    commands.update({m.name : m.fn})



while True:
    s = input()
    
    for i in commands.keys():
        if i in s:
            commands[i](s, variables)
            break
    else:
        commands["calc"](s, variables)






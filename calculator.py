from importlib import import_module
from commands import __all__ as modules 
import math


variables = {
    "PI" : math.pi,
    "ans" : 0,
}


commands = {}
cmds = []
# fill 'commands' dict with functions from commands package 
for c in modules:
    m = import_module("commands." + c)
    cmds.append(m)
    commands.update({m.name : m.fn})





while True:
    s = input()
    
    for key in commands.keys():
        if key in s:
            commands[key](s, variables, cmds)
            break
    else:
        commands["calc"](s, variables, cmds)
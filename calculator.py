variables = {}
commands = {}

def build_command(name, description, fn):
    fn.description = description
    commands.update({name : fn})


def assign(a):
    a = a.split(" ")
    
    if(len(a) != 3):
        print("invalid input format")
        return
    if not a[2].isdigit():
        print("'" + a[2] + "'" + " is not a number")
    if a[1].isdigit():
        print("'" + a[1] + "'" + " is not a valid variable name")
    if a[1] in variables:
        print("variable " + a[1] + " has been replaced, " + variables[a[1]] + " -> " + a[2])

    variables.update({a[1] : a[2]})

def print_vars(a):
    print(variables)

def helper(a):
    print("\n")
    for i in commands:
        print(i + "   " + commands[i].description)
        print()
        
def calc(a):
    a = a.replace(" ", "")
    


def is_expression(str, set):
    return 0 not in [c in str for c in set]

def is_variable(str, set):
    for c in str:
        if c not in set:
            return 0


def test(str, set):
    return [c in str for c in set]


valid_chars = [
    "0", "1", "2", "3", "4", "5", "6", "7", "8", "9",
    # variables.keys()
]

print(valid_chars)
print()
print(test("hi 22 x", valid_chars))


    
def undo(a):
    ...


build_command("assign", "assigns variable - 'assign variable value", assign)
build_command("variables", "prints all current variables", print_vars)
build_command("help", "this", helper)
build_command("calc", "calculates the given expression", calc)
build_command("undo", "undoes the last process", undo)
    
while True:
    a = input()
    
    for i in commands.keys():
        if i in a:
            commands[i](a)
            break
    else:
        calc(a)
    




name = "assign"
description = "assigns variable' - 'assign 'variable' 'value'"
# arguments = ["see description"]

def assign(s, variables, commands):
    s = s.split(" ")
    # if s[2] in commands:
    #     print("cannot assign command name " + s[2] + " twice")
    if 1 in [s[1] == cmd.name for cmd in commands]:
        print("cannot assign command name '" + s[1] + "' twice")
        return
    
    if(len(s) != 3):
        print("invalid input format")
        return
    if not s[2].isdigit():
        print("'" + s[2] + "'" + " is not a number")
        return
    if s[1].isdigit():
        print("'" + s[1] + "'" + " is not a valid variable name")
        return
    
    undo_list = [c.undo_list for c in commands if c.name == "undo"][0]
    if s[1] in variables:
        undo_list.append((s[1], variables[s[1]]))
        print("variable " + s[1] + " has been replaced, " + variables[s[1]] + " -> " + s[2])
    else:
        undo_list.append((s[1]))
        print("new variable " + s[1] + " = 2")


    
    return variables.update({s[1] : s[2]})



fn = assign

variables = {}




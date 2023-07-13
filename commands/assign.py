name = "assign"
description = "assigns variable - 'assign 'variable' 'value'"
arguments = ["see description"]

def assign(s, variables):
    s = s.split(" ")
    
    if(len(s) != 3):
        print("invalid input format")
        return
    if not s[2].isdigit():
        print("'" + s[2] + "'" + " is not a number")
        return
    if s[1].isdigit():
        print("'" + s[1] + "'" + " is not a valid variable name")
        return
    
    if s[1] in variables:
        print("variable " + s[1] + " has been replaced, " + variables[s[1]] + " -> " + s[2])
    else:
        print("new variable x = 2")

    return variables.update({s[1] : s[2]})



fn = assign
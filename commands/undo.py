name = "undo"
description = "undoes the last process"

undo_list = []
def undo(s, variables, commands):
    u = undo_list.pop()
    if len(u) == 1:
        del variables[u[0]]
        print("deleted variable " + u[0])
    else:
        variables.update({u[0] : u[1]})
        print("undo: " + u[0] + " = " + str(u[1]))
fn = undo


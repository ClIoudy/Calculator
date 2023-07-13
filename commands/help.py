name = "help"
description = "type help 'command_name' for more detailed descriptions"
arguments = ["all commands are possible arguments(see description)"]
def helper(s, variables, commands):
    print("\n")
    for cmd in commands:
        print(cmd.name + "   " + cmd.description)
        print()
    
    
    

fn = helper
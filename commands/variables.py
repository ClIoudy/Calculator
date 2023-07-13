name = "variables"
description = "prints all currently stored variables"
arguments = [
    "-a -> prints all variables, including system vars like PI"
]

def print_vars(s, variables, commands):
    print(variables)

fn = print_vars
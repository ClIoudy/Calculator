from re import findall
name = "calc"
description = "calculates expression"
# args = [""]

operators = ["+", "-", "/", "*"]

def calc(s, variables, commands):    
    if s == "":
        return
    if s == "ans":
        print(variables["ans"])
        return variables["ans"]
    groups = group(s)
    groups = mend(groups, variables)
    try:
        result = parse(groups)
    except:
        result = "invalid expression"
        
    
    undo_list = [c.undo_list for c in commands if c.name == "undo"][0]
    undo_list.append(("ans", variables["ans"]))
    variables["ans"] = result
    print(variables["ans"])

    
fn = calc

def group(s):
    s = s.replace(" ", "")
    results = findall(r"(\w+)|([+\-*/])", s)
    return [list(element)[0] for element in [filter(None, element) for element in results]]
    


def parse(groups):
    if len(groups) <= 1:
        return float(groups[0])

    right = float(groups[len(groups) - 1])
    op = groups[len(groups) - 2]

    match(op):
        case "+":
            left = parse(groups[:len(groups) - 2])
            result = left + right 
        case "-":
            left = parse(groups[:len(groups) - 2])
            result = left - right 
            
        case "*":
            left = float(groups[len(groups) - 3])
            right =  right * left
            groups = groups[:len(groups) - 2]
            groups[len(groups) - 1] = right

            result = parse(groups)
        
        case "/":
            left = float(groups[len(groups) - 3])
            right =  right / left
            groups = groups[:len(groups) - 2] 
            groups[len(groups) - 1] = right

            result = parse(groups)
            

    return result
        

# mend(s) turns expressions like 2a (with say a = 3) into 2 * 3
   
def mend(groups, variables):
    r = []
    for s in groups:
        if s.isdigit() or s in operators:
            r.append(s)
            continue
        else:
            results = findall(r"(\d+)|(\w+)", s)
            l = [list(element)[0] for element in [filter(None, element) for element in results]]
            a = []
            for element in l:
                if not element.isdigit():
                    element = resolve_vars(element, variables)
                    for e in element:
                        a.append(e)
                    
                else:
                    a.append(element)
                a.append("*")
            for e in a[:-1]:
                r.append(e)
    return r

def resolve_vars(s, variables):
    if s.isdigit():
        return s
    l = []
    keys = sorted(variables.keys(), key=len)
    keys.reverse()
    
    for key in keys:
        a = s.find(key)
        while a != -1:
            l.append(variables[s[a:a + len(key)]])
            l.append("*")
            s = s.replace(key, "", 1)
            a = s.find(key)
    l = l[:-1]
    return l

variables = {
    "pi": "3.14",
    "a": "5",
    "b": "2",
    "x": "100",
}
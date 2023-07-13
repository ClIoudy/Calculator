from re import findall
name = "calc"
description = "calculates expression"
args = [""]

operators = ["+", "-", "/", "*"]

def calc(s, variables):
    
    groups = group(s)
    groups = mend(groups, variables)
    try:
        result = parse(groups)
    except:
        result = "invalid expression"
    print(result)

    
fn = calc

def group(s):
    s = s.replace(" ", "")
    results = findall(r"(\w+)|([+\-*/])", s)
    return [list(element)[0] for element in [filter(None, element) for element in results]]
    


def parse(groups):
    if len(groups) <= 1:
        return int(groups[0])

    right = int(groups[len(groups) - 1])
    op = groups[len(groups) - 2]

    match(op):
        case "+":
            left = parse(groups[:len(groups) - 2])
            result = left + right 
        case "-":
            left = parse(groups[:len(groups) - 2])
            result = left - right 
            
        case "*":
            left = int(groups[len(groups) - 3])
            right =  right * left
            groups = groups[:len(groups) - 2]
            groups[len(groups) - 1] = right

            result = parse(groups)
        
        case "/":
            left = int(groups[len(groups) - 3])
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
            a.append(l[0])
            for element in l[-1:]:
                a.append("*")   
                if not element.isdigit():
                    ...
                    for e in resolve_vars(element, variables):
                        a.append(e)
                    continue
                a.append(element) 
            for e in a:
                r.append(e)
    return r

def resolve_vars(s, variables):
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
    return l[:-1]

# variables = {
#     "pi": "3.14",
#     "a": "5",
#     "b": "2",
#     "x": "100",
# }
  
# expr = "2b"
# r = calc(expr, variables)
# print(r)



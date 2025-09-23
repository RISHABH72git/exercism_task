def is_paired(input_string):
    brackets = {']':'[','}':'{',')':'('}
    braket_list = list(brackets.keys()) + list(brackets.values())
    stacks=[]
    for i in input_string:
        if i in braket_list:
            if i in list(brackets.keys()) and stacks:
                ele = stacks.pop()
                if brackets[i] != ele:
                    return False
            else:
                stacks.append(i)
    
    return len(stacks) == 0

def decode(string):
    if string == "":
        return string
    result = []
    num = ""
    for i in string:
        if i.isdigit():
            num += i
        else:
            count = int(num) if num else 1
            result.append(i*count)
            num = ""
    return "".join(result)

def encode(string):
    if string == "":
        return string
    result = []
    count = 1
    for i in range(1, len(string)):
        if string[i-1] == string[i]:
            count += 1
        else:
            if count > 1:
                result.append(f'{count}{string[i-1]}')
            else:
                result.append(f'{string[i-1]}')
            count = 1

    
    if count > 1:
        result.append(f'{count}{string[-1]}')
    else:
        result.append(f'{string[-1]}')

    return "".join(result)

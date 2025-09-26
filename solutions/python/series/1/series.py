def slices(series, length):
    if series == "":
        raise ValueError("series cannot be empty")
        
    if length == 0:
        raise ValueError("slice length cannot be zero")

    if length < 0:
        raise ValueError("slice length cannot be negative")

    if length > len(series):
        raise ValueError("slice length cannot be greater than series length")

    if length == len(series):
        return [series]

    result = []
    for i in range(len(series)):
        text = ""
        k = i
        if k+length > len(series):
            break
        for j in range(length):
            text += series[k]
            k+=1

        result.append(text)
    return result

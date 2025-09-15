def is_isogram(string):
    for i, val in enumerate(string):
        sub_string_sen = string[0:i] + string[i+1:len(string)]
        if val.isalpha() and val.lower() in sub_string_sen:
            return False
    return True

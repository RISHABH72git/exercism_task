import string
def rotate(text, key):
    alhpabets_lower = string.ascii_lowercase
    alhpabets_upper = string.ascii_uppercase

    alphabet_index = key
    cipher = ''
    for i, val in enumerate(text):
        if val.isalpha() and val.islower():
            index = alhpabets_lower.find(val) + alphabet_index
            cipher += alhpabets_lower[get_index(index)]
        elif val.isalpha() and val.isupper():
            index = alhpabets_upper.find(val) + alphabet_index
            cipher += alhpabets_upper[get_index(index)]
        else:
            cipher += val
    
    return cipher

def get_index(index):
    return index % 26 if index >= 26 else index
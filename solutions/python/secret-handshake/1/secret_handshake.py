actions = {
    "00001":"wink",
    "00010":"double blink",
    "00100": "close your eyes",
    "01000" : "jump",
    "10000" : "Reverse the order of the operations in the secret handshake."
}
def commands(binary_str):
    result = []
    key = '00000'
    binary_str_len = len(binary_str)-1
    for i in range(binary_str_len, -1, -1):
        if binary_str[i] == "1":
            action_key = (key[0:i] + "1") + "0" * (binary_str_len - i)
            if action_key != "10000":
                result.append(actions[action_key])
            else:
                result.reverse()
            
    return result

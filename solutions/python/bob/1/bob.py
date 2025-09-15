def response(hey_bob):
    hey_bob = hey_bob.strip()

    if not hey_bob:
        return "Fine. Be that way!"
        
    if hey_bob.endswith('?') and not hey_bob.isupper():
        return "Sure."
    elif hey_bob.isupper() and not hey_bob.endswith('?'):
        return "Whoa, chill out!"
    elif hey_bob.endswith('?') and hey_bob.isupper():
        return "Calm down, I know what I'm doing!"
    else:
        return "Whatever."

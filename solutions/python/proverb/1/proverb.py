def proverb(*words, qualifier = None):
    result = []
    if not words:
        return result
        
    for i in range(1, len(words)):
        result.append(f"For want of a {words[i-1]} the {words[i]} was lost.")
    if qualifier is not None:
        result.append(f"And all for the want of a {qualifier} {words[0]}.")
    else:
        result.append(f"And all for the want of a {words[0]}.")

    return result
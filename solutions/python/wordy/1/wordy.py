def answer(question):
    if not question.startswith("What is ") or not question.endswith("?"):
        raise ValueError("syntax error")

    # Remove starting and ending phrases
    q = question[8:-1].strip()

    # Empty or invalid
    if not q:
        raise ValueError("syntax error")

    # Replace word operations with symbols for easier parsing
    replacements = {
        "plus": "+",
        "minus": "-",
        "multiplied by": "*",
        "divided by": "/",
    }

    for phrase, symbol in replacements.items():
        q = q.replace(phrase, symbol)

    # Split into tokens
    tokens = q.split()

    # Validate all tokens
    valid_ops = {"+", "-", "*", "/"}
    equation = []

    i = 0
    while i < len(tokens):
        token = tokens[i]

        # Handle numbers (including negatives)
        if token.lstrip("-").isdigit():
            equation.append(int(token))
            i += 1
        elif token in valid_ops:
            equation.append(token)
            i += 1
        else:
            # Unknown token (not number or known op)
            raise ValueError("unknown operation")

    # Simple case — just a single number
    if len(equation) == 1 and isinstance(equation[0], int):
        return equation[0]

    # Must alternate number, op, number, ...
    if len(equation) < 3 or not isinstance(equation[0], int):
        raise ValueError("syntax error")

    print(equation)# Evaluate left-to-right (ignore normal operator precedence)
    result = equation[0]
    i = 1

    while i <= len(equation) - 1:
        try:
            op = equation[i]
            num = equation[i + 1]

            if not isinstance(num, int):
                raise ValueError("syntax error")

            if op == "+":
                result += num
            elif op == "-":
                result -= num
            elif op == "*":
                result *= num
            elif op == "/":
                result //= num
            else:
                raise ValueError("unknown operation")

            i += 2

        except Exception:
            raise ValueError("syntax error")

    return result

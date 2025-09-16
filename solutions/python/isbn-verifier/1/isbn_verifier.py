def is_valid(isbn):
    new_isbn = "".join([i for i in isbn if i != '-'])
    if len(new_isbn) != 10:
        return False
    count = 10
    sum = 0
    for i in new_isbn:
        if i.isdigit():
            sum += int(i) * count
            count -= 1
        elif i == 'X' and count == 1:
            sum += 10 * count
            count -= 1
    return sum % 11 == 0 and count == 0

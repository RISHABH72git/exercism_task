def sum_of_multiples(limit, multiples):
    set_item = set()
    for i in multiples:
        if i:
            set_item.update(set(range(i, limit, i)))

    return sum(set_item)

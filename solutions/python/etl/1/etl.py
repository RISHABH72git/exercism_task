def transform(legacy_data):
    result = {}
    for key in legacy_data:
        for i in legacy_data[key]:
            result[i.lower()] = key

    return result

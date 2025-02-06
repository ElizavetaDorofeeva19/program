def flatten(lst):
    result = []
    for item in lst:
        if isinstance(item, list):
            result.extend(flatten(item))

        else:
            result.append(item)
    return result


def group_by_type(input_list, dopolnenie=False):
    if dopolnenie:
        input_list = flatten(input_list)
    result = dict()
    for i in input_list:
        result.setdefault(str(type(i).__name__), []).append(i)
    return result


print(group_by_type([1, 1, "hello", 3.14, [1, 2, 3], "world", 42]))

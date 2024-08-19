def apply_all_func(int_list: list, *functioins):
    try:
        result = {}
        for func in functioins:
            result[func.__name__] = func(int_list)
        return result

    except TypeError as exc:
        return exc


print(apply_all_func([6, 20, 15, 9], max, min))
print(apply_all_func([6, 20, 15, 9], len, sum, sorted))

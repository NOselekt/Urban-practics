data_structure = [
  [1, 2, 3],
  {'a': 4, 'b': 5},
  (6, {'cube': 7, 'drum': 8}),
  "Hello",
  ((), [{(2, 'Urban', ('Urban2', 35))}])
]

def struct_count(arg=None):
    struct = []
    res = 0
    if struct:
        if isinstance(arg, dict):
            struct = [[i, j] for i, j in arg.items()]
        else:
            struct = [i for i in arg]
            for i in struct:
                if isinstance(i, dict):
                    for j, k in i.items():
                        res += len(j)
                        if isinstance(k, int) or isinstance(k, float):
                            res += k
                        elif isinstance(k, str):
                            res += len(k)
                elif isinstance(i, int) or isinstance(i, float):
                    res += i
                elif isinstance(i, str):
                    res += len(i)
                else:
                    res += struct_count(i)
    return res

print(struct_count(data_structure))
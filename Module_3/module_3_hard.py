data_structure = [
  [1, 2, 3],
  {'a': 4, 'b': 5},
  (6, {'cube': 7, 'drum': 8}),
  "Hello",
  ((), [{(2, 'Urban', ('Urban2', 35))}])
]

def struct_count(arg=None):
    res = 0
    if isinstance(arg, int) or isinstance(arg, float):
        res += arg
    elif isinstance(arg, str):
        res += len(arg)
    else:
        if arg:
            struct = []
            if isinstance(arg, dict):
                struct = [[i, j] for i, j in arg.items()]
            else:
                struct = [i for i in arg]
            for element in struct:
                if isinstance(element, dict):
                    for j, k in element.items():
                        res += struct_count(j) + struct_count(k)
                else:
                    res += struct_count(element)
    return res

print(struct_count(data_structure))
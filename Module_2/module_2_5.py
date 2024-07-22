def get_matrix(n = 0, m = 0, value = 0):
    if n == 0 or m == 0:
        return []
    matrix = [[value for string in range(m)] for row in range(n)]
    return matrix
print(get_matrix())

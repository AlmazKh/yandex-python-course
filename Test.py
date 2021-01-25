def matrix(n=1, m=None, a=0):
    if not m:
        m = n
    return [[a for j in range(m)] for i in range(n)]


print(matrix(2, 3, 845))

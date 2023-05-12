def solution(ineq, eq, n, m):
    cen = ineq + eq
    if (cen == '<='):
        return int(n <= m)
    elif (cen == '>='):
        return int(n >= m)
    elif (cen == '>!'):
        return int(n > m)
    return int(n < m)
# License: GPL

def editpath(s0, s1):
    '''
    path,cost = editpath(s0, s1)

    Return the edit path

    Parameters
    ----------
    s0 : str
        First string
    s1 : str
        Second string

    Returns
    -------
    path : str
        How to transform s0 into s1
    cost : int

    '''
    cost =  [[0 for i in xrange(1+len(s1))] for j in xrange(1+len(s0))]
    n0 = len(s0)
    n1 = len(s1)
    for i0,c0 in enumerate(s0):
        cost[i0+1][0] = i0+1
        for i1, c1 in enumerate(s1):
            cost[i0+1][i1+1] = min(
                            cost[i0][i1] + (c0 != c1),
                            cost[i0][i1+1] + 1,
                            cost[i0+1][i1] + 1)
    path = ''
    p0, p1 = 0,0
    while p0 < n0 and p1 < n1:
        c0 = s0[p0]
        c1 = s1[p1]
        cm = cost[p0][p1] + (c0 != c1)
        if cm == cost[p0+1][p1+1]:
            if (c0 == c1):
                path += 'm'
            else:
                path += 'x'
            p0 += 1
            p1 += 1
        elif cost[p0][p1] == (cost[p0][p1+1] + 1):
            path += ('r%s' % c0)
            p0 += 1
        elif cost[p0][p1] == (cost[p0+1][p1] + 1):
            path += ('a%s' % c1)
            p1 += 1
        else:
            assert False
    while p0 < n0:
        path += ('r%s' % s0[p0])
        p0 += 1
    while p1 < n1:
        path += ('a%s' % s1[p1])
        p1 += 1
    return path, cost[n0][n1]


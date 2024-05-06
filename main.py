def isqr(m):
    return all(len(r) == len(m) for r in m)

def normalize(m):
    return list(map(lambda y: list(map(lambda x: bool(x), y)), m))

def seq(m):
    return list(sum(r) for r in m)

def ah(a, index, e=[]):
    ex = e.copy()
    ex.append(index)
    n, u = 0, 0
    for i in range(len(a[index])):
        if a[index][i] != 0 and (i not in ex):
            n += ah(a, i, ex)
            u += 1
    return (u << n) % 6997

def ml(m):
    return list(ah(m, i) for i in range(len(m)))

def findVal(a,b,p):
    c, b = normalize(a), normalize(b)
    c, b, d = ml(c), ml(b), dict()
    for i in range(len(b)):
        for u in range(len(c)):
            if c[u] == b[i]:
                d[i] = u
                c[u] = -1
                b[i] = -1
                break
    n = 0
    for i in range(len(p)):
        if i+1 < len(p):
            n += a[d[p[i]]][d[p[i+1]]]
    return n

def findPos(a,b,p):
    c, b = normalize(a), normalize(b)
    c, b, d = ml(c), ml(b), dict()
    for i in range(len(b)):
        for u in range(len(c)):
            if c[u] == b[i]:
                d[i] = u
                c[u] = -1
                b[i] = -1
                break

    for i in range(len(p)):
        p[i] = d[p[i]]
    return p

def solveLength(a, b, p):
    assert isqr(a) and isqr(b), 'Attributes should contain only square matrices'
    assert len(a) == len(b), 'Matrices should have equal length'
    assert sorted(seq(normalize(a))) == sorted(seq(normalize(b))), 'Graphs are not isomorphic'
    return findVal(a, b, p)

def solvePositions(a, b, p):
    assert isqr(a) and isqr(b), 'Attributes should contain only square matrices'
    assert len(a) == len(b), 'Matrices should have equal length'
    assert sorted(seq(normalize(a))) == sorted(seq(normalize(b))), 'Graphs are not isomorphic'
    return findPos(a, b, p)

if __name__ == '__main__':

    # https://inf-ege.sdamgia.ru/problem?id=9753

    a = [
        [0, 45, 0, 10, 0, 0, 0],
        [45, 0, 0, 40, 0, 55, 0],
        [0, 0, 0, 0, 15, 60, 0],
        [10, 40, 0, 0, 0, 20, 35],
        [0, 0, 15, 0, 0, 55, 0],
        [0, 55, 60, 20, 55, 0, 45],
        [0, 0, 0, 35, 0, 45, 0]
    ]

    b = [
        [0, 1, 1, 0, 0, 0, 0],
        [1, 0, 1, 0, 0, 0, 0],
        [1, 1, 0, 1, 1, 1, 0],
        [0, 0, 1, 0, 0, 1, 1],
        [0, 0, 1, 0, 0, 1, 0],
        [0, 0, 1, 1, 1, 0, 1],
        [0, 0, 0, 1, 0, 1, 0]
    ]

    j = [3, 5]

    print(solveLength(a, b, j))
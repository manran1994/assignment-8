n, m = map(int, raw_input().split())
A = [raw_input() for x in range(n)]
M = []

def update(x, y):
    up = x; down = x; left = y; right = y;
    pos = set([(x, y)])
    while up >= 0 and down < n and left >=0 and right < m:
        costs = [A[elem[0]][elem[1]] == 'D' for elem in [(up, y), (down, y), (x, left), (x, right)]]
        if sum(costs) > 0: break;
        for elem in [(up, y), (down, y), (x, left), (x, right)]: 
            pos.add(elem)
        up-=1
        left-=1
        down+=1
        right+=1
    return pos

def switch(x):
    return {
        0: (0, 0),
        1: (1, 0),
    }.get(x, (x-4, 1))

for ii in range(n):
    for jj in range(m):
        if A[ii][jj] == 'S':
            M.append(update(ii, jj))

# for ii in M: 
#     print ii

res = [(max([len(x) for x in M]), 0)]
for ii in range(len(M) - 1):
    for jj in range(ii+1, len(M)):
        len_mii = len(M[ii])
        len_mjj = len(M[jj])

        if len(M[ii].intersection(M[jj])) > 0:
            continue
        
        nres = [len_mii, len_mjj]
        nres.sort(reverse=True)
        res.append(tuple(nres))

res.sort(reverse=True)
# print res

if len(res) == 0: print 0, 0
else: print res[0][0], res[0][1]
group = ['abcdefhi', 'jklmnopqr', 'stuvwxyz_']
K = map(int, raw_input().split())
A = raw_input()

data = ['', '', '']
ids = [[], [], []]
for ii in range(len(A)): 
    for gid in range(3):
        if A[ii] in group[gid]: 
            data[gid]+=A[ii]
            ids[gid].append(ii)
            break

def rotate(gid):
    k = K[gid] % len(ids[gid])
    data[gid] = data[gid][-k:] + data[gid][:-k]

res = ['x' for x in range(len(A))]
for gid in range(3):
    rotate(gid)
    for ii in range(len(ids[gid])):
        res[ids[gid][ii]] = data[gid][ii]

print ''.join(res)
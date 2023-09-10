from itertools import permutations

perm = permutations([1, 2, 3,4,5,6,7])
area = [1,2,3,4]


def cross(a, b):
    if a == 1 and b == 1:
        return 2
    if a == 1 and b == 2:
        return 2
    if a == 1 and b == 3:
        return 4
    if a == 2 and b == 1:
        return 1
    if a == 2 and b == 2:
        return 1
    if a == 2 and b == 4:
        return 3
    if a == 2 and b == 5:
        return 3
    if a == 2 and b == 6:
        return 4
    if a == 2 and b == 7:
        return 3
    if a == 3 and b == 4:
        return 2
    if a == 3 and b == 5:
        return 2
    if a == 3 and b == 7:
        return 2
    if a == 4 and b == 3:
        return 1
    if a == 4 and b == 6:
        return 2
    return 0


for aa in list(area):
    for p in list(perm):
        a=aa
        n=0
        for b in list(p):
            if a==0: continue
            a=cross(a,b)
            if a!=0 : n=n+1
            if n==7:
                print("possible")
                break

print("impossible")

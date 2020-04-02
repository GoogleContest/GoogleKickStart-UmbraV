# Attempt to try this in python
# read a line with a single integer


def from_iterable(iterables):
    for it in iterables:
        for element in it:
            yield element


def plus(plist, index):
    c = len(plist)
    elem = plist[index]
    if elem == 9 and index != 0:
        plist[index] = 0
        j = index
        if plist[j - 1] == 8:
            while plist[j - 1] == 8:
                plist[j - 1] = 0
                j = j - 1
            else:
                plist[j - 1] = plist[j - 1] + 2
        else:
            plist[index - 1] = plist[index - 1] + 2
    elif elem == 9 and index == 0:
        plist[0] = 0
        plist.insert(0, 2)
    else:
        plist[index] = plist[index] + 1
    plist = plist + (0 * (c - 1 - index))
    p = int("".join(map(str, plist)))
    return p


def minus(mlist, index):
    c = len(mlist)
    rlist = []
    if mlist[index] > 0:
        mlist[index] = mlist[index] - 1
        rlist = mlist[0:index] + "8" * (c - index)
        print(rlist)
        s = [str(i) for i in rlist]
        m = int("".join(s))
    return m


t = int(input())
for i in range(1, t + 1):
    n = [int(s) for s in input().split(" ")]  # n is a list
    nlist = list(map(int, from_iterable(map(str, n))))
    Num = int("".join(map(str, nlist)))
    c = len(nlist)
    dlist = nlist
    if c == 1:
        result = 1
    else:
        for index, elem in enumerate(dlist):
            if elem % 2 != 0:
                # p = plus(dlist, index)
                m = minus(dlist, index)
                result = m
                break

        # result = min(abs(m - Num), abs(p - Num))
    print("Case #{}: {}".format(i, result))


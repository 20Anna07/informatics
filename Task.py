def z_func(st):
    z = [0] * len(st)
    l, r = 0, 0
    for i in range(1, len(st)):
        if i <= r:
            z[i] = min(r - i + 1, z[i - l])
        while i + z[i] < len(st) and st[z[i]] == st[i + z[i]]:
            z[i] += 1
        if i + z[i] - 1 > r:
            l, r = i, i + z[i] - 1
    return z

def finding(str1, str2):
    before = ''
    for i in range(len(str1)):
        this = str1[:i]
        combo = this + '#' + str2
        z = z_func(combo)
        n = len(this)
        if z[n + 1] != n:
            return before
        before = this
    return before
            

strs = list(map(str, input().split()))
befores = [strs[0]]
for i in range(1, len(strs)):
    befores.append(finding(strs[0], strs[i]))
# print(befores)
mini = min(befores, key=len)
m = len(mini)
if m == 0:
    print('no one')
else:
    k = 0
    # print(mini)
    for i in befores:
        if i[: m] != mini:
            print('no one')
            k = -1
            break
    if k == 0:
        print(mini)
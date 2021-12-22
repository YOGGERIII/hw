# (X+2*Y)(2*X^2-Y^2+Z)

# (2*X+3*Y+4*Z)(XY^2+X^2Y+Z^2)

# (A+2*B^2)(B+3*C^3)(2*A+B+C)

def mul(p1, p2):
    ans = []
    for i in p1:
        for j in p2:
            union = {}
            for k in i[1]:
                union[k] = i[1][k]
            for k in j[1]:
                if k in i[1]:
                    union[k] += j[1][k]
                else:
                    union[k] = j[1][k]
            ans.append([int(i[0]) * int(j[0]), union])
    return ans

ipt = input('Input the polynomials: ')

order = {}
n = 0
for i in ipt:
    if i.isalpha() and i not in order:
        order[i] = n
        n += 1
order['!'] = n

ipt = ipt[1:-1].split(')(')
ipt = [i.replace('-', '+-').split('+') for i in ipt]
ipt = [[term.split('*') if '*' in term else ([-1, term[1:]] if term[0] == '-' else [1, term]) for term in poly] for poly in ipt]
# print(ipt)
for poly in ipt:
    for term in poly:
        i = 0
        while i < len(term[1]) - 1:
            if term[1][i].isalpha() and term[1][i + 1] != '^':
                term[1] = term[1][:i + 1] + '^1' + term[1][i + 1:]
            i += 1
        if term[1][-1].isalpha():
            term[1] += '^1'
        i = 0
        while i < len(term[1]):
            if term[1][i].isalpha():
                term[1] = term[1][:i] + '!' + term[1][i:]
                i += 1
            i += 1
        term[1] = term[1][1:].split('!')
        # print(term[1])
        new_term1 = {}
        for i in term[1]:
            if i:
                new_term1[i[0]] = int(i[2:])
            else:
                new_term1['!'] = 0
        term[1] = new_term1

while len(ipt) > 1:
    ipt[1] = mul(ipt[0], ipt[1])
    del ipt[0]

for i in ipt[0]:
    i[1] = list(i[1].items())
    i[1].sort(key=lambda x: order[x[0]])

for i in range(len(ipt[0]) - 1, -1, -1):
    for j in range(i):
        if str(ipt[0][j][1]) == str(ipt[0][i][1]):
            ipt[0][j][0] += ipt[0][i][0]
            del ipt[0][i]
            break

for i in ipt[0][:1]:
    if i[0] != 1:
        print('{}*'.format(i[0]), end='')
    else:
        print('+', end='')

    for j in i[1]:
        print(j[0], end='')
        if j[1] != 1:
            print('^{}'.format(j[1]), end='')

for i in ipt[0][1:]:
    if i[0] == 1:
        print('+', end='')
    elif i[0] == -1:
        print('-', end='')
    else:
        print('{:+}*'.format(i[0]), end='')

    for j in i[1]:
        if j[0] != '!':
            print(j[0], end='')
            if j[1] != 1:
                print('^{}'.format(j[1]), end='')

print()
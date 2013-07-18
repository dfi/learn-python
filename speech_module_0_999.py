x = range(1000)

a = [i for i in range(10)]
b = [i for i in range(10, 20)]
c = [i for i in range(20, 100, 10)]
d = [i for i in range(20, 100) if i%10 != 0]
e = [i for i in range(100, 1000, 100)]
f = [i for i in range(100, 1000) if ( i%100 in range(1, 10) )]
g = [i for i in range(100, 1000) if ( i%100 in range(10, 20) )]
h = [i for i in range(100, 1000) if ( (i%10 == 0) and (i%100 > 10) )]

z = []

for i in x:
    if i not in (a+b+c+d+e+f+g+h):
        z.append(i)
        
print('a:\n', a, '\n')
print('b:\n', b, '\n')
print('c:\n', c, '\n')
print('d:\n', d, '\n')
print('e:\n', e, '\n')
print('f:\n', f, '\n')
print('g:\n', g, '\n')
print('h:\n', h, '\n')
print('z:\n', z)
print('---------------------------')
print(len(x) - len(a) - len(b) - len(c) - len(d) - len(e) - len(f) - len(g) - len(h) - len(z))

#type(range(i)) is range in Python 3, but list in Python 2

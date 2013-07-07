z = range(1000)

a = range(10)
b = range(10, 20)
c = range(20, 100, 10)
d = [i for i in range(21, 100) if i % 10 != 0]
e = range(100, 1000, 100)
f = [i for i in range(100, 1000) if ( i % 100 in range(1, 10) ) ]
g = [i for i in range(100, 1000) if ( i % 100 in range(10, 20) ) ]
h = [i for i in range(120, 1000) if (i % 10 == 0 and i % 100 != 0)]

x = []

for i in z:
    if i not in a:
        if i not in b:
            if i not in c:
                if i not in d:
                    if i not in e:
                        if i not in f:
                            if i not in g:
                                if i not in h:
                                    x.append(i)
        
print 'a:\n', a
print 'b:\n', b
print 'c:\n', c
print 'd:\n', d
print 'e:\n', e
print 'f:\n', f
print 'g:\n', g
print 'h:\n', h

print 'x:\n', x
print '--------------------'
print len(z) - len(a) - len(b) - len(c) - len(d) - len(e) - len(f) - len(g) - len(h) - len(x)

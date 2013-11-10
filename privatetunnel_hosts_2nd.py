'''
这么写明显比第一种方法简洁，思路也清晰不少。
当然还有更好的办法……
'''
with open('pt_srvlist.bundle', 'r') as The_read:
    for line in The_read:
        list1 = line.split('","ingress":"')
        list2 = line.split('"hostname":"')

    list3 = []
    for a in list1:
        for i in range(len(a)):
            if a[i] == '"':
                b = a[:i]
                list3.append(b)
                break

    list4 = []
    for a in list2:
        for i in range(len(a)):
            if a[i] == '"':
                b = a[:i]
                list4.append(b)
                break

    list5 = []
    for i in range(1, len(list3)):
        list5.append(list3[i] + '    ' + list4[i] + '\n')

    x = ''.join(list5)


with open('out_new.txt', 'w') as Out_put:
    Out_put.write(x)

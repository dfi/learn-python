'''
openvpn 连不上 privatetunnel ，**去网站一看，以前的hosts都没了，现在只给了
一个 privatetunnel-win-2.2.exe ，从中得到 pt_srvlist.bundle ，于是有了以下
粗糙代码。
'''
'''
虽然折腾一番有些许成就感，但所知甚少。
'''

with open('pt_srvlist.bundle', 'r') as The_read:
    for line in The_read:
        list1 = line.split(':')
    list2 = []
    for i in list1:
        if '.' in i:
            list2.append(i)
    x1 = ''.join(list2)

    list3 = x1.split('"')
    list4 = []
    for i in list3:
        if '.' in i:
            list4.append(i+'\n')
    x2 = ''.join(list4)

    listz = []
    for i in list4:
        count = 0
        for j in range(len(i)):
            if i[j] == '.':
                count += 1
        if count > 1:
            listz.append(i)
    x3 = ''.join(listz)

    for i in range(len(listz)):
        if i % 2:
            temp = listz[i]
            listz[i] = listz[i-1]
            listz[i-1] = temp
    x4 = ''.join(listz)

    for i in range(len(listz)):
        if not i % 2:
            listz[i] = listz[i].strip('\n') + '    '

    x5 = ''.join(listz)


with open('out1.txt', 'w') as Out_put:
    Out_put.write(x1)
with open('out2.txt', 'w') as Out_put:
    Out_put.write(x2)
with open('out3.txt', 'w') as Out_put:
    Out_put.write(x3)
with open('out4.txt', 'w') as Out_put:
    Out_put.write(x4)
with open('out5.txt', 'w') as Out_put:
    Out_put.write(x5)

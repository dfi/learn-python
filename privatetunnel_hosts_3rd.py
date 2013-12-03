'''
在 privatetunnel_hosts_2nd.py 的基础上用到了函数
'''

def Do_List(In_List):
    Out_List = []
    for a in In_List:
        for i in range(len(a)):
            if a[i] == '"':
                Out_List.append(a[:i])
                break
    return Out_List

with open('pt_srvlist.bundle', 'r') as The_read:
    for line in The_read:
        list1 = line.split('","ingress":"')
        list2 = line.split('"hostname":"')

    list3 = Do_List(list1)
    list4 = Do_List(list2)

    list5 = []
    for i in range(1, len(list3)):
        list5.append(list3[i] + '    ' + list4[i] + '\n')

    x = ''.join(list5)


with open('out_new.txt', 'w') as Out_put:
    Out_put.write(x)

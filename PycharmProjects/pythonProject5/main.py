# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


#2
def anz_symm(list):
    ct=0
    for e in range(len(list)):
        for i in range(e+1,len(list)):
            x = list[i]%10
            if list[e] == list[i]//10 + x*10:
                ct+=1
    return ct

#3
def konk(list):
    l=[]
    number=''
    for e in list:
        e=str(e)
        for i in e:
            if i not in l:
                l.append(int(i))
    l.sort(reverse=True)
    for idx in l:
        idx=str(idx)
        number+=idx
    return int(number)

#4
def crypt1(list):
    key = list[0]
    for e in range(1, len(list)):
        list[e]+= key
    return list

def crypt2(list):
    key = list[0]
    for e in range(1, len(list)):
        list[e]*= key
    return list

def crypt3(list):
    key = list[0]
    for e in range(1, len(list)):
        list[e]^= key
    return list
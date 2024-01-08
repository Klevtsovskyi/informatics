#T09s2_11
#Ханойські вежі

def hanoi (n,a,b,c):
    '''Здійснює перенесення n дисків з a на b, використовуючи c як допоміжний.

    '''
    if n != 0:
        hanoi(n-1,a,c,b)    #перенести n-1 диск з a на c
        print('{} -> {}'.format(a,b))   #показати перенесення 1 диску
        hanoi(n-1,c,b,a)    #перенести n-1 диск з c на b

n = int(input("введіть кілкість дисків: "))

hanoi(n,1,2,3)






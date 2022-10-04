import random
q0=random.randint(1,999)
w0=random.randint(1,999)
b0=random.randint(2,9)
def maxim(x):
    max=0
    while x>0:
        r=x%10
        x//=10
        if r>max:
            max=r
    return max
def verificare(n,b):
    if maxim(n)<b:
        return True
    else:
        return False
def conversia_in_baza_10(n,b):
    i=0
    sum=0
    while n>0:
        r=n%10
        z=r*(b**i)
        n//=10
        sum+=z
        i+=1
    return sum

def suma_in_baza10(q,w,b):
    q1=conversia_in_baza_10(q,b)
    w1=conversia_in_baza_10(w,b)
    suma=q1+w1
    return suma

def suma_convertita(q,w,b):
    c=suma_in_baza10(q,w,b)
    lista=[]
    while c>0:
        o=c//b
        nr=c-(b*o)
        lista.append(nr)
        c=o
    m=reversed(lista)
    l=''.join(map(str,m))
    return l



def scaderea(q,w,b):
    q1=conversia_in_baza_10(q,b)
    w1=conversia_in_baza_10(w,b)
    if q1>w1:
        scad=q1-w1
        return scad
    else:
        scad=w1-q1
        return scad

def scaderea_convertita(q,w,b):
    scad=scaderea(q,w,b)
    lista=[]
    while scad>0:
        o=scad//b
        nr=scad-(b*o)
        lista.append(nr)
        scad=o
    m=reversed(lista)
    l=''.join(map(str,m))
    return l

def inmultire(q,w,b):
    q1=conversia_in_baza_10(q,b)
    w1=conversia_in_baza_10(w,b)
    x=q1*w1
    return x
def inmultirea_convertita(q,w,b):
    x=inmultire(q,w,b)
    lista=[]
    while x>0:
        o=x//b
        nr=x-(b*o)
        lista.append(nr)
        x=o
    m=reversed(lista)
    l=''.join(map(str,m))
    return l

if (b0>1) and (b0<10):
    print('Rezultatul verificarii bazei',b0,'a numarului',q0,'este:',verificare(q0,b0))
    print('Rezultatul verificarii bazei',b0,'a numarului',w0,'este:',verificare(w0,b0))
    if verificare(q0,b0)==True and verificare(w0,b0)==True :
        print('Suma nr: ',q0,'si',w0,'in baza',b0,'este=',suma_convertita(q0,w0,b0))
        print('Diferenta nr: ',q0,'si',w0,'in baza',b0,'este=',scaderea_convertita(q0,w0,b0))
        print('Inmultirea nr: ',q0,'si',w0,'in baza',b0,'este=',inmultirea_convertita(q0,w0,b0))
    while verificare(q0,b0)!=True or verificare(w0,b0)!=True:
        import random
        q0=random.randint(1,999)
        w0=random.randint(1,999)
        b0=random.randint(2,9)
        if verificare(q0,b0)==True and verificare(w0,b0)==True :
            print('Rezultatul verificarii bazei',b0,'a numarului',q0,'este:',verificare(q0,b0))
            print('Rezultatul verificarii bazei',b0,'a numarului',w0,'este:',verificare(w0,b0))
            print('Suma nr: ',q0,'si',w0,'in baza',b0,'este=',suma_convertita(q0,w0,b0))
            print('Diferenta nr: ',q0,'si',w0,'in baza',b0,'este=',scaderea_convertita(q0,w0,b0))
            print('Inmultirea nr: ',q0,'si',w0,'in baza',b0,'este=',inmultirea_convertita(q0,w0,b0))
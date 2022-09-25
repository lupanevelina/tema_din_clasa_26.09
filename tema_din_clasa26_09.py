n=int(input("n="))
a=False
if n<100000 :
    def nr_c(x):
        nr=0
        while x>0:
            r=x%10
            x//=10
            nr=nr+1
        return nr
    def nr_c_pare(x):
        l=[]
        while x>0:
            l.append(x%10)
            x//=10
        pare=[]
        for i in l:
            if i%2==0 :
                pare.append(i)
        return len(pare)
    def nr_c_impare(x):
        l=[]
        while x>0:
            l.append(x%10)
            x//=10
        impare=[]
        for i in l:
            if i%2!=0 :
                impare.append(i)
        return len(impare)
    def suma(x):
        s=0
        while x>0:
            r=x%10
            x//=10
            s=s+r
        return s
    def maxim(x):
        max=0
        while x>0:
            r=x%10
            x//=10
            if r>max:
                max=r
        return max
    def minim(x):
        min=9
        while x>0:
            r=x%10
            x//=10
            if r<min:
                min=r
        return min
    def media(x):
        s=0
        lista=[]
        while x>0:
            r=x%10
            x//=10
            s=s+r
            lista.append(r)
            nr_de_cifre=len(lista)
            med=s//nr_de_cifre
        return med
    def repeta(x):
        lista=[]
        x=str(x)
        for i in x:
            if x.count(i)>=2:
                if i not in lista:
                    lista.append(i)
        return lista
    def div(x):
        list=[]
        for i in range(1,x+1):
            if x%i==0 :
                list.append(i)
        return list
    def afisarea_cu_sep(x):
        afisare=str(x)[::1]
        lista=list(afisare)
        return ' '.join(lista)
    def reverse(x):
        rev=str(x)[::-1]
        return rev
    def prim(x):
        if x<=1:
            return False
        else:
            for i in range(2,x):
                if x%i==0 :
                    return False
        return True
    def cel_mai_mare_nr_format(x):
        lista=[]
        x=str(x)
        for elem in x:
            lista.append(int(elem))
        lista=sorted(lista)
        lista=reversed(lista)
        nr=''
        for elem in lista:
            nr+=str(elem)
        return nr
else:
    print('Numarul e mai mare ca 100000!') 

print('a). Nr de cifre in',n,'este: ',nr_c(n))
print('b). Nr de cifre pare in',n,'este: ',nr_c_pare(n))
print('c). Nr de cifre impare in',n,'este: ',nr_c_impare(n))
print('d). Suma cifrelor nr',n,'este:',suma(n))
print('e). Cifra maxima a nr',n,'este:',maxim(n))
print('f). Cifra minima a nr',n,'este:',minim(n))
print('g). Media aritmetica a cifrelor nr',n,'este:',media(n))
print('h). Cifrele care se repeta de cel putin 2 ori in nr',n,'sunt:',repeta(n))
print('i). Afisarea cifrelor separate ai nr',n,':',afisarea_cu_sep(n))
print('j). Divizorii nr',n,'sunt:',div(n))
print('k). Inversul nr',n,'este:',reverse(n))
print('l). Cel mai mare nr format din cifrele nr',n,'este:',cel_mai_mare_nr_format(n))
if prim(n) is True:
    print('m).',n,'E PRIM :D')
else:
    print('m).',n,'NU E PRIM :O')



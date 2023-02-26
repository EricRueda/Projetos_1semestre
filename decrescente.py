a = int(input('Digite um valor: '))
b = int(input('Digite outro valor: '))
c = int(input('Digite o último valor: '))

if a < b < c:
    print(a, b ,c)

elif c < a < b:
    print(c, a, b)

elif b < c < a:
    print(b, c, a)
    

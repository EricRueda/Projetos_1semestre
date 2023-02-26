import math

a = float(input('Digite o valor de a: '))
b = float(input('Digite o valor de b: '))
c = float(input('Digite o valor de c: '))

delta = b**2-4*a*c

if delta <= 0:
    print('Não é possível calcular, pois os valores das raízes são imaginários')

else:
    raiz = math.sqrt(delta)
    x1 = (-b+raiz)/2*a
    x2 = (-b-raiz)/2*a
    print('As raízes são respectivamente', x1, 'e', x2)




#git hub teste

import math

x = float(input("Ingrese el valor de x: "))
cifras = float(input("Ingrese cuantas cifras significativas: "))
es = 0.5*(10**(2-cifras))
n = 1
ea = es+1
ant = x

while ea>es:
    f = x
    for i in range(1,(n+1)):
        f += round((x**((2*i)+1))/math.factorial((2*i)+1),6)
    ea = round(abs((f-ant)/f)*100,6)
    print('{:^10}{:^10}{:^10}'.format('Iteracion','x','error'))
    print('{:^10}{:^10}{:^10}'.format(n,f,ea))
    ant = f
    n += 1

print("Resultado: x=",f," con un error de: ",ea)

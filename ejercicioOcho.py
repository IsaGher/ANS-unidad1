import math

x = float(input("Ingrese valor de x: "))
cifras = float(input("Ingrese cuantas cifras significativas: "))
es = 0.5*(10**(2-cifras))
ea = 1+es
n = 1
ant = x

while ea>es:
    f = x
    for i in range(1,(1+n)):
        f += round((math.factorial(2*i)/((2**i)*math.factorial(i))**2)*(x**(2*i+1)/(2*i+1)),6)
    try:
        ea = round(abs((f-ant)/f)*100,6)
    except ZeroDivisionError:
        print("Resultado: x= 0")
        exit()  
    print('{:^10}{:^10}{:^10}'.format('Iteracion','x','error'))
    print('{:^10}{:^10}{:^10}'.format(n,f,ea))
    ant = f
    n += 1

print("Resultado: x=",f," con error de: ",ea)
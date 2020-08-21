#num = int(input("ingresa el numero que quieres multiplicar"))
minimo = 1
maximo = 10
i = 1

for i in range(10):
    print("TABLA DE MULTIPLICAR DEL NUMERO:",{i})


    while minimo <= maximo:

        resultado = minimo * i
        print("{} x {} = {}".format(i, minimo, resultado))
        
        minimo = minimo + 1
    


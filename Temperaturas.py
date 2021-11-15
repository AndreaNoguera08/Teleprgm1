vTemperaturas = (36, 42, 57, 58, 07, 45, 26, 35, 83, 56, 57, 97, 28, 115, 53, 35, 99, 62, 78, 29, 98, 37, 42, 56, 86, 28, 86, 95, 26, 49, 67, 21, 815, 67, 104, 58, 512, 24, 92, 89, 67, 53, 81, 79, 83, 81, 44, 132, 77, 98, 73, 57)
mayor = None
menor = None
for numero in vTemperaturas:
    if mayor == None and menor == None:
        mayor = numero
        menor = numero
    else:
        if numero < menor:
           menor = numero
        if numero > mayor:
         mayor = numero
         print ("el numero mayor es:", {mayor})
         print ("el numero menor es:", {menor})

         if vTemperaturas > 100:
             print ("URGENTE! La temperatura llego a ser mayor a 100 grados")
                     
    

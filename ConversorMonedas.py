def conversor(tipoDivisa, valorDolar):
    divisa = input("\n¿Cuántos " +tipoDivisa +" a dólares va a cambiar?: ")
    divisa = float(divisa)
    dolares = divisa/valorDolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print("Tienes $" + dolares + " dólares\n")


menu = """
🗽CONVERSOR A DÓLARES🗽

💰 Escoja la divisa que desea cambiar a dólares💵

1- Peso argentino
2- Boliviano
3- Real brasileño
4- Peso chileno
5- Peso colombiano
6- Dólar (Ecuador)
7- Dólar guayanés
8- Guaraní paraguayo
9- Nuevo sol peruano
10- Dólar surinamés
11- Peso uruguayo
12- Bolivar fuerte venezolano
 
"""
opcion = int(input(menu))

if opcion == 1: # Peso argentino
    conversor("pesos argentinos", 186.98)
    
elif opcion == 2: # Boliviano
    conversor("bolivianos", 6.85)
    
elif opcion == 3: # Real brasileño
    conversor("reales", 4600)
    
elif opcion == 4: # Peso chileno
    conversor("pesos chilenos", 806.80)
       
elif opcion == 5: # Peso colombiano
    conversor("pesos colombianos", 4650)
    
elif opcion == 6: # Dólar (Ecuador)
    conversor("dólares", 1)
    
elif opcion == 7: # Dólar (Guyana)
    conversor ("dólares guayaneses", 210)
        
elif opcion == 8: # Guaraní
    conversor("guaranís", 7341.70)
    
elif opcion == 9: # Sol
    conversor("nuevos soles", 3.83)
    
elif opcion == 10: # Dólar (Suriname)
    conversor("dólares surinamés", 32.52)
    
elif opcion == 11: # Peso uruguayo
    conversor("pesos uruguayos", 38.63)
    
elif opcion == 12: # Bolivar fuerte
    conversor("bolivares fuertes", 248)
        
else: print ("Ingrese una opción correcta")


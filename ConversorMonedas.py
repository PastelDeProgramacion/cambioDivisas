def conversor(tipoDivisa, valorDolar):
    divisa = input("\n驴Cu谩ntos " +tipoDivisa +" a d贸lares va a cambiar?: ")
    divisa = float(divisa)
    dolares = divisa/valorDolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print("Tienes $" + dolares + " d贸lares\n")


menu = """
馃椊CONVERSOR A D脫LARES馃椊

馃挵 Escoja la divisa que desea cambiar a d贸lares馃挼

1- Peso argentino
2- Boliviano
3- Real brasile帽o
4- Peso chileno
5- Peso colombiano
6- D贸lar (Ecuador)
7- D贸lar guayan茅s
8- Guaran铆 paraguayo
9- Nuevo sol peruano
10- D贸lar surinam茅s
11- Peso uruguayo
12- Bolivar fuerte venezolano
 
"""
opcion = int(input(menu))

if opcion == 1: # Peso argentino
    conversor("pesos argentinos", 186.98)
    
elif opcion == 2: # Boliviano
    conversor("bolivianos", 6.85)
    
elif opcion == 3: # Real brasile帽o
    conversor("reales", 4600)
    
elif opcion == 4: # Peso chileno
    conversor("pesos chilenos", 806.80)
       
elif opcion == 5: # Peso colombiano
    conversor("pesos colombianos", 4650)
    
elif opcion == 6: # D贸lar (Ecuador)
    conversor("d贸lares", 1)
    
elif opcion == 7: # D贸lar (Guyana)
    conversor ("d贸lares guayaneses", 210)
        
elif opcion == 8: # Guaran铆
    conversor("guaran铆s", 7341.70)
    
elif opcion == 9: # Sol
    conversor("nuevos soles", 3.83)
    
elif opcion == 10: # D贸lar (Suriname)
    conversor("d贸lares surinam茅s", 32.52)
    
elif opcion == 11: # Peso uruguayo
    conversor("pesos uruguayos", 38.63)
    
elif opcion == 12: # Bolivar fuerte
    conversor("bolivares fuertes", 248)
        
else: print ("Ingrese una opci贸n correcta")


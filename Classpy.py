"""
x=5
x=x*2
print (x);

"""
"""
luis = 5
pedro = 10
#quiero que luis tenga la misma cantidad de dinero que pedro
luis = pedro

print("luis tiene : ",luis," soles");

#quiero que luis tenga 10 soles mas de lo que hoy tiene

luis += 10
"""
vida=100
patada=50
golpe=30
ojo=90
fatality=200

def quitarVida(vida,ataque):
    vida-=ataque

ataque=input("Ingresa tu ataque :")

if ataque=="patada":
   newvida =quitarVida(vida,patada)
   if (newvida<0):
    print("estas vivo, tienes ",newvida, "de salud")
   else: 
        print("has muerto")
        exit()

    if ataque=="golpe":
       newvida=quitarVida(vida,golpe)
       if (newvida<0):
          print("estas vivo, tienes ",newvida, "de salud")
       else: 
        print("has muerto")
        exit()

    if ataque=="ojo":
       newvida=quitarVida(vida,ojo)
       if (newvida<0):
          print("estas vivo, tienes ",newvida, "de salud")
        else: 
            print("has muerto")
            exit()
    if ataque=="fatality":
       newvida=quitarVida(vida,fatality)
       if (newvida<0):
          print("estas vivo, tienes ",newvida, "de salud")
        else: 
            print("has muerto")
            exit()

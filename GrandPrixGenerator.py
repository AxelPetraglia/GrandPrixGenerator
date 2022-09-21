import random
import pandas as pd

class equipo:
    def __init__(self, peso_base, nombre, historial, bonusposteo, peso_rand, peso_cont):
        self.peso_base = peso_base
        self.nombre = nombre
        self.historial = historial
        self.bonusposteo = bonusposteo
        self.peso_rand = peso_rand
        self.peso_cont = peso_cont

#peso_base: el puntaje 1
#historial: equipos más ganadores tienen más chances de seguir siendo buenos (última final ganada = 5; última final perdida = 3, última semifinal = 1, final histórica = 1)
#bonus por posteo: los que en esa tanda hayan publicado sobre futbol tienen un bonus;
#peso random: A veces un equipo puede tener una generación dorada y ese mundial punchean por encima de su talle
#peso_cont: El continente afecta mucho el resultado de lo paises (Eulasia = 5, Pharos = 4, el resto 0)

def load_file():
    datos = pd.read_excel('GrandPrixExcel.xlsx')
    print(datos)

    global equipo1
    equipo1 = equipo(str("1"), (datos.loc[0][0]), str(datos.loc[0][1]), str(datos.loc[0][2]), random.randint(0, 5), str(datos.loc[0][3]))
    peso_equipo1 = str(int(equipo1.historial) + int(equipo1.bonusposteo) + int(equipo1.peso_rand) + int(equipo1.peso_cont))

    print("\nEquipo: " + equipo1.nombre + "\nHistorial: " + str(equipo1.historial))
    print("Bonus por posteo: " + str(equipo1.bonusposteo) + "\nPeso Random: " + str(equipo1.peso_rand) + "\nBonus continental: " + str(equipo1.peso_cont))
    print("\nPeso total = " + peso_equipo1)

    global equipo2
    equipo2 = equipo(str("1"), (datos.loc[1][0]), str(datos.loc[1][1]), str(datos.loc[1][2]), random.randint(1, 5), str(datos.loc[1][3]))
    peso_equipo2 = str(int(equipo2.historial) + int(equipo2.bonusposteo) + int(equipo2.peso_rand) + int(equipo2.peso_cont))

    print("\nEquipo: " + equipo2.nombre + "\nHistorial: " + str(equipo2.historial))
    print("Bonus por posteo: " + str(equipo2.bonusposteo) + "\nPeso Random: " + str(equipo2.peso_rand) + "\nBonus continental: " + str(equipo2.peso_cont))
    print("\nPeso total = " + peso_equipo2)

#Usamos un excel con los datos que pide la class
#Cada grupo en una sheet de excel (no implementando)

def partidos():
    peso_equipo_a = str(int(equipo1.historial) + int(equipo1.bonusposteo) + int(equipo1.peso_rand) + int(equipo1.peso_cont))
    peso_equipo_b = str(int(equipo2.historial) + int(equipo2.bonusposteo) + int(equipo2.peso_rand) + int(equipo2.peso_cont))
    coeficiente1 = int(peso_equipo_a)/(int(peso_equipo_a)+int(peso_equipo_b))
    coeficiente2 = int(peso_equipo_b)/(int(peso_equipo_b)+int(peso_equipo_a))
    print("\nEl coeficiente de " + equipo1.nombre + " es: " + str(coeficiente1))
    print("El coeficiente de " + equipo2.nombre + " es: " + str(coeficiente2))
    #El peso de ambos equipos es la suma de todos los valores de la clase
    #El coeficiente de ambos equipos se calcula con: (peso del equipo) dividido por ((peso del equipo) + (peso del rival))
    #LA SUMA DE LOS DOS COEFICIENTES ES SIEMPRE 1, se divide ese 1 en dos mitades (el mas fuerte tiene la mitad mas grande, el más debil la mitad mas chica)

    coeficiente_partido = random.uniform(0, 1)
    print("\nCoeficiente de partido: " + str(coeficiente_partido))
    #coeficiente_partido es un numero random que se genera entre 0 y 1
    #Si el coeficiente_partido cae en la "mitad" de uno de los equipos, ese equipo gana el partido
    #Ahora, necesitamos que el "1" se divida en tres para agregar una chance de empate
    #El numero de coeficiente_partido así debería caer en tres rangos: el del equipo1 (coeficiente1), del equipo2 (coeficiente2), y del empate (c_empate)

    if coeficiente1 > coeficiente2:
        coeficiente_big = coeficiente1
        coeficiente_small = coeficiente2
    else:
        coeficiente_big = coeficiente2
        coeficiente_small = coeficiente1
    #esto calcula cual es el coeficiente más grande y cual el más chico, para ver cuánta diferencia hay entre ambos
    
    c_empate = 0.33*(1 - (coeficiente_big-coeficiente_small))
    print("Coeficiente de empate: " + str(c_empate))
    
    #La chance MÁXIMA de empate para todo partido es 0.33
    #Para generar la chance de empate (c_empate) del partido se toma el 0.33 y se lo multiplica por (1 - diferencia de los coeficientes)
    #Los dos límites del rango de empate en ese "1" se crean con: 
      #coeficiente1 - (c_empate / 2) = para cortar en el "tercio" de equipo 1
      #coeficiente1 + (c_empate / 2) = para cortar en el "tercio" de equipo 2
      #el rango de empate se genera haciendo el +- a un coeficiente

    if coeficiente_partido < (coeficiente1 - c_empate/2):
      print("\nGanó " + equipo1.nombre)
    elif coeficiente_partido < (coeficiente1 + c_empate/2):
      print("¡Empate!")
    else: 
      print("\nGanó " + equipo2.nombre)

    #Acá está el "cálculo" del partido:       
      #Si el coeficiente_partido generado al azar es menor a (coeficiente1 - chance de empate/2), es porque cayó en el "tercio" del equipo 1
      #Si el coeficiente es menor a (coeficiente1 + c_empate/2), cayó en el "tercio" generado al empate
      #Si no cayó en el equipo1 ni en el empate, cayó en el equipo 2 y gana ese equipo

load_file()
partidos()

print("----------------------------------")

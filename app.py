    # importar la libreria random
import random
#crear variable para mostrar los resultados finales e incluir cuantas rondas fueron en total
rondas = 0
gana_jugador = 0
gana_computadora = 0
empate = 0

while True:
    # leer datos de entrada en la consola
    jugador = input('¿Piedra, papel o tijera? ')
    # convertir la entrada a minusculas
    jugador = jugador.lower()
    print('El jugador eligió:', jugador)
    # generar una lista de opciones para la computadora
    opciones = ['piedra', 'papel', 'tijera']
    # seleccionar una opción al azar
    computadora = random.choice(opciones)
    print('La computadora eligió:', computadora)
    # comparar las opciones del jugador y la computadora
    if jugador == computadora:
        print('Empate')
        #aumentar el contador de empates
        empate += 1
    elif jugador == 'piedra' and computadora == 'tijera':
        print('Ganaste')
        #aumentar el contador de victorias del jugador
        gana_jugador += 1
    elif jugador == 'papel' and computadora == 'piedra':
        print('Ganaste')
        #aumentar el contador de victorias del jugador
        gana_jugador += 1
    elif jugador == 'tijera' and computadora == 'papel':
        print('Ganaste')
        #aumentar el contador de victorias del jugador
        gana_jugador += 1
    #crear elif para cuando se lea un valor invalido
    elif jugador not in opciones:
        print('Valor invalido')
    else:
        print('Perdiste')
        #aumentar el contador de victorias de la computadora
        gana_computadora += 1
    #aumentar el contador de rondas
    rondas += 1
    # preguntar al usuario si desea volver a jugar
    entrada = input('¿Deseas volver a jugar? ')
    # convertir la entrada a minusculas
    if entrada.lower() == 'no':
        break


print('Rondas jugadas:', rondas)
print('Victorias del jugador:', gana_jugador)
print('Victorias de la computadora:', gana_computadora)
print('Empates:', empate)


import random

intentos = 0
numeromin=1
numeromax=20
##agregamos unos correros

print("hola cual es tu nombre wachin : ")
ususario=input()

numeroaleatorio=random.randint(numeromin,numeromax)

print("s hora de jugar "+ ususario + " estoy pensando en un numero entre el "+ str(numeromin) + " y " + str(numeromax) +" adivinas cual  es....?")


#se encargara deejecutar l juego
while intentos < 6:
    print("aver adivina...")
    prueba=input()
    prueba=int(prueba)

    intentos=intentos+1

    if prueba<numeroaleatorio:
        print("tu numero es demasiado bajo ya vas  "+ str(intentos)+ " intentos" )
    if prueba>numeroaleatorio:
        print("tu numeoro es  muy alto ya vas "+ str(intentos)+ " intentos" )
    if prueba== numeroaleatorio:
        break

if prueba == numeroaleatorio:
    print("buen trabajo " + ususario + " adicvinaste mi numero en "+ str(intentos) + " intentos")    

if prueba !=numeroaleatorio:
    print("no , el numero que estaba pensando era " + str(numeroaleatorio))

    #ver video
    #https://www.youtube.com/watch?v=BHdnTvdqA7A
    #audiolibro
    #https://www.youtube.com/watch?v=ZoiFxJYt5Qk
    #libro
    #https://es.slideshare.net/orzoe300/1la-meta-pdf
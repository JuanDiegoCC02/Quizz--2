#Metodo de Cifrado de Cesar

class Juego:
    def __init__(self, nombre_jugador):
      
        self.nombre_jugador = nombre_jugador
        self.jugando = False

    def iniciar_juego(self):
        self.jugando = True
        print(f"\n¡Bienvenido al juego, {self.nombre_jugador}!")
        print("El juego ha comenzado..")
        
        #Ingreso del mensaje e impresion del msj_Cifrado
        mensaje=input("Ingrese el mensaje que desea Cifrar: ")
        msj_Cifrado=self.Cifrado_de_Cesar(mensaje)
        print(f"Mensaje Cifrado: {msj_Cifrado}")

        print("¡Gracias por jugar!\n")

    def salir(self):
        print(f"\nHasta luego, {self.nombre_jugador}. ¡Vuelve pronto!")


    #Funcion del Cifrado
    def Cifrado_de_Cesar(self, mensaje):
        
        #Declaracion de (ABCEDARIO), (Movimiento de Cifrado) y (la variable donde se va almacenar el msj_Cifrado)
        abcedario = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
        movimiento = 1
        msj_Cifrado=""

       #For para recorrer las letras del mensaje  //Metodo .upper para la conversion de letras a MAYUCULAS
        for letra in mensaje.upper():
            if letra in abcedario:
               
               #Aplicacion del metodo .find para enontrar la posicion de la letra
               i=abcedario.find(letra)
               i+=movimiento
               if i >=27:
                     i-=27
               msj_Cifrado += abcedario[i]

            else:
                msj_Cifrado+=letra

        return msj_Cifrado

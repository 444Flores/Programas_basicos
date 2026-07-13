# Programa 3: Índice de Masa Corporal (IMC)

def calcular_imc():

    print("Calcular el IMC (indice de masa corporal)")
    try:
        #pedimos los datos al usuario
        peso = float(input("Ingresa tu peso en kilogramos (solo numeros, ej. 72.5): "))
        altura = float(input("Ingresa tu altura en metros (solo numeros, ej. 1.70): "))
        
        #hacemos el calculo de imc
        imc = peso / (altura ** 2)
        
        #imprimimos los resultados
        print(f"\nResultados:")
        print(f"Peso: {peso} kg | Altura: {altura} m")
        print(f"Tu Indice de Masa Corporal (IMC) es: {imc:.2f}\n")

        #si hay un error saltara este mensaje
    except ValueError:
        print("Error: Por favor ingresa valores numericos validos.\n")

#solo ejecuta la funcion si el archivo es ejecutado directamente
if __name__ == "__main__":
    calcular_imc()
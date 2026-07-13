# Programa 2: Promedio de tres numeros

def calcular_promedio():
    print("Calcula el promedio de tres numeros")
    try:
        #pedimos los 3 numeros al usuario
        num1 = float(input("Ingresa el primer numero: "))
        num2 = float(input("Ingresa el segundo numero: "))
        num3 = float(input("Ingresa el tercer numero: "))
        
        #calculamos el promedio
        promedio = (num1 + num2 + num3) / 3
        
        #imprimimos los resultados
        print(f"\nResultados:")
        print(f"Numeros ingresados: {num1}, {num2}, {num3}")
        print(f"El promedio de los numeros es: {promedio:.2f}\n")

        #si hay un error saltara este mensaje
    except ValueError:
        print("Error: Por favor ingresa valores numericos validos.\n")

#solo ejecuta la funcion si el archivo es ejecutado directamente
if __name__ == "__main__":
    calcular_promedio()
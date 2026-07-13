# Programa 1: area de un rectangulo
def calcular_area():
    print("Calcula el area de un rectangulo")
    try:
        #solicitamos al usuario que ingrese los datos
        base = float(input("Ingresa la base del rectangulo: "))
        altura = float(input("Ingresa la altura del rectangulo: "))

        #calculamos el area del rectangulo
        area = base * altura

        #imprimimos los resultados
        print(f"\nResultados:")
        print(f"Base ingresada: {base}")
        print(f"Altura ingresada: {altura}")
        print(f"El area del rectangulo es: {area}\n")

        #si hay un error saltara este mensaje
    except ValueError:
        print("Error: Por favor ingresa valores numericos validos.\n")

#solo ejecuta la funcion si el archivo es ejecutado directamente
if __name__ == "__main__":
    calcular_area()
# Programa 4: Salario neto

def calcular_salario_neto():
    print("Calculo de salasrio neto")
    try:
        #solicitamos los datos al usuario
        salario_bruto = float(input("Ingresa el salario bruto mensual: $"))
        porcentaje_impuestos = float(input("Ingresa el porcentaje de impuestos (solo numero(s), ej. 16): "))
        deducciones = float(input("Ingresa el total de otras deducciones: $"))
        
        #hacemos los calculos
        retencion_impuestos = salario_bruto * (porcentaje_impuestos / 100)
        salario_neto = salario_bruto - retencion_impuestos - deducciones
        
        #imprimimos los resultados
        print(f"\nNOMINA DE PAGO: ")
        print(f"Salario Bruto: ${salario_bruto:.2f}")
        print(f"Impuestos Retenidos ({porcentaje_impuestos}%): ${retencion_impuestos:.2f}")
        print(f"Otras Deducciones: ${deducciones:.2f}")
        print(f"-----------------------------------")
        print(f"Salario Neto a Recibir: ${salario_neto:.2f}\n")

        #si hay un error saltara este mensaje
    except ValueError:
        print("Error: Por favor ingresa valores numéricos válidos.\n")

#solo ejecuta la funcion si el archivo es ejecutado directamente
if __name__ == "__main__":
    calcular_salario_neto()
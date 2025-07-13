from evaluador import calcular_promedio_area, calcular_nota_final, estado_actual

def ingresar_notas(nombre_area):
    notas = []
    cantidad = int(input(f"\n¿Cuántas notas tienes en {nombre_area}? "))
    for i in range(cantidad):
        nota = float(input(f"Ingrese la nota {i+1}: "))
        peso = float(input(f"Ingrese el peso (por ejemplo 1 para normal, 2 para doble): "))
        notas.append((nota, peso))
    return notas

def main():
    print("📚 Bienvenido a la calculadora de Tecsup")
    
    # Pesos del curso
    peso_teoria = float(input("Peso de Teoría (ej. 0.4): "))
    peso_laboratorio = float(input("Peso de Laboratorio (ej. 0.6): "))
    
    # Notas
    notas_teoria = ingresar_notas("Teoría")
    notas_laboratorio = ingresar_notas("Laboratorio")
    
    # Promedios por área
    promedio_teoria = calcular_promedio_area(notas_teoria)
    promedio_laboratorio = calcular_promedio_area(notas_laboratorio)
    
    # Promedio final
    nota_final = calcular_nota_final(peso_teoria, promedio_teoria, peso_laboratorio, promedio_laboratorio)
    
    # Resultado
    print("\n----- RESULTADOS -----")
    print(f"Promedio Teoría: {promedio_teoria}")
    print(f"Promedio Laboratorio: {promedio_laboratorio}")
    print(f"Nota Final del Curso: {nota_final}")
    print(f"Estado: {estado_actual(nota_final)}")

if __name__ == "__main__":
    main()

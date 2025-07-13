##Estoy creando el archivo Evaluador.py 
NOTA_APROBATORIA = 12.5
NOTA_SUSTI = 10.5

def calcular_promedio_area(notas):
    total = 0
    total_pesos = 0
    for nota, peso in notas:
        total += nota * peso
        total_pesos += peso
    if total_pesos == 0:
        return 0
    return round(total / total_pesos, 2)

def calcular_nota_final(peso_teoria, promedio_teoria, peso_laboratorio, promedio_laboratorio):
    return round(
        promedio_teoria * peso_teoria + promedio_laboratorio * peso_laboratorio, 2
    )

def estado_actual(nota_final):
    if nota_final >= NOTA_APROBATORIA:
        return "✅ Aprobado"
    elif nota_final >= NOTA_SUSTI:
        return "⚠️ Va a Sustitutorio"
    else:
        return "❌ Desaprobado"
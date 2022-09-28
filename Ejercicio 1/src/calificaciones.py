def resultados():
    aciertos = int(input('Numero de aciertos: '))
    errores = int(input('Numero de errores: '))
    notfound = int(input('Numero de respuestas sin marcar: '))
    return [aciertos, errores, notfound]

def calculo_calificacion(aciertos, errores, notfound):
    totalrespuestas = aciertos + notfound
    parte1 = (aciertos*10)/(totalrespuestas)
    parte2 = (errores*10)/(50 - totalrespuestas)
    nota = parte1 - parte2
    nota = max(0, nota) 
    return nota

#______________________________________________________________________________________________________________________

'''def calcula_nota_cuatrimestre(cuestionarios, parcial, proyecto):
    if proyecto < 5:
        nota_suspensa = 3
        return nota_suspensa
    elif 5 <= proyecto <= 10:
            #¡¡¡¡averiguar como sumar los elementos de la tupla cuestionarios!!!!
        suma_cuestionarios = cuestionarios[0]+cuestionarios[1]+cuestionarios[2]  
        nota_cuatrimestre = (0.1*suma_cuestionarios) + (0.6*parcial)+ (0.1*proyecto)
        return nota_cuatrimestre

    

def notas_cuestionarios():
    c1 = float(input('Nota del primer cuestionario: '))
    c2 = float(input('Nota del segundo cuestionario: '))
    c3 = float(input('Nota del tercer cuestionario: '))
    cuestionarios = (c1, c2, c3)
    return cuestionarios
def nota_parciales():
    parciales = float(input('Nota del primer parcial: '))
    return parciales
def nota_proyectos():
    proyecto = float(input('Nota del primer proyecto: '))
    return proyecto'''

#def calcula_nota_evaluacion_continua(cuestionarios, parciales, proyectos):
    
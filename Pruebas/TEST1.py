'''import csv
import statistics
from matplotlib import pyplot as plt
def lista_espectadores(fichero):
    espectadores = []
    with open(fichero, encoding = 'utf-8') as j:
        for linea in j:
            season, views= linea.split(',')
            season=int(season)
            views=float(views)
            tupla= (season, views)
            espectadores.append(tupla)
    return espectadores
espectacion=lista_espectadores('./data/GH.csv')
print(espectacion[:6])'''
#a, b, c = 5, 2, 3
#print('{0} {1:2d} {2:03d} {3:.2f} {4:04.1f}'.format(a, b, c, a/b, a/c))
#print(2+(3//5)**2/2)
#print('La media de {0} y {1} es {2:.2f}'.format(4, 5, (4 + 5) / 2))
nombre= input('Como se llama: P') 
peso= float
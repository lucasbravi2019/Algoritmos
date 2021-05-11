# Area de cuadrado, triangulo y circulo
import math
def elegir_figura():
    global figura
    figura = input('Por favor ingrese el nombre de la figura de la que desee calcular el area \n')
    return figura
def obtener_lado_cuadrado():  
    global lado 
    lado = input('Por favor diga la longitud de un lado \n')
def calcular_area_cuadrado():
    obtener_lado_cuadrado()
    global area
    area = float(lado) ** 2
    area = round(area, 2)
def obtener_lado_triangulo():
    global base
    base = input('Por favor diga la longitud de la base \n')
    global altura
    altura = input('Por favor diga la longitud de la altura \n')
def calcular_area_triangulo():
    obtener_lado_triangulo()
    global area
    area = float(base) * float(altura) / 2
    area = round(area, 2)
def obtener_diametro_circulo():
    global diametro
    diametro = input('Por favor ingrese el diametro del circulo \n')
def calcular_area_circulo():
    obtener_diametro_circulo()
    global area 
    area = float(diametro) ** 2 * math.pi / 4
    area = round(area, 2)
def calcular_area():
    elegir_figura()
    if figura == 'cuadrado':
        calcular_area_cuadrado()
        print(f'El area del cuadrado es de {area} m2')
    elif figura == 'triangulo':
        calcular_area_triangulo()
        print(f'El area del triangulo es de {area} m2')
    elif figura == 'circulo':
        calcular_area_circulo()
        print(f'El area del circulo es de {area} m2')
    else:
        print('Por favor escriba "cuadrado", "triangulo" o "circulo"')
        calcular_area()
calcular_area()    

#Calificacion de alumno

def obtener_asistencia():
    global asistencia
    asistencia = input('Por favor indique el porcentaje de asistencia del alumno \n')
    asistencia = float(asistencia) / 100
def obtener_calificacion():
    global calificacion
    calificacion = input('Por favor indique la calificacion final del alumno \n')
    calificacion = float(calificacion)
def condicion_alumno():
    obtener_asistencia()
    obtener_calificacion()
    if asistencia >= 0.8 and calificacion >= 7:
        print('Aprobado')
    elif asistencia <= 0.8 and calificacion >=7:
        print('Desaprobado por inasistencias')
    elif calificacion < 7:
        print('Desaprobado')
    else:
        print('Error')
condicion_alumno()

# Mayor, intermedio y menor

def obtener_numeros():
    global numero_a, numero_b, numero_c
    numero_a = input('Por favor ingrese un numero \n')
    numero_b = input('Por favor ingrese un numero \n')
    numero_c = input('Por favor ingrese un numero \n')
    numero_a = float(numero_a)
    numero_b = float(numero_b)
    numero_c = float(numero_c)
def analizar_mayor():
    global mayor 
    mayor = max(numero_a, numero_b, numero_c)
    print(f'El numero mas grande es {mayor}')
def analizar_intermedio():
    global intermedio
    intermedio = (numero_a + numero_b + numero_c) - mayor - menor
    print(f'El intermedio es {intermedio}')
def analizar_menor():
    global menor
    menor = min(numero_a, numero_b, numero_c)
    print(f'El numero menor es {menor}')
def analizar_numeros():
    obtener_numeros()
    analizar_mayor()
    analizar_menor()
    analizar_intermedio()
analizar_numeros()
# print("ACT 1")
# print("--------")
# num = int(input("Introduce un número: "))
# if num % 2 == 0:
#     print("Es par")
# else:
#     print("Es impar")

# print("ACT 2")
# print("--------")
# num1 = int(input("Introduce el primer número: "))
# num2 = int(input("Introduce el segundo número: "))
# if num1 > num2:
#     print(f"{num1} es mayor que {num2}")
# elif num1 == num2:
#     print(f"{num1} y {num2} son iguales")
# else:
#     print(f"{num2} es mayor que {num1}")

# print("ACT 3")
# print("--------")
# number = int(input("Introduce un número: "))
# if number % 5 == 0 and number % 7 == 0:
#     print(f"{number} es múltiplo de 5 y 7")
# elif number % 5 == 0:
#     print(f"{number} es múltiplo de 5")
# elif number % 7 == 0:
#     print(f"{number} es múltiplo de 7")
# else:

# print("ACT 4")
# print ("-------")
# edad = (int(input("Introduzca su edad: ")))
# if 0 <= edad < 66:
#     if edad < 7:
#         print("Educación infantil")
#     elif edad < 12:
#         print("Educación primaria")
#     elif edad < 17:
#         print("Educación secundaria obligatoria")
#     else:
#         print("Enseñanza post-obligatoria")
# else:
#     print("Datos no válidos")

# print("ACT 5")
# print("--------")
# number1=int(input("Introduce el primer numero: "))
# number2=int(input("Introduce el segundo numero: "))
# number3=int(input("Introduce el tercer numero: "))
# number4=int(input("Introduce el cuarto numero: "))
# media = ((number1 + number2 + number3 + number4) / 4)
# numerosuperiormedia = ""
# contador = 0
# if number1>media:
#     contador +=1
#     numerosuperiormedia+=str(number1)+", "
# if number2>media:
#     contador +=1
#     numerosuperiormedia+=str(number2)+", "
# if number3>media:
#     contador +=1
#     numerosuperiormedia+=str(number3)+", "
# if number4>media:
#     contador +=1 
#     numerosuperiormedia+=str(number4)+", "
# print("La media es, " , media , "hay," , contador , "numeros superiores a la media: ", numerosuperiormedia )

# print("ACT 6")
# print("--------")
# num1 = int(input("Introduce el primer numero: "))
# num2 = int(input("Introduce el segundo numero: "))
# if num1%num2 == 0:
#     print("Son múltiplos entre sí")
# else:
#     print("No son múltiplos entre sí")

# print("ACT 7")
# print("--------")
# caracter = (input("Introduce un caracter: "))
# if caracter == "a" or caracter == "A" or caracter == "á" or caracter == "Á":
#     print("Es la primera vocal")
# elif caracter == "e" or caracter == "E" or caracter == "é" or caracter == "É":
#     print("Es la segunda vocal")
# elif caracter == "i" or caracter == "I" or caracter == "í" or caracter == "Í":
#     print("Es la tercera vocal")
# elif caracter == "o" or caracter == "O" or caracter == "ó" or caracter == "Ó":
#     print("Es la cuarta vocal")
# elif caracter == "u" or caracter == "U" or caracter == "ú" or caracter == "Ú":
#     print("Es la quinta vocal")
# else:
#     print("Es una consonante")

# print("ACT 8")
# print("--------")
# edad = int(input("Introduzca su edad: "))
# estado_civil = input("¿Cuál es su estado civil?: ")
# if (estado_civil == "soltero" or "divorciado" or "Soltero" or "Divorciado") and edad < 35:
#     print("Su porcentaje de retención es de un 12%")
# elif (estado_civil == "viudo" or "casado" or "Viudo" or "Casado") and edad < 35:
#     print("Su porcentaje de retención es de un 11,3%")
# elif 50 < edad :
#     print("Su porcentaje de retención es del 8,5%")
# else :
#     print("Su retención es del 10,5%")


# print("ACT 9")
# print("--------")
# dia_semana = int(input("Introduzca un día de la semana: "))
# if 7 < dia_semana or dia_semana <= 0 :
#     print("Te has pasado colega.")
# elif dia_semana == 1:
#     print("Lunes")
# elif dia_semana == 2:
#     print("Martes")
# elif dia_semana == 3:
#     print("Miércoles")
# elif dia_semana == 4:
#     print("Jueves")
# elif dia_semana == 5:
#     print("Viernes")
# elif dia_semana == 6:
#     print("Sábado")
# elif dia_semana == 7:
#     print("Domingo")


# print("ACT 10")
# print("--------")
# hora1 = int(input("Introduce la hora: "))
# minutos1 = int(input("Introduce los minutos: "))
# segundos1 = int(input("Introduce los segundos: "))
# hora2 = int(input("Introduce la hora: "))
# minutos2 = int(input("Introduce los minutos: "))
# segundos2 = int(input("Introduce los segundos: "))
# mensaje1 = "Hora 1 es mayor"
# mensaje2 = "Hora 2 es mayor"
# if (24 < hora1 or 24 < hora2) or (59 < minutos1 or 59 < minutos2) or (59 < segundos1 or 59 < segundos2):
#     print("Datos no válidos")
# elif hora1 > hora2:
#     print(mensaje1)
# elif hora2 > hora1:
#     print(mensaje2)
# elif (hora1 == hora2) and (minutos1 > minutos2):
#     print(mensaje1)
# elif (hora1 == hora2) and (minutos1 < minutos2):
#     print(mensaje2)
# elif (hora1 == hora2) and (minutos1 == minutos2) and (segundos1 > segundos2):
#     print(mensaje1)
# elif (hora1 == hora2) and (minutos1 == minutos2) and (segundos1 < segundos2):
#     print(mensaje2)


# print("ACT 11")
# print("--------")
# cliente = (input("¿Eres estudiante o regular?: "))
# cantidad = int(input("¿Cuánto has gastado?: "))
# descuento15 = cantidad * 15 / 100
# descuento12 = cantidad * 12 / 100
# descuento10 = cantidad * 10 / 100
# descuento5 = cantidad * 5 / 100
# if cantidad <= 0:
#     print("A tu casa anda.")
# elif ((cliente == "estudiante" or cliente == "Estudiante") and (100 <= cantidad)):
#     (print("Se aplica un descuento del 15%", cantidad - descuento15))
# elif ((cliente == "estudiante" or cliente == "Estudiante") and (cantidad < 100)):
#     (print("Se aplica un descuento del 10%", cantidad - descuento10))
# elif ((cliente == "regular" or cliente == "Regular") and  (200 <= cantidad)):
#     (print("Se aplica un descuento del 12%", cantidad - descuento12))
# else:
#     (print("Se aplica un descuento del 5%", cantidad - descuento5))




# print("ACT 12")
# print("--------")
# weekday = int(input("Introduzca un día de la semana: "))
# vacaciones = (input("¿Estás de vacaciones?: ").lower())
# if ((weekday <= 0) or (weekday > 7)) or ((vacaciones != "si") and (vacaciones != "no")) :
#     print("Datos no válidos")
# elif (( 1 <= weekday <= 5) and (vacaciones == "no")):
#     print("La alarma suena a las 7:00")
# elif ((weekday >= 6) and (vacaciones == "no")):
#     print("La alarma suena a las 10:00")
# elif (vacaciones == "si"):
#     print("La alarma está apagada")




# print("ACT 13")
# print("--------")
# caracter = input("Introduzca un caracter: ")
# num1 = int(input("Introduzca un número: "))
# num2 = int(input("Introduzca otro número: "))
# if caracter == "+" :
#     print(num1 + num2)
# elif caracter == "-" :
#     print(num1 - num2)
# elif caracter == "*" :
#     print(num1 * num2)
# elif caracter == "/":
#     print(num1 / num2)
# elif caracter == "//":
#     print(num1 // num2)
# elif caracter == "**":
#     print(num1 ** num2)
# elif caracter == ">":
#     print(num1 > num2)
# elif caracter == "<":
#     print(num1 < num2)
# elif caracter == "==":
#     print(num1 == num2)
# elif caracter == "!=":
#     print(num1 != num2)
# else:
#     print(f"{num1} {caracter} {num2}")


# print("ACT 14")
# print("--------")
# monedas2e = int(input("¿Cuántas monedas de 2€ tienes?: ")) * 2
# monedas1e = int(input("¿Cuántas monedas de 1€ tienes?: ")) * 1
# monedas50c = int(input("¿Cuántas monedas de 50 centimos tienes?: " )) * 0.50
# monedas20c = int(input("¿Cuántas monedas de 20 centimos tienes?: ")) * 0.20
# monedas10c = int(input("¿Cuántas monedas de 10 centimos tienes?: ")) * 0.10
# monedas5c = int(input("¿Cuántas monedas de 5 centimos tienes?: ")) * 0.05
# monedas2c = int(input("¿Cuántas monedas de 2 centimos tienes?: ")) * 0.02
# monedas1c = int(input("¿Cuántas monedas de 1 centimo tienes?: ")) * 0.01
# dinero_total = (monedas2e + monedas1e + monedas50c + monedas20c + monedas10c + monedas5c + monedas2c + monedas1c)
# print(f"Tienes en total {dinero_total}€")


# print("ACT 15")
# print("---------")
# dia = int(input("Introduce el día: "))
# mes = int(input("Introdue el mes: "))
# year = int(input("Introduce el año: "))
# fecha_completa = (f"{dia}/{mes}/{year}")
# if (dia == 30 and mes == 2) or (dia == 31 and mes == 4) or (dia == 31 and mes == 6) or (dia == 31 and mes == 9) or (dia == 31 and mes == 11) or (dia > 31) or (mes > 12) :
#     print("Fecha no válida")
# elif (year % 4 == 0 ) or (year // 4 == 0 and year // 100 == 0 and year // 400 == 0 ):
#     print (f"Es un año bisiesto {fecha_completa}")
# elif year > 2026:
#     print("Esa fecha no existe")
# else:
#     print(f"La fecha es válida {fecha_completa}")

# print("ACT 16")
# print ("-------")
# base = int(input("Introduce la base: "))
# exponente = int(input("Introduce el exponente: "))
# if exponente > 0:
#     print(base**exponente)
# elif exponente == 0:
#     print(base**exponente)
# else:
#     print(1/base**exponente)


# print("ACT 17")
# print("--------")
# lado1 = int(input("Introduce cuanto mide el lado 1: "))
# lado2 = int(input("Introduce cuanto mide el lado 2: "))
# lado3 = int(input("Introduce cuanto mide el lado 3: "))
# if (lado1 + lado2 < lado3):
#     print("Figura no válida")
# elif (lado1 == lado2 == lado3):
#     print("Triángulo Equilatero")
# elif (lado1 == lado2 != lado3) or (lado1 == lado3 !=lado2) or (lado2 == lado3 != lado1):
#     print("Triángulo Isósceles")
# elif ((lado1** 2) + (lado2**2) == lado3**2):
#     print("Satisface el Teorema de Pitágoras")

# print("ACT 18")
# print("--------")
# num1 = int(input("Pon un número: "))
# num2 = int(input("Pon otro número: "))
# print(f"La distancia entre {num1} y {num2} es:", (abs(num1 - num2)))


# print("ACT 19")
# print("--------")
# alumnos = int(input("¿Cuántos alumnos van al viaje?: "))
# if alumnos <= 0:
#     print("Datos no válidos")
# elif alumnos >= 100:
#     print("Cada alumno paga 65€, y a la compañía cobrará", alumnos*65,"€")
# elif 50 <= alumnos <=99:
#     print("Cada alumno paga 70€, y a la compañía cobrará", alumnos*70,"€")
# elif 30 <= alumnos <=49:
#     print("Cada alumno paga 95€, y a la compañía cobrará", alumnos*95,"€")
# else:
#     menos30 = 2500//alumnos
#     print((f"Cada alumno pagará {menos30}€ y la compañía cobrará 2500€"))


# print("ACT 20")
# print("--------")
# dia = (input("¿Qué día es hoy?: "))
# mins= int(input("¿Cuántos minutos has estado de llamada?: "))
# turno = (input("¿En qué turno se ha hecho la llamada?: "))

# if mins <= 10:
#     precio = mins * 0.66
# elif mins <= 13:
#     precio = 6.60 + (mins - 10) * 0.50
# elif mins <=15:
#     precio = 8.10 + (mins - 13) * 0.45
# else:
#     precio = 9 + (mins - 15) * 0.35

# if dia == "domingo":
#     precio = precio * 1.03
# elif turno == "mañana":
#     precio = precio * 1.15
# elif turno == "tarde":
#     precio = precio * 1.10

# print (f"El precio total a pagar es de {precio}€")


# print("ACT 21")
# print("--------")
# maths = int(input("¿Cuánta nota has sacado en Mates?: "))
# english = int(input("¿Cuánta nota has sacado en Inglés?: "))
# programming = int(input("¿Cuánta nota has sacado en Programación?: "))
# attendance = int(input("¿Cúanto porciento tienes de asistencia?: "))
# avg = ((maths + english + programming) /3)

# if avg >= 85:
#     print("Admitido con beca.")
# elif (70 <= avg <= 84) and attendance >= 75:
#     print("Admitido sin beca.")
# elif (60 <= avg <= 69):
#     print("Estás en espera.")
# else:
#     print("Solicitud rechazada.")

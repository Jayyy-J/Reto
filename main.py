Código: generador_contraseñas.py

import random
import string

def generar_contraseña(longitud, incluir_mayusculas, incluir_minusculas, incluir_numeros, incluir_simbolos):

 caracteres = ""
if incluir_mayusculas:
 caracteres += string.ascii_uppercase
if incluir_minusculas:
 caracteres += string.ascii_lowercase
if incluir_numeros:
 caracteres += string.digits
if incluir_simbolos:
 caracteres += string.punctuation

if not caracteres:
return "Debe seleccionar al menos un tipo de carácter."

  return ''.join(random.choice(caracteres) for _ in range(longitud))

def menu_interactivo():
print("¡Bienvenido al Generador de Contraseñas Seguras!")
print("Este programa te ayudará a crear contraseñas personalizadas y seguras.\n")

while True:
try:
  longitud = int(input("Ingresa la longitud deseada para tu contraseña (mínimo 8): "))
if longitud < 8:
 print("La longitud mínima es de 8 caracteres. Inténtalo de nuevo.")
continue
except ValueError:
print("Por favor, ingresa un número válido.")
continue

print("\nSelecciona los tipos de caracteres a incluir:")
incluir_mayusculas = input("¿Incluir letras mayúsculas? (s/n): ").lower() == 's'
incluir_minusculas = input("¿Incluir letras minúsculas? (s/n): ").lower() == 's'
incluir_numeros = input("¿Incluir números? (s/n): ").lower() == 's'
incluir_simbolos = input("¿Incluir símbolos? (s/n): ").lower() == 's'

contraseña = generar_contraseña(longitud, incluir_mayusculas, incluir_minusculas, incluir_numeros, incluir_simbolos)
print(f"\nTu contraseña generada es: {contraseña}")

otra = input("\n¿Deseas generar otra contraseña? (s/n): ").lower()
if otra != 's':
print("¡Gracias por usar el Generador de Contraseñas Seguras! Hasta pronto.")
break

if name == "main":
menu_interactivo()

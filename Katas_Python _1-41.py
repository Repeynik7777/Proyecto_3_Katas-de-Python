""" 1. Escribe una función que reciba una cadena de texto como parámetro y devuelva un diccionario con las frecuencias
de cada letra en la cadena. Los espacios no deben ser considerados"""

def contar_frecuencias(cadena):
    frecuencias = {}
    for letra in cadena:
        if letra != ' ':
            if letra in frecuencias:
                frecuencias[letra] += 1
            else:
                frecuencias[letra] = 1
    return frecuencias

texto = "rrikki-tiki-tavi"
resultado = contar_frecuencias(texto)
print(resultado)

#=========================================================================================================

""" 2. Dada una lista de números, obtén una nueva lista con el doble de cada valor. Usa la función map()"""

numeros = [1, 2, 3, 4, 5]
dobles = list(map(lambda x: x * 2, numeros))
print(dobles)

#=========================================================================================================

""" 3. Escribe una función que tome una lista de palabras y una palabra objetivo como parámetros. La función debe
devolver una lista con todas las palabras de la lista original que contengan la palabra objetivo."""

def buscar_palabras_con_objetivo(lista_palabras, palabra_objetivo):
    resultado = [palabra for palabra in lista_palabras if palabra_objetivo in palabra]
    return resultado

palabras = ["manzana", "banana", "naranja", "pan", "manantial"]
objetivo = "man"

coincidencias = buscar_palabras_con_objetivo(palabras, objetivo)
print(coincidencias)

#=========================================================================================================

""" 4. Genera una función que calcule la diferencia entre los valores de dos listas. Usa la función map()"""

def diferencias_entre_listas(lista1, lista2):
    return list(map(lambda x, y: x - y, lista1, lista2))
a = [10, 20, 30]
b = [1, 5, 10]

resultado = diferencias_entre_listas(a, b)
print(resultado)

#=========================================================================================================

""" 5. Ecribe una función que tome una lista de números como parámetro y un valor opcional nota_aprobado, que por
defecto es 5. La función debe calcular la media de los números en la lista y determinar si la media es mayor o igual
que nota aprobado. Si es así, el estado será "aprobado", de lo contrario, será "suspenso". La función debe devolver
una tupla que contenga la media y el estado"""

def evaluar_notas(lista_numeros, nota_aprobado=5):
    if not lista_numeros:
        return (0, "sin notas")
    
    media = sum(lista_numeros) / len(lista_numeros)
    estado = "aprobado" if media >= nota_aprobado else "suspenso"
    return (media, estado)

notas = [4, 6, 5.5, 7]
resultado = evaluar_notas(notas)
print(resultado)  # (5.625, 'aprobado')


#=========================================================================================================


""" 6. Escribe una función que calcule el factorial de un número de manera recursiva."""

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

print(factorial(5))  

#=========================================================================================================

""" 7. Genera una función que convierta una lista de tuplas a una lista de strings. Usa la función map()"""

def tuplas_a_strings(lista_tuplas):
    return list(map(lambda tupla: ' '.join(map(str, tupla)), lista_tuplas))

tuplas = [(1, 2), (3, 4), (5, 6)]
resultado = tuplas_a_strings(tuplas)
print(resultado)

#=========================================================================================================

""" 8. Escribe un programa que pida al usuario dos números e intente dividirlos. Si el usuario ingresa un valor no numérico
o intenta dividir por cero, maneja esas excepciones de manera adecuada. Asegúrate de mostrar un mensaje
indicando si la división fue exitosa o no."""

def dividir_numeros():
    try:
        num1 = float(input("Introduce el primer número: "))
        num2 = float(input("Introduce el segundo número: "))
        
        resultado = num1 / num2
        print(f"División exitosa. El resultado es: {resultado}")
    
    except ValueError:
        print("Error: Debes ingresar valores numéricos.")
    
    except ZeroDivisionError:
        print("Error: No se puede dividir por cero.")
    
    else:
        print("La operación se realizó correctamente.")
    
    finally:
        print("Programa finalizado.")

# Ejecutar la función
dividir_numeros()

#=========================================================================================================

""" 9. Escribe una función que tome una lista de nombres de mascotas como parámetro y devuelva una nueva lista
excluyendo ciertas mascotas prohibidas en España. La lista de mascotas a excluir es ["Mapache", "Tigre",
"Serpiente Pitón", "Cocodrilo", "Oso"].Usa la función filter()"""

def filtrar_mascotas_permitidas(lista_mascotas):
    prohibidas = {"Mapache", "Tigre", "Serpiente Pitón", "Cocodrilo", "Oso"}
    return list(filter(lambda mascota: mascota not in prohibidas, lista_mascotas))

mascotas = ["Perro", "Gato", "Tigre", "Canario", "Mapache", "Conejo"]
resultado = filtrar_mascotas_permitidas(mascotas)
print(resultado)

#=========================================================================================================

""" 10. Escribe una función que reciba una lista de números y calcule su promedio. Si la lista está vacía, lanza una
excepción personalizada y maneja el error adecuadamente."""

class ListaVaciaError(Exception):
    """Excepción personalizada para listas vacías."""
    pass

def calcular_promedio(lista):
    if not lista:
        raise ListaVaciaError("Error: La lista está vacía. No se puede calcular el promedio.")
    
    return sum(lista) / len(lista)


try:
    numeros = [7, 8, 9]
    promedio = calcular_promedio(numeros)
    print(f"El promedio es: {promedio}")
except ListaVaciaError as e:
    print(e)

# Resultado: El promedio es: 8.0

#=========================================================================================================

""" 11.  Escribe un programa que pida al usuario que introduzca su edad. Si el usuario ingresa un valor no numérico o un
valor fuera del rango esperado (por ejemplo, menor que 0 o mayor que 120, maneja las excepciones
adecuadamente."""

try:
    edad = int(input("Introduce tu edad: "))
    if edad < 0 or edad > 120:
        raise ValueError("Edad fuera de rango válido (0-120).")
    print(f"Tienes {edad} años.")
except ValueError as e:
    print(f"Entrada inválida: {e}")


#=========================================================================================================

""" 12. Genera una función que al recibir una frase devuelva una lista con la longitud de cada palabra. Usa la función map()"""

def longitud_palabras(frase):
    palabras = frase.split()
    return list(map(len, palabras))

print(longitud_palabras("Hola mundo en Python"))
# [4, 5, 2, 6]

#=========================================================================================================

""" 13. Genera una función la cual, para un conjunto de caracteres, devuelva una lista de tuplas con cada letra en
mayúsculas y minúsculas. Las letras no pueden estar repetidas .Usa la función map()"""

def letras_mayus_minus(letras):
    unicas = set(letras)
    return list(map(lambda c: (c.upper(), c.lower()), unicas))

print(letras_mayus_minus("aAbBc"))
# [('B', 'b'), ('A', 'a'), ('C', 'c')]

#=========================================================================================================

""" 14. Crea una función que retorne las palabras de una lista de palabras que comience con una letra en especifico. Usa la
función filter()"""

def palabras_con_letra(lista, letra):
    return list(filter(lambda palabra: palabra.startswith(letra), lista))

print(palabras_con_letra(["gato", "perro", "gorila", "pez"], "g"))
# ['gato', 'gorila']

#=========================================================================================================

""" 15. Crea una función lambda que sume 3 a cada número de una lista dada."""

sumar_tres = lambda lista: list(map(lambda x: x + 3, lista))

print(sumar_tres([1, 2, 3]))
# [4, 5, 6]

#=========================================================================================================

""" 16. Escribe una función que tome una cadena de texto y un número entero n como parámetros y devuelva una lista de
todas las palabras que sean más largas que n. Usa la función filter()"""

def palabras_largas(frase, n):
    palabras = frase.split()
    return list(filter(lambda palabra: len(palabra) > n, palabras))

print(palabras_largas("El conocimiento es poder", 4))
# ['conocimiento', 'poder']

#=========================================================================================================

""" 17. Crea una función que tome una lista de dígitos y devuelva el número correspondiente. Por ejemplo, 5,7,2
corresponde al número quinientos setenta y dos 572. Usa la función reduce()"""

from functools import reduce

def digitos_a_numero(digitos):
    return reduce(lambda x, y: x * 10 + y, digitos)

print(digitos_a_numero([5, 7, 2]))
# 572

#=========================================================================================================

""" 18. Escribe un programa en Python que cree una lista de diccionarios que contenga información de estudiantes
(nombre, edad, calificación) y use la función filter para extraer a los estudiantes con una calificación mayor o igual a
90. Usa la función filter()"""

estudiantes = [
    {"nombre": "Ana", "edad": 20, "nota": 95},
    {"nombre": "Luis", "edad": 22, "nota": 85},
    {"nombre": "Marta", "edad": 21, "nota": 90}
]

aprobados = list(filter(lambda est: est["nota"] >= 90, estudiantes))
print(aprobados)

#=========================================================================================================

""" 19. Crea una función lambda que filtre los números impares de una lista dada."""

filtrar_impares = lambda lista: list(filter(lambda x: x % 2 != 0, lista))

print(filtrar_impares([1, 2, 3, 4, 5]))
# [1, 3, 5]

#=========================================================================================================

""" 20. Para una lista con elementos tipo integer y string obtén una nueva lista sólo con los valores int. Usa la función
filter()"""

def solo_enteros(lista):
    return list(filter(lambda x: isinstance(x, int), lista))

print(solo_enteros([1, "hola", 3, "7", 5]))
# [1, 3, 5]

#=========================================================================================================

""" 21. Crea una función que calcule el cubo de un número dado mediante una función lambda"""

cubo = lambda x: x ** 3    
print(cubo(3))  # Output: 27

#=========================================================================================================
""" 22. Dada una lista numérica, obtén el producto total de los valores de dicha lista.Usa la función reduce() ."""

lista_numerica = [2, 3, 4]

def reduce(lista):
    total_producto =   sum(lista)
    print(total_producto)  # Output: 9

reduce(lista_numerica)

#=========================================================================================================
""" 23. Concatena una lista de palabras.Usa la función reduce() ."""

lista_palabras = ["Hola", "amigo", "!"]

def reduce(lista):
    lista_concatenada =  " ".join(lista)
    print(lista_concatenada)  # Output: Hola amigo !

reduce(lista_palabras)

#=========================================================================================================
""" 24. Calcula la diferencia total en los valores de una lista. Usa la función reduce() ."""

valores = [10, 2, 3]

def reduce(lista):
  diferencia = sum(lista)/len(lista)
  print(diferencia)  # Output: 5

reduce(valores)

#=========================================================================================================
""" 25. Crea una función que cuente el número de caracteres en una cadena de texto dada."""

cadena_texto = "Hola, mundo!"

def contar_numero_caracteres(texto):
  longuitud_de_cadena = len(texto)
  print(longuitud_de_cadena)  # Output: 12

contar_numero_caracteres(cadena_texto)

#=========================================================================================================
""" 26. Crea una función lambda que calcule el resto de la división entre dos números dados."""

resto = lambda a, b: a % b
print(resto(10, 3))  # Output: 1

#=========================================================================================================
""" 27. Crea una función que calcule el promedio de una lista de números."""

lista_numerica = [15, 12, 3]

def reduce(lista):
  promedio = sum(lista)/len(lista)
  print(promedio)  # Output: 10

reduce(lista_numerica)
#=========================================================================================================
""" 28. Crea una función que busque y devuelva el primer elemento duplicado en una lista dada."""

def primer_duplicado(lista):
    vistos = set()
    for elemento in lista:
        if elemento in vistos:
            return elemento
        vistos.add(elemento)
    return None

print(primer_duplicado([1, 2, 3, 2, 4]))  # Output: 2


#=========================================================================================================
""" 29. Crea una función que convierta una variable en una cadena de texto y enmascare todos los caracteres con el
carácter '#', excepto los últimos cuatro."""

def enmascarar_variable(variable):
    # Convertir la variable a cadena
    cadena = str(variable)
    
    # Enmascarar todos los caracteres excepto los últimos cuatro
    if len(cadena) <= 4:
        return cadena  # No se enmascara si tiene 4 o menos caracteres
    
    return '#' * (len(cadena) - 4) + cadena[-4:]

# Ejemplo de uso:
print(enmascarar_variable(123456789))    # ######6789
print(enmascarar_variable("contraseña")) # #######seña

#=========================================================================================================
""" 30. Crea una función que determine si dos palabras son anagramas, es decir, si están formadas por las mismas letras
pero en diferente orden."""

def son_anagramas(palabra1, palabra2):
    # Eliminar espacios y convertir a minúsculas para comparación uniforme
    palabra1 = palabra1.replace(" ", "").lower()
    palabra2 = palabra2.replace(" ", "").lower()
    
    # Comparar las letras ordenadas de ambas palabras
    return sorted(palabra1) == sorted(palabra2)

# Ejemplo de uso:
print(son_anagramas("Roma", "Amor"))       # True
print(son_anagramas("Escucha", "Cuchase")) # True
print(son_anagramas("Hola", "Hulo"))       # False

#=========================================================================================================

""" 31.  Crea una función que solicite al usuario ingresar una lista de nombres y luego solicite un nombre para buscar en
esa lista. Si el nombre está en la lista, se imprime un mensaje indicando que fue encontrado, de lo contrario, se
lanza una excepción."""

def buscar_nombre():
    try:
        # Solicitar al usuario que ingrese una lista de nombres separados por comas
        entrada = input("Ingresa una lista de nombres separados por comas: ")
        nombres = [nombre.strip() for nombre in entrada.split(",") if nombre.strip()]
        
        # Solicitar el nombre a buscar
        nombre_a_buscar = input("Ingresa el nombre que deseas buscar: ").strip()
        
        # Buscar el nombre en la lista
        if nombre_a_buscar in nombres:
            print(f"El nombre '{nombre_a_buscar}' fue encontrado en la lista.")
        else:
            raise ValueError(f"El nombre '{nombre_a_buscar}' no está en la lista.")
    
    except ValueError as e:
        print("Excepción:", e)

buscar_nombre()
      
#=========================================================================================================

""" 32. Crea una función que tome un nombre completo y una lista de empleados, busque el nombre completo en la lista y
devuelve el puesto del empleado si está en la lista, de lo contrario, devuelve un mensaje indicando que la persona
no trabaja aquí."""

def buscar_puesto_empleado(nombre_completo, lista_empleados):
    """
    Busca el nombre completo en una lista de empleados y devuelve su puesto.
    
    Parámetros:
    - nombre_completo: str, nombre completo del empleado a buscar.
    - lista_empleados: list of tuples, donde cada tupla es (nombre, puesto).
    
    Retorna:
    - El puesto del empleado si está en la lista.
    - Un mensaje indicando que no trabaja aquí si no se encuentra.
    """
    for nombre, puesto in lista_empleados:
        if nombre.lower().strip() == nombre_completo.lower().strip():
            return f"{nombre} trabaja como {puesto}."
    
    return f"{nombre_completo} no trabaja aquí."

# Ejemplo de uso:
empleados = [
    ("María Rodríguez", "Gerente de Ventas"),
    ("Luis Gómez", "Analista de Datos"),
    ("Carla Méndez", "Diseñadora Gráfica")
]

# Pruebas:
print(buscar_puesto_empleado("Luis Gómez", empleados))         # Luis Gómez trabaja como Analista de Datos.
print(buscar_puesto_empleado("Ana López", empleados))          # Ana López no trabaja aquí.

#=========================================================================================================

""" 33. Crea una función lambda que sume elementos correspondientes de dos listas dadas"""

sumar_listas = lambda lista1, lista2: list(map(lambda x, y: x + y, lista1, lista2))

lista1 = [1, 2, 3]
lista2 = [4, 5, 6]

resultado = sumar_listas(lista1, lista2)
print(resultado)  # [5, 7, 9]

#=========================================================================================================

"""34. Crea la clase Arbol , define un árbol genérico con un tronco y ramas como atributos. Los métodos disponibles son:
crecer_tronco , nueva_rama , crecer_ramas , quitar_rama e info_arbol . El objetivo es implementar estos métodos para
manipular la estructura del árbol."""

class Arbol:
    def __init__(self):
        self.tronco = 1
        self.ramas = []

    def crecer_tronco(self):
        self.tronco += 1

    def nueva_rama(self):
        self.ramas.append(1)

    def crecer_ramas(self):
        self.ramas = [longitud + 1 for longitud in self.ramas]

    def quitar_rama(self, posicion):
        if 0 <= posicion < len(self.ramas):
            self.ramas.pop(posicion)
        else:
            print("Posición no válida. No se pudo quitar la rama.")

    def info_arbol(self):
        return {
            "longitud_tronco": self.tronco,
            "numero_ramas": len(self.ramas),
            "longitudes_ramas": self.ramas
        }

# --- Caso de uso ---

# 1. Crear un árbol.
mi_arbol = Arbol()

# 2. Hacer crecer el tronco del árbol una unidad.
mi_arbol.crecer_tronco()

# 3. Añadir una nueva rama al árbol.
mi_arbol.nueva_rama()

# 4. Hacer crecer todas las ramas del árbol una unidad.
mi_arbol.crecer_ramas()

# 5. Añadir dos nuevas ramas al árbol.
mi_arbol.nueva_rama()
mi_arbol.nueva_rama()

# 6. Retirar la rama situada en la posición 2.
mi_arbol.quitar_rama(2)

# 7. Obtener información sobre el árbol.
info = mi_arbol.info_arbol()
print("Información del árbol:")
print(f"Longitud del tronco: {info['longitud_tronco']}")
print(f"Número de ramas: {info['numero_ramas']}")
print(f"Longitudes de las ramas: {info['longitudes_ramas']}")

#=========================================================================================================

"""36. Crea la clase UsuarioBanco ,representa a un usuario de un banco con su nombre, saldo y si tiene o no cuenta
corriente. Proporciona métodos para realizar operaciones como retirar dinero, transferir dinero desde otro usuario y
agregar dinero al saldo."""

class UsuarioBanco:
    def __init__(self, nombre, saldo, cuenta_corriente):
        self.nombre = nombre
        self.saldo = saldo
        self.cuenta_corriente = cuenta_corriente

    def retirar_dinero(self, cantidad):
        if cantidad <= 0:
            raise ValueError("La cantidad a retirar debe ser mayor que cero.")
        if cantidad > self.saldo:
            raise ValueError(f"{self.nombre} no tiene saldo suficiente para retirar {cantidad} unidades.")
        self.saldo -= cantidad

    def transferir_dinero(self, otro_usuario, cantidad):
        if cantidad <= 0:
            raise ValueError("La cantidad a transferir debe ser mayor que cero.")
        if cantidad > otro_usuario.saldo:
            raise ValueError(f"{otro_usuario.nombre} no tiene saldo suficiente para transferir {cantidad} unidades.")
        otro_usuario.saldo -= cantidad
        self.saldo += cantidad

    def agregar_dinero(self, cantidad):
        if cantidad <= 0:
            raise ValueError("La cantidad a agregar debe ser mayor que cero.")
        self.saldo += cantidad

    def __str__(self):
        return f"{self.nombre} - Saldo: {self.saldo} - Cuenta Corriente: {self.cuenta_corriente}"

# --- Caso de uso ---

# 1. Crear dos usuarios: Alicia y Bob
alicia = UsuarioBanco("Alicia", 100, True)
bob = UsuarioBanco("Bob", 150, True)

# 2. Agregar 20 unidades de saldo a Bob
bob.agregar_dinero(20)

# 3. Hacer una transferencia de 80 unidades desde Bob a Alicia
alicia.transferir_dinero(bob, 80)

# 4. Retirar 50 unidades de saldo a Alicia
alicia.retirar_dinero(50)

# Mostrar información final
print(alicia)
print(bob)

#=========================================================================================================

"""37. Crea una función llamada procesar_texto que procesa un texto según la opción especificada: contar_palabras ,
reemplazar_palabras , eliminar_palabra . Estas opciones son otras funciones que tenemos que definir primero y llamar dentro
de la función procesar_texto ."""

from collections import Counter

# 1. Función para contar palabras
def contar_palabras(texto):
    palabras = texto.lower().split()
    return dict(Counter(palabras))

# 2. Función para reemplazar palabras
def reemplazar_palabras(texto, palabra_original, palabra_nueva):
    return texto.replace(palabra_original, palabra_nueva)

# 3. Función para eliminar palabras
def eliminar_palabra(texto, palabra_a_eliminar):
    palabras = texto.split()
    palabras_filtradas = [p for p in palabras if p != palabra_a_eliminar]
    return ' '.join(palabras_filtradas)

# 4. Función principal que procesa el texto
def procesar_texto(texto, opcion, *args):
    if opcion == "contar":
        return contar_palabras(texto)
    elif opcion == "reemplazar":
        if len(args) != 2:
            raise ValueError("Para 'reemplazar' se requieren dos argumentos: palabra_original y palabra_nueva.")
        return reemplazar_palabras(texto, args[0], args[1])
    elif opcion == "eliminar":
        if len(args) != 1:
            raise ValueError("Para 'eliminar' se requiere un solo argumento: palabra_a_eliminar.")
        return eliminar_palabra(texto, args[0])
    else:
        raise ValueError("Opción no válida. Usa: 'contar', 'reemplazar' o 'eliminar'.")
    
texto = "Hola mundo hola mundo Python es genial y Python es poderoso"

# Contar palabras
print("Contar palabras:")
print(procesar_texto(texto, "contar"))

# Reemplazar "Python" por "JavaScript"
print("\nReemplazar 'Python' por 'JavaScript':")
print(procesar_texto(texto, "reemplazar", "Python", "JavaScript"))

# Eliminar la palabra "mundo"
print("\nEliminar palabra 'mundo':")
print(procesar_texto(texto, "eliminar", "mundo"))
   
#=========================================================================================================

"""38. Genera un programa que nos diga si es de noche, de día o tarde según la hora proporcionada por el usuario."""

def determinar_momento_dia(hora):
    if 0 <= hora < 6:
        return "Es de noche."
    elif 6 <= hora < 12:
        return "Es de día (mañana)."
    elif 12 <= hora < 18:
        return "Es de tarde."
    elif 18 <= hora < 24:
        return "Es de noche."
    else:
        return "Hora no válida. Introduce una hora entre 0 y 23."

# Solicitar al usuario la hora
try:
    hora_usuario = int(input("Introduce la hora (0-23): "))
    resultado = determinar_momento_dia(hora_usuario)
    print(resultado)
except ValueError:
    print("Por favor, introduce un número entero válido.")

#=========================================================================================================

"""39. Escribe un programa que determine qué calificación en texto tiene un alumno en base a su calificación numérica.
Las reglas de calificación son:
 0  69 insuficiente
 70  79 bien
 80  89 muy bien
 90  100 excelente"""

def calificacion_en_texto(nota):
    if 0 <= nota <= 69:
        return "Insuficiente"
    elif 70 <= nota <= 79:
        return "Bien"
    elif 80 <= nota <= 89:
        return "Muy bien"
    elif 90 <= nota <= 100:
        return "Excelente"
    else:
        return "Nota no válida"

# Solicitar la nota al usuario
try:
    nota = int(input("Introduce la calificación numérica del alumno (0-100): "))
    resultado = calificacion_en_texto(nota)
    print(f"Calificación: {resultado}")
except ValueError:
    print("Por favor, introduce un número válido.")

#=========================================================================================================

"""40. Escribe una función que tome dos parámetros: figura (una cadena que puede ser "rectangulo" , "circulo" o
"triangulo" ) y datos (una tupla con los datos necesarios para calcular el área de la figura)."""

import math

def calcular_area(figura, datos):
    figura = figura.lower()
    
    if figura == "rectangulo":
        base, altura = datos
        return base * altura
    
    elif figura == "circulo":
        (radio,) = datos
        return math.pi * radio ** 2
    
    elif figura == "triangulo":
        base, altura = datos
        return (base * altura) / 2
    
    else:
        return "Figura no reconocida"

# Ejemplos de uso:
print("Área del rectángulo:", calcular_area("rectangulo", (5, 3)))   # 15
print("Área del círculo:", calcular_area("circulo", (4,)))           # ≈ 50.27
print("Área del triángulo:", calcular_area("triangulo", (6, 2)))     # 6.0

#=========================================================================================================

""" En este ejercicio, se te pedirá que escribas un programa en Python que utilice condicionales para determinar el
monto final de una compra en una tienda en línea, después de aplicar un descuento. El programa debe hacer lo
siguiente:
1. Solicita al usuario que ingrese el precio original de un artículo.
2. Pregunta al usuario si tiene un cupón de descuento (respuesta sí o no).
3. Si el usuario responde que sí, solicita que ingrese el valor del cupón de descuento.
4. Aplica el descuento al precio original del artículo, siempre y cuando el valor del cupón sea válido (es decir, mayor
a cero). Por ejemplo, descuento de 15€.
5. Muestra el precio final de la compra, teniendo en cuenta el descuento aplicado o sin él.
6. Recuerda utilizar estructuras de control de flujo como if, elif y else para llevar a cabo estas acciones en tu
programa de Python"""

def calcular_precio_final():
    try:
        precio_original = float(input("Introduce el precio original del artículo (€): "))
        
        tiene_cupon = input("¿Tienes un cupón de descuento? (sí o no): ").strip().lower()

        if tiene_cupon == "sí" or tiene_cupon == "si":
            valor_cupon = float(input("Introduce el valor del cupón de descuento (€): "))
            
            if valor_cupon > 0:
                precio_final = precio_original - valor_cupon
                if precio_final < 0:
                    precio_final = 0
                print(f"Descuento aplicado: {valor_cupon}€")
            else:
                print("Cupón no válido. No se aplica descuento.")
                precio_final = precio_original
        else:
            print("No se aplica descuento.")
            precio_final = precio_original

        print(f"Precio final de la compra: {precio_final:.2f}€")
    
    except ValueError:
        print("Entrada no válida. Por favor, introduce un número para el precio y el descuento.")

# Ejecutar el programa
calcular_precio_final()

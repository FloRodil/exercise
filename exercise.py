lista_personas = [
    ('11111111', 'Pedro', 'Paez', 24),
    ('22222222', 'Fito', 'Garcia', 23),
    ('33333333', 'Leo', 'Peralta', 26),
    ('44444444', 'Bruno', 'Mac', 25),
    ('55555555', 'Nico', 'Zaoral', 27),
    ('44444444', 'Bruno', 'Mac', 25),
]


def ordenar(lista_personas) -> list:
    """ El metodo debe devolver una lista con las edades ordenadas de menor a mayor"""
    edades = []
    for tupla in lista_personas:
        edades.append(tupla[3])
    return sorted(edades)


def convertir_a_diccionario(lista_personas) -> dict:
    """ Hacer un diccionario que tenga como claves los “dni” y como valores tuplas con nombre, apellido y edad """
    dicc = {}
    for tupla in lista_personas:
        dicc[tupla[0]] = tupla[1:]
    return dicc


def devolver_edad(lista_personas, dni) -> int:
    """ Para la 'lista_personas' devuelve la edad de la persona que tenga el dni definido.
    Tip: intentar usar el método convertir_a_diccionario"""
    dicc = convertir_a_diccionario(lista_personas)
    for clave,valor in dicc.items():
        if clave == dni:
            return valor[2]


def eliminar_repetidos(lista_personas) -> list:
    """ El metodo debe devolver los elementos unicos """
    sin_repetir=[lista_personas[0]]
    for i in range(1,len(lista_personas)):
        contador = 0
        for k in range(len(sin_repetir)):
            if lista_personas[i] != sin_repetir[k]:
                contador = contador + 1
        if contador == len(sin_repetir):
                sin_repetir.append(lista_personas[i])
    return sin_repetir


def separar_por_edad(lista_personas) -> tuple[list,list]:
    """ Devolver dos listas
    * lista 1: mayores de 25 (incluido)
    * lista 2: menores de 25
    """
    lista_1 = []
    lista_2 = []
    for tupla in lista_personas:
        if tupla[3] >= 25:
            lista_1.append(tupla)
        else:
            lista_2.append(tupla)
    return lista_1, lista_2


def obtener_promedio(lista) -> float:
    """ Implementar obtener el promedio de la lista de números que se recibe.
    Capturar con un try/except la excepción de dividir por cero"""
    suma = 0
    for n in lista:
        suma = suma + n
    try:
        promedio = suma/len(lista)
        return promedio
    except ZeroDivisionError:
        return 'La lista está vacía. No es posible dividir por cero.'


def main():
    """ Este metodo no debe modificarse y es solo a fines de probar el codigo """
    print('Resultados:\n')
    print(' * Edades ordenadas: %s\n' % ordenar(lista_personas))
    print(' * Elementos como diccionario: %s\n' % convertir_a_diccionario(lista_personas))
    print(' * La edad para dni 55555555 es: %s\n' % devolver_edad(lista_personas, '55555555'))
    print(' * Elementos únicos: %s\n' % eliminar_repetidos(lista_personas))
    print(' * Los mayores de 25 son: %s\n' % separar_por_edad(lista_personas)[0])
    print(' * Los menores de 25 son: %s\n' % separar_por_edad(lista_personas)[1])
    print(' * El promedio de las edades es: %s\n' % obtener_promedio(ordenar(lista_personas)))
    print(' * El promedio de una lista vacía es: %s\n' % obtener_promedio([]))


main()
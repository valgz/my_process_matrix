from functools import reduce

def process_list(elements):

    """
    Recibe una lista de numeros y devuelve una nueva, con los elementos cambiados.
    Cada elemento de la nueva, será el promedio del valor antiguo y el de sus vecinos
    """

    processed_list = []

    if len(elements) == 1:
        processed_list = elements
    else:
        for index, element in enumerate(elements):
            new_element = process_element(index, elements)
            processed_list.append(new_element)

    return processed_list



def process_element(index, elements):
    
    """
    Recibe el indice de un elemento y la lista en la que está y 
    calcula su promedio con sus vecinos y devuelve dicho promedio.
    """

    indices = get_neighbour_indices(index, elements)
    values = get_neighbour_values(indices, elements)
    average = get_average(values)

    return average



def get_neighbour_indices(index, elements):

    """
    Recibe el indice de un elemento y la lista en la que está,
    Devuelve la lista de indices de los vecinos, incluyendo al propio elemento
    """

    indices = []

    indices.append(index - 1)   #agregamos el vecino de la izquierda
    indices.append(index)       #agregamos el indice del propio elemento
    indices.append(index + 1)   #agregamos el vecino de la derecha
    
    #filter para eliminar indices imposibles
    correct_indices = list(filter(lambda i: 0 < i < len(elements), indices))

    return correct_indices



def get_neighbour_values(indices, elements):

    values = []
    for index in indices:
        values.append(elements[index])
    return values



def get_average(values):

    return round((reduce(lambda accum, actual: accum + actual, values, 0) / len(values)), 2)


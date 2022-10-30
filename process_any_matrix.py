
from functools import reduce


'''
Para resolver este ejercicio me base en las funciones de process_list
Mi función process_matrix está al final de este fichero :)
'''


def possible_indices(indices, matrix):

    '''
    Recibe una lista de coordenadas y una matriz
    Devuelve una nueva lista con los indices posibles
    '''

    return list(filter(lambda coord: 0 <= coord[0] < len(matrix) and 0 <= coord[1] < len(matrix[0]), indices))



def get_neighbour_indices(i, j, matrix):

    '''
    Recibe los dos indices del elemento a procesar: el indice de la columna (i),
    el indice de los elementos de cada columna (j), y la matriz. 
    Devuelve una lista de tuplas, que representa los indices de los vecinos del elemento 
    que esta siendo procesado.
    '''

    indices = []

    indices.append((i, j - 1))      #vecino arriba
    indices.append((i - 1, j))      #vecino izquierdo
    indices.append((i, j))          #propio elemento
    indices.append((i, j + 1))      #vecino abajo
    indices.append((i + 1, j))      #vecino derecho

    return possible_indices(indices, matrix)



def get_neighbour_values(indices, matrix):

    ''''
    Recibe una listas de coordenadas de vecinos incluyendo al propio elemento y una matriz 
    Devuelve la lista de valores correspondientes a los vecinos y al propio elemento
    '''

    return list(map(lambda coord: matrix[coord[0]][coord[1]], indices))



def get_average(values):

    '''
    Recibe una lista de valores y devuelve su promedio
    '''

    return round((reduce(lambda accum, actual: accum + actual, values, 0) / len(values)), 2)



def process_element(i, j, matrix):

    '''
    Recibe los dos indices del elemento a procesar: el indice de la lista de listas (i) y 
    el indice de la sublista (j), y la matriz
    Devuelve el promedio de los valores del propio elemento y sus vecinos'''
    
    indices = get_neighbour_indices(i, j, matrix)
    values = get_neighbour_values(indices, matrix)
    average = get_average(values)

    return average



def is_valid_matrix(matrix):

    '''
    Recibe una matriz y devuelve True en caso de que se cumplan tres condiciones:
    que la matriz este compuesta por una lista de listas, las sublistas son todas del mismo tamaño 
    y que el contenido de las sublistas son solo numeros.
    '''

    condition1 = True
    condition2 = True
    condition3 = True

    for sub in matrix:
        condition1 = condition1 and (type(sub) == list)
    
        length = len(matrix[0])

        if condition1:
            condition2 = condition2 and (length == len(sub))
        else:
            break

        if condition2:
            for element in sub:
                condition3 = condition3 and (type(element) == int or type(element) == float)
        else:
            break

        if not condition3:
            break
            
    return condition1 and condition2 and condition3



def process_matrix(matrix):

    '''
    Recibe una matriz y devuelve otra matriz cuyos valores son el promedio
    del propio elemento y sus vecinos
    '''

    if is_valid_matrix(matrix):
        
        submatrix = []
        processed_matrix = []

        for i, column in enumerate(matrix):
            for j, value in enumerate(column):
                new_value = process_element(i, j, matrix)
                submatrix.append(new_value)
            processed_matrix.append(submatrix)
            submatrix = []

        return processed_matrix

    else:
        raise ValueError('Only works on numerical matrices')


import numpy as np

naves = [
    [' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' '],
]
 
def tablero_naves(naves):
    num_fila = 1
    for fila in naves:
        print(num_fila, fila)
        num_fila = num_fila + 1
print(['  1', '2', '3', '4', '5'])
for n in range(5):
    num_fila = np.random.choice(5,5,replace=False)
    num_col = np.random.choice(5,5,replace=False)
    naves[num_fila[n]][num_col[n]] = 'X'
print("\n"*50)
disparos = [
    [' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' '],
]
print("Comienzan los disparos!!")
def ubica_disparo():
    columna = input("Ingrese columna (1 a 5): ")
    while columna not in "12345":
        print("Columna equivocada! ")
        columna = input("Ingrese columna (1 a 5): ")

    fila = input("Ingrese fila (1 a 5): ")
    while fila not in "12345":
        print("Fila equivocada!")
        fila = input("Ingrese fila (1 a 5):")

    return int(fila) - 1, int(columna) - 1
num_disparos = 0
naves_hundidas = 0
while num_disparos < 20 and naves_hundidas < 5:
    print("Ubique un disparo")
    num_fila, num_col = ubica_disparo()

    if naves[num_fila][num_col] == 'X':
        print("Hundido!")
        disparos[num_fila][num_col] = '\U0001F923'
        num_disparos = num_disparos + 1
        naves_hundidas = naves_hundidas + 1
    else:
        disparos[num_fila][num_col] = '\U0001F612'
        print("Agua!")
        num_disparos = num_disparos + 1

    tablero_naves(disparos)
    print("Terminado!")
    


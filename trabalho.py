#Natália Sens Weise e Matheus Petters Bevilaqua
import random
limite = 10
memoria = [[], [], [], [], []]
contador = 0
ocupados = []

#sorteia um index
#só dá pra usar o valor 4 se for o primeiro, o 5 n vai, por conta do loop, é difícil dar certo
def sorting_index():
    global tam 
    i = random.randrange(0, 5) - tam
    while i < 0:
        i = (random.randrange(0, 5)) - tam
    return i

#verifica se tem algo na memória
def is_full():
    global tamanho
    tamanho = 0
    for processo in memoria:
        tamanho+=len(processo)
    return tamanho==10

#coloca na memoria o processo em uma posição livre
def put_in_memory():
    global contador
    temp = []
    for _ in range(tam):
        temp.append(1)
    index = sorting_index()

    while ocupados.__contains__(index):
        index = sorting_index()
    memoria[index] = temp
    ocupados.append(index)
    contador+=1

#espera pelo tamanho do processo e daí põe na memória 
def ask_for_process():
    global contador
    global tam
    tam = int(input('Espaço que deseja ocupar: '))

    while tamanho + tam > limite:
        tam = int(input('não há espaço suficiente, tente um espaço menor....'))
    if not is_full():
        # a ideia aqui era remover um processo de vez e qnd da memória, mas tem algo errado
        # queria substituir os espaços com arrays de 0, pra daí qnd tiver arrays consecutivos de 0, juntar
        # n sei se to viajando KKKKKKKKKK help
        # if tamanho > 0 and contador > 0 and (contador%2 == 0):
        #     temp = []
        #     for _ in range(tam):
        #         temp.append(0)
        #     index = sorting_index()
        #     while not ocupados.__contains__(index):
        #         index = sorting_index()
        #     memoria[index] = temp
        #     ocupados.remove(index)
        #     contador+=1
        put_in_memory()
                    
while not is_full():
    print(memoria)
    ask_for_process()
print(memoria)
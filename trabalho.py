#Natália Sens Weise e Matheus Petters Bevilaqua
import random
limite = 10
memoria = []
tamanho = 0

#sorteia um index
def sorting_index():
    i = random.randrange(0, len(memoria))
    while i < 0:
        i = (random.randrange(0, len(memoria)))
    return i

#verifica se tem algo na memória
def is_full():
    global tamanho
    tamanho = 0
    for processo in memoria:
        if processo.__contains__(1):
            tamanho+=len(processo)
    return tamanho==10

#coloca na memoria o processo em uma posição livre
def put_in_memory():
    if len(memoria) == 2 and memoria[0].__contains__(0):
        memoria.pop(0)
    temp = []
    for _ in range(tam):
        temp.append(1)
    memoria.append(temp)

#remove o processo, e coloca vários 0 no lugar
def remove_in_memory():
    index = sorting_index()
    print(index)
    while not memoria[index].__contains__(1):
        index = sorting_index()
    taman = len(memoria[index])
    temp = []
    for _ in range(taman):
        temp.append(0)
    memoria[index] = temp

#essa função é pra verificar se tem algum array de 0 consecutivo pra unir eles, e se tiver unir
def verify_free_space():
    temp = []
    for index in range(len(memoria)):
        if memoria[index].__contains__(0):
            if index != len(memoria) - 1:
                if memoria[index+1].__contains__(0):
                    for i in memoria[index]:
                        temp.append(i)
                    for i in memoria[index+1]:
                        temp.append(i)
                    memoria[index] = temp
                    memoria.pop(index+1)
                    break
            else:
                if memoria[index-1].__contains__(0):
                    for i in memoria[index]:
                        temp.append(i)
                    for i in memoria[index-1]:
                        temp.append(i)
                    memoria[index] = temp
                    memoria.pop(index-1)
                    break

#espera pelo tamanho do processo e daí põe na memória 
def ask_for_process():
    global tam
    tam = int(input('Espaço que deseja ocupar: '))

    while (((tamanho + tam ) > limite) and (not is_full())):
        remove_in_memory()
        verify_free_space()

    if not is_full():
        put_in_memory()
        if is_full():
            remove_in_memory()
    verify_free_space()
                    
while True:
    print(memoria)
    ask_for_process()

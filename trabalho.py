#Natália Sens Weise e Matheus Petters Bevilaqua
import random
limite = 10
memoria = [[], [], [], [], []]
contador = 0
ocupados = []
tamanho = 0

#sorteia um index
def sorting_index():
    global tam 
    i = random.randrange(0, 5)
    while i < 0:
        i = (random.randrange(0, 5))
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

#remove o processo, e coloca vários 0 no lugar
def remove_in_memory():
    index = sorting_index()

    while not ocupados.__contains__(index):
        index = sorting_index()
    t = len(memoria[index])
    temp = []
    for _ in range(t):
        temp.append(0)

    memoria[index] = temp
    ocupados.append(index)

#essa função é pra verificar se tem algum array de 0 consecutivo pra unir eles
def verify_free_space():
    temp = []
    for index in range(len(memoria)):
        if memoria[index].__contains__(0):
            if index < len(memoria) - 1:
                if memoria[index+1].__contains__(0):
                    for i in memoria[index]:
                        temp.append(i)
                    for i in memoria[index+1]:
                        temp.append(i)
                    print(memoria)
                    memoria.pop(index)
                    memoria[index+1] = temp
                    break
            else:
                if memoria[index-1].__contains__(0):
                    for i in memoria[index]:
                        temp.append(i)
                    for i in memoria[index+1]:
                        temp.append(i)
                    print(memoria)
                    memoria.pop(index)
                    memoria[index+1] = temp
                    break

#espera pelo tamanho do processo e daí põe na memória 
def ask_for_process():
    global contador
    global tam
    tam = int(input('Espaço que deseja ocupar: '))

    while (((tamanho + tam ) > limite) and (not is_full())):
        tam = int(input('não há espaço suficiente, tente um espaço menor....'))
    if not is_full():
        put_in_memory()
        if is_full():
            remove_in_memory()
    verify_free_space()
                    
while True:
    print(memoria)
    ask_for_process()
print(memoria)
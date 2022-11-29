#Natália Sens Weise e Matheus Petters Bevilaqua
import random

memory_space = 10
memory = []
while memory_space != 0:
    memory.append(0)
    memory_space-=1

memory_limit = 20

def show_memory():
    print(memory)

def waiting_process():
    show_memory()
    global tam 
    tam = int(input("Tamanho que deseja alocar: "))
    if check_space():
        alocatte_memory()
    else:
        print("Não espaço na memória no momento, aguarde...")

def check_space():
    space = 0
    for i in memory:
        if i == 0:
            space+=1
    return space > 0

def sorting_index():
    global tam 
    i = random.randrange(0, 10) - tam
    while i < 0:
        i = (random.randrange(0, 10)) - tam
    return i

def select_positions(i):
    c = 0
    positions = []
    t = tam
    while t != 0:
        positions.append(i+c)
        c+=1
        t-=1
    return positions

def alocatte_memory():
    global tam 
    temp = tam
    i = sorting_index()
    while memory[i] == 1:
        i = sorting_index()
    positions = select_positions(i)

    for index in positions:
        if memory[index] != 0:
            print(index)
            alocatte_memory()

    teste = []
    while temp > 0:
        teste.append(1)
        temp-=1
        
    for index in positions:
        memory[index] = teste
        break

    waiting_process()
    

if __name__ == '__main__':
    waiting_process()
    show_memory()
# memory-simulator
Projeto desenvolvido para a disciplina de Sistemas Operacionais. 
Consiste em um simulador de alocação de memória particionada dinâmica.

## O que preciso para executá-lo?

  * Primeiro você precisa instalar:
    * a versão mais recente e usual do [Python](https://www.python.org/downloads/);
    * um editor de código (ex: [VSCode](https://code.visualstudio.com/));
    * e, dentro do VSCode, instalar a extensão do Python no editor.
  
  * Após isso, basta executar o programa escrevendo no terminal da pasta `python trabalho.py` e seguir as instruções que aparecerem na tela.

## Como funciona?

  O sistema mostrará a memória (que está vazia) e pedirá o tamanho do processo que vai entrar.
  Caso o processo seja maior que o limite (10) ou menor que 1 irá solicitar um outro valor ao usuário.
  Quando tiver obtido um valor compatível, irá adicionar na memória como listas de 1s (simulação da fragmentação). 
  * Ex: `[[1, 1, 1, 1], [1, 1]]`
  
  Quando a memória estiver cheia, ele vai começar a remover processos qleatoriamente, colocando uma lista de 0s no lugar. 
  * Ex:`[[0, 0, 0, 0], [1, 1], [1, 1, 1], [1]]`
  
  Quando listas de 0s estiverem seguidas uma da outra, irá uní-las (simulação da solução para fragmentação em memória particionada dinâmica). 
  * Ex: `[[0, 0, 0, 0], [0, 0], [1, 1, 1], [1], [1, 1, 1, 1, 1]]`, `[[0, 0, 0, 0, 0, 0], [1, 1, 1], [1], [1, 1, 1, 1, 1]]`
  
  Quando tiver na lista apenas uma área vazia e um processo, ele libera pra área vazia (lista de 0s) ser ocupada.
  * Ex: `[[0, 0, 0, 0, 0, 0], [1, 1, 1]]`, `[[1], [1, 1, 1]]`
  
  Para encerrar, basta dar CTRL + X.

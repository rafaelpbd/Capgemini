# Escreva um algoritmo que mostre na tela uma escada de tamanho n utilizando o caractere *
# e espaços. A base e altura da escada devem ser iguais ao valor de n. A última linha não deve conter
# nenhum espaço.

# A variavel estrelas recebe o numero de linhas com estrelas que o
#  usuario deseja formar.

estrelas = int(input("Digite o numeros de linhas: "))

# variavel i é inicializada antes da sua utilização na estrutura de repetição while

i = 1

''' estrutura de repetição while, ela que efetivamente irá criar a 
escada de estrelas conforme pedido no exercicio. Enquanto a variavel
 i for menor ou igual ao numero de linhas com estrelas digitados pelo
 usuário, esse loop se repetirá. Em cada volta do loop, a escada é
  formada "imprimindo" na tela o caractere espaço vazio multiplicado
   pelo número contido na variavel estrelas subtraindo-se o valor na 
   variavel i, faz-se em seguida a concatenação com o caractere * 
   multiplicado pelo valor contido na variavel i. Como em cada volta 
   do loop while, o número da variavel i é alterado, o número de 
   caracteres "espaços vazios" diminui e o número de caracteres "*" 
   aumenta, formando assim, uma escada de estrelas.
'''

while(i <= estrelas):
    print(" " * (estrelas - i) + (i * "*"))
    i = i + 1


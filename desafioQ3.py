'''
Duas palavras podem ser consideradas anagramas de si mesmas se as letras de uma palavra
podem ser realocadas para formar a outra palavra. Dada uma string qualquer, desenvolva um
algoritmo que encontre o número de pares de substrings que são anagramas.
Exemplo:
Exemplo 1)
Entrada:
ovo
Saída:
3
Explicação:
A lista de todos os anagramas pares são: [o, o], [ov, vo] que estão nas posições [[0, 2], [0, 1],
[1, 2]] respectivamente.

Exemplo 2)
Entrada: ifailuhkqq
Saída: 3

Explicação:
A lista de todos os anagramas pares são: [i, i], [q, q] e [ifa, fai] que estão nas posições [[0, 3]],
[[8, 9]] e [[0, 1, 2], [1, 2, 3]].
'''

'''
    Observação em relação a resposta da questão 03.

Infelizmente não fui capaz de compreender completamente o que foi pedido na questão 03. Por exemplo, a questão apresenta, no exemplo 2, a string "ifailuhkqq" como entrada e o número inteiro 3 como saída. Nesse exemplo é explicado que as substrings [ifa, fai](que não são consideradas palavras reais) seriam consideradas anagramas, porém, não consegui entender porque as substrings  [failu, luifa] ou [lui, ilu]... etc... não poderia formar um novo anagrama. Qual o critério que determinou que as substrings aleatórias [ifa, fai] são válidas mas as demais não são?
Nessa situação, fiz um algoritmo que verifica se duas strings digitadas pelo usuário são anagramas entre si. Provavelmente, não era o que foi solicitado, mas foi o mais próximo que cheguei com o que consegui compreender da questão.
'''

'''
Cria a função verificaAnagrama, nessa função, que recebe dois parâmetros (as duas palavras que se quer verificar se são anagramas ou não) é utilizada uma função embutida do python, chamada sorted, essa função coloca a string digitada em ordem alfabetica. Para verificar se as palavras digitadas são anagramas ou não, é feita a comparação entre as duas palavras em ordem alfabetica e caso elas sejam iguais, são anagramas, caso contrário, não são. 
'''

def verificaAnagrama(p1, p2): 
      
    
    if(sorted(p1) == sorted(p2)): 
        print("As palavras {} e {} são anagramas.".format(p1, p2))  
    else: 
        print("As palavras {} e {} não são anagramas.".format(p1, p2))         

# Variáveis palavra1 e palavra2 recebem as palavras que o usuário deseja saber se são anagramas entre si.

palavra1 = input("Digite a primeira palavra: ")
palavra2 = input("Digite a segunda palavra: ")          

# Faz a chamada da função verificaAnagrama

verificaAnagrama(palavra1, palavra2) 


'''
Débora se inscreveu em uma rede social para se manter em contato com seus amigos. A
página de cadastro exigia o preenchimento dos campos de nome e senha, porém a senha precisa ser
forte. O site considera uma senha forte quando ela satisfaz os seguintes critérios:

Possui no mínimo 6 caracteres.
Contém no mínimo 1 digito.
Contém no mínimo 1 letra em minúsculo.
Contém no mínimo 1 letra em maiúsculo.
Contém no mínimo 1 caractere especial. Os caracteres especiais são: !@#$%^&*()-+Débora digitou uma string aleatória no campo de senha, porém ela não tem certeza se é uma
senha forte. Para ajudar Débora, construa um algoritmo que informe qual é o número mínimo de
caracteres que devem ser adicionados para uma string qualquer ser considerada segura.
'''

# A variável senha recebe a senha informada pelo usuário.

senha = input("Digite a sua senha: ")

# A estrutura condicional if verifica o tamanho (quantos caracteres ela possui) da senha digitada pelo usuário, caso possua menos que 6 caracteres, ela informa, quantos ainda faltam para completar o valor mínimo de 6.

if((len(senha)) < 6):
    print(6 - (len(senha)))

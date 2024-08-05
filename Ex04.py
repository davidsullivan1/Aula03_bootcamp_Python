### Exercício 4: Validação de Dados de Entrada
# Antes de processar os dados de usuários em um sistema de recomendação, 
# você precisa garantir que cada usuário tenha idade entre 18 e 65 anos e tenha 
# fornecido um email válido. Escreva um programa que valide essas condições 
# e imprima "Dados de usuário válidos" ou o erro específico encontrado.

import re



def checkEmail(email):
    if re.fullmatch(regex, email):
        print("Valid Email")
    else:
        print("Invalid Email")

idade = 18; 
email = 'suporte@email.com'

regex = re.compile(r'^[\w-]+@(?:[a-zA-Z0-9-]+\.)+[a-zA-Z]{2,}$')







if idade < 18:
    print("Usuário tem idade inferior a 18 anos")
elif idade > 65:
    print("Usuário tem idade maior que 65 anos")
elif checkEmail(email) == "Invalid Email":
    print("Email informado para o usuário inválido")
else:
    print("Dados de Usuário Válidos")



    
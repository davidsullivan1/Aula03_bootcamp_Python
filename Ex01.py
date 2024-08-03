### Exercício 1: Verificação de Qualidade de Dados
# Você está analisando um conjunto de dados de vendas e precisa garantir 
# que todos os registros tenham valores positivos para `quantidade` e `preço`. 
# Escreva um programa que verifique esses campos e imprima "Dados válidos" se ambos 
# forem positivos ou "Dados inválidos" caso contrário.


quantidade = int(input("Digite a quantidade de um produto: "))
preco = float(input("Digite o Preço do Produto: "))


if(quantidade < 0 or preco < 0):
    print("Dados Inválidos, quantidade e preço do produto precisam ser maior do que zero")
else:
    print(f"Você informou {quantidade} com R${preco:_.2f}")

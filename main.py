from datetime import datetime

nome = input("Digite seu nome: ")
cidade = input("Digite sua cidade: ")

ano_nascimento = int(input("Digite seu ano de nascimento: "))

ano_atual = datetime.now().year
idade = ano_atual - ano_nascimento

print(f"\nOlá {nome} de {cidade}")
print(f"Você tem {idade} anos")

if idade < 18:
    print("Você é menor de idade")
else:
    print("Você é maior de idade")
from datetime import datetime


def obter_idade():
    ano_atual = datetime.now().year

    while True:
        try:
            ano_nascimento = int(input("Digite seu ano de nascimento: "))
            idade = ano_atual - ano_nascimento

            if idade < 0 or idade > 120:
                print("Ano inválido! Tente novamente.")
                continue

            return idade

        except ValueError:
            print("Digite um número válido!")


def classificar_idade(idade):
    if idade < 18:
        return "menor de idade"
    elif idade < 60:
        return "maior de idade"
    else:
        return "idoso"


while True:
    print("\n=== MENU ===")
    print("1 - Informar dados")
    print("2 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        nome = input("Digite seu nome: ")
        cidade = input("Digite sua cidade: ")

        idade = obter_idade()
        categoria = classificar_idade(idade)

        print(f"\nOlá {nome} de {cidade}")
        print(f"Você tem {idade} anos")
        print(f"Você é {categoria}")

    elif opcao == "2":
        print("Programa encerrado.")
        break

    else:
        print("Opção inválida. Tente novamente.")
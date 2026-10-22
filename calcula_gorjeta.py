def pergunta_preco():
    while True:
        try:
            preco = float(input("Insira o preço total: "))
        except ValueError:
            print("Insira apenas um número real")
            continue
        break
    return preco


def pergunta_porcentagem():
    while True:
        try:
            porcentagem = float(input("Insira a porcentagem da gorjeta: "))
        except ValueError:
            print("Insira apenas um número real")
            continue
        break
    return porcentagem


def pergunta_pessoas():
    while True:
        try:
            pessoas = int(input("Insira a quantidade de pessoas em que a conta será dividida: "))
        except ValueError:
            print("Insira apenas um número inteiro de pessoas")
            continue
        if pessoas > 0:
            break
        print("Insira ao menos um pessoa...")
    return pessoas


def calcular(preco, porcentagem, pessoas):
    gorjeta = preco * porcentagem / 100
    preco_total = preco + gorjeta
    preco_individual = preco_total / pessoas
    return preco_total, gorjeta, preco_individual


def resultado(preco_total, gorjeta, preco_individual):
    print(f"Preço Total: {preco_total:.2f} "
          f"\nGorjeta : {gorjeta:.2f} "
          f"\nPreço por pessoa: {preco_individual:.2f} ")


def main():
    while True:
        preco = pergunta_preco()
        porcentagem = pergunta_porcentagem()
        pessoas = pergunta_pessoas()
        preco_total, gorjeta, preco_individual = calcular(preco, porcentagem, pessoas)
        resultado(preco_total, gorjeta, preco_individual)
        perguntinha = input("Gostaria de fazer mais alguma conta? (s/n): ")
        if perguntinha == "n":
            print("Obrigado! Tenha um ótimo dia")
            break


if __name__ == "__main__":
    main()

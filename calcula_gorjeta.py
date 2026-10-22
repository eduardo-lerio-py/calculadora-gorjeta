def pergunta_numero(mensagem, tipo=float, minimo=0):
    while True:
        try:
            valor = tipo(input(mensagem).replace(",", "."))
        except ValueError:
            print("Insira apenas um número real!")
            continue
        if valor >= minimo:
            break
        print(f"Valor incorreto! Insira um número maior ou igual a {minimo}")
    return valor


def calcular(preco, porcentagem, pessoas):
    gorjeta = preco * porcentagem / 100
    preco_total = preco + gorjeta
    preco_individual = preco_total / pessoas
    return preco_total, gorjeta, preco_individual


def resultado(preco_total, gorjeta, preco_individual):
    print(f"Preço Total: {preco_total:.2f} "
          f"\nGorjeta: {gorjeta:.2f} "
          f"\nPreço por pessoa: {preco_individual:.2f} ")


def main():
    while True:
        preco = pergunta_numero("Insira o preço total: ")
        porcentagem = pergunta_numero("Insira a porcentagem da gorjeta: ")
        pessoas = pergunta_numero("Insira a quantidade de pessoas em que a conta será dividida: ", int, 1)

        preco_total, gorjeta, preco_individual = calcular(preco, porcentagem, pessoas)
        resultado(preco_total, gorjeta, preco_individual)

        perguntinha = input("Gostaria de fazer mais alguma conta? (s/n): ")
        if perguntinha.lower().strip() == "n":
            print("Obrigado! Tenha um ótimo dia")
            break


if __name__ == "__main__":
    main()

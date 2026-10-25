class Conta:
    def __init__(self, preco, porcentagem, pessoas):
        self.preco = preco
        self.porcentagem = porcentagem
        self.pessoas = pessoas

    def gorjeta(self):
        return self.preco * self.porcentagem / 100

    def preco_total(self):
        return self.preco + self.gorjeta()

    def preco_individual(self):
        return self.preco_total() / self.pessoas


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


def resultado(conta):
    print(f"Preço Total: {conta.preco_total():.2f} "
          f"\nGorjeta: {conta.gorjeta():.2f} "
          f"\nPreço por pessoa: {conta.preco_individual():.2f} ")


def main():
    while True:
        preco = pergunta_numero("Insira o preço total: ")
        porcentagem = pergunta_numero("Insira a porcentagem da gorjeta: ")
        pessoas = pergunta_numero("Insira a quantidade de pessoas em que a conta será dividida: ", int, 1)

        conta = Conta(preco, porcentagem, pessoas)
        resultado(conta)

        perguntinha = input("Gostaria de fazer mais alguma conta? (s/n): ")
        if perguntinha.lower().strip() == "n":
            print("Obrigado! Tenha um ótimo dia")
            break


if __name__ == "__main__":
    main()

import random
import string

def gerar_senha(tamanho: int):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    senha = "".join(random.choice(caracteres) for _ in range(tamanho))
    return senha


def main():
    try:
        tamanho = int(input("Digite o tamanho da senha: "))

        if tamanho <= 0:
            print("O tamanho deve ser maior que zero.")
            return

        senha = gerar_senha(tamanho)

        print(f"Senha gerada: {senha}")

    except ValueError:
        print("Digite um número válido.")


if __name__ == "__main__":
    main()
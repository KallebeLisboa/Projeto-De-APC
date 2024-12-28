# Configuração para seguir e voltar nas informações
def informacoes_sabao():
    def fluxo(count):
        while True:
            seguir = input().strip()
        # Verifica se a entrada contém apenas números
            if not seguir.isdigit():
                print("Digite um valor válido: apenas números inteiros de 1 a 2 são permitidos.")
                continue

        # Converte a entrada para número inteiro
            seguir = int(seguir)

        # Verifica se o número está no intervalo permitido
            if seguir < 1 or seguir > 2:
                print("Digite um número válido dentro do intervalo (1 a 2).")
                continue

    # Se for válido, sai do loop
            break
        if seguir == 2:
            count += 1
        if seguir == 1:
            count -= 1
        return count

    count = 1
    print("Pressione 1 para voltar e 2 para prosseguir: ")
    
    # Informações
    print("-=" * 15)
    print("Informações: ")

    while True:
        if count == 1:
            print("Você gosta de fritura?")
            print("Pois é, elas são feitas com óleo de cozinha. E o que as pessoas fazem com o óleo que sobra na panela?")
            count = fluxo(count)
        elif count == 2:
            print("Por não se misturar com a água, a presença de óleo nos rios cria uma barreira que dificulta a entrada de luz e a oxigenação da água,")
            print("comprometendo assim, a base da cadeia alimentar aquática e contribuindo para a ocorrência de enchentes e aquecimento do planeta (Revista Planeta Cidade, 2007).")
            count = fluxo(count)
        elif count == 3:
            print("Para evitar que o óleo de cozinha usado seja lançado na rede de esgoto,")
            print("diversas são as possibilidades de reciclagem do óleo de fritura.")
            count = fluxo(count)
        else:
            print("Você chegou ao final das informações. Obrigado!")
            break

# Protegendo a execução automática com if __name__ == "__main__"
if __name__ == "__main__":
    informacoes_sabao()

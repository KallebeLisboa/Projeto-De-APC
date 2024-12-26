
# Configuração para seguir e voltar nas informações
def fluxo(count):
    while True:
        seguir = input().strip()
        if any(char.isalpha() for char in seguir):
            print("Digite um valor válido sem letras")
            continue
        if " " in seguir:
            print("Digite um valor válido sem espaços")
            continue
        seguir = float(seguir)
        if seguir != 2 and seguir != 1:
            print("Digite 1 para voltar e 2 para seguir")
            continue
        break
    if seguir == 2:
        count += 1
    if seguir == 1:
        count -= 1
    return count

count = 1
print("Precione 1 para voltar e 2 para prosseguir: ")
fluxo(count)

# Informações

print("-="*15)
print("Informações: ")

while True:
    if count == 1:
        print("Você gosta de fritura? ")
        print("Pois é, elas são feitas com óleo de cozinha. E o que as pessoas fazem com o óleo que sobra na panela?")
        count = fluxo(count)
    if count == 2:
        print("Por não se misturar com a água, a presença de óleo nos rios cria uma barreira que dificulta a entrada de luz e a oxigenação da água,")
        print("comprometendo assim, a base da cadeia alimentar aquática e contribui para a ocorrência de enchentes e aquecimento do planeta (Revista Planeta Cidade, 2007).")
        count = fluxo(count)
        continue
    if count == 3:
        print("Para evitar que o óleo de cozinha usado seja lançado na rede de esgoto,")
        print("versas são as possibilidades de reciclagem do óleo de fritura.")
        count = fluxo(count)
        continue

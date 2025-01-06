# Conversor: Perguntar quantidade de óleo e já adaptar a quantidade dos materiais

#1000 mL de óleo // 100 mL de água // 100g de soda cáustica // 5 mL álcool (duas tampinhas)

def conversao():
    oleo_padrao = 1000.00
    agua_padrao = 100.00
    soda_padrao = 100.00
    alcool_padrao = 5.00

    #Verificação de número válido  
    while True:
        oleo = input("Quantos mLs de óleo serão usados: ").strip()
        print("=-"*15)
        # Verifica se a entrada contém apenas números
        if not oleo.isdigit():
            print("Digite um valor válido: apenas números inteiros são permitidos.")
            continue

    # Converte a entrada para número inteiro
        oleo = float(oleo)

    # Verifica se o número está no intervalo permitido
        if oleo < 0:
            print("Digite um número válido maior que 0: ")
            continue

    # Se for válido, sai do loop
        break

    #Cáuculo de água
    agua = ((oleo*agua_padrao)/oleo_padrao)

    #Cáuculo de soda
    soda = ((oleo*soda_padrao)/oleo_padrao)

    #Cáuculo de álcool
    alcool = ((oleo*alcool_padrao)/oleo_padrao)
    print("-"*15)
    print(f"A quantidade de óleo é \033[1;32m{oleo:.2f} mLs\033[m")
    print(f"A quantidade de água é \033[1;32m{agua:.2f} mLs\033[m")
    print(f"A quantidade de soda cáustica é \033[1;32m{soda:.2f}g\033[m")
    print(f"A quantidade de álcool é \033[1;32m{alcool:.2f} mLs\033[m")
    print("-"*15)


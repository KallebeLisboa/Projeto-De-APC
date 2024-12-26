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
        if any(char.isalpha() for char in oleo):
            print("Digite um valor válido sem letras")
            continue
        if " " in oleo:
            print("Digite um valor válido sem espaços")
            continue
        oleo = float(oleo)
        if oleo < 0:
            print("Digite um valor válido maior que 0")
            continue
        break

    #Cáuculo de água
    agua = ((oleo*agua_padrao)/oleo_padrao)

    #Cáuculo de soda
    soda = ((oleo*soda_padrao)/oleo_padrao)

    #Cáuculo de álcool
    alcool = ((oleo*alcool_padrao)/oleo_padrao)
    print("-"*15)
    print(f"A quantidade de óleo é {oleo:.2f} mLs")
    print(f"A quantidade de água é {agua:.2f} mLs")
    print(f"A quantidade de soda cáustica é {soda:.2f}g")
    print(f"A quantidade de álcool é {alcool:.2f} mLs")
    print("-"*15)


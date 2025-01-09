import finalizar

# Sub menu
def escolha():
    opcoes = {
        1: conversao_sabao,
        2: conversao_vela,
        3: conversao_sabonete,
        4: finalizar.finalizar_Sub_menu,
    }

    while True:
        print("\nPressione:")
        print("[1] Para produção de sabão")
        print("[2] Para produção de vela")
        print("[3] Para produção de sabonete")
        print("[4] Para voltar ao menu anterior")
        print()

        while True:
            decisao = input("Digite sua opção (1 a 4): ").strip()
            print("=-" * 15)

    # Verifica se a entrada contém apenas números
            if not decisao.isdigit():
                print("Digite um valor válido: apenas números inteiros de 1 a 4 são permitidos.")
                continue

    # Converte a entrada para número inteiro
            decisao = int(decisao)

    # Verifica se o número está no intervalo permitido
            if decisao < 1 or decisao > 4:
                print("Digite um número válido dentro do intervalo (1 a 4).")
                continue

    # Se for válido, sai do loop
            break
        if decisao in opcoes:
            opcoes[decisao]()  # Chama a função correspondente
            
        else:
            print("Opção inválida!")
        if decisao == 1:
            with open("escolha.txt", "w") as arquivo:
                arquivo.write("sabao")  # Atualiza a escolha no arquivo
            print("Você escolheu SABÃO. Retornando ao menu do produto...")
            return  # Sai do menu principal para executar a próxima lógica
        elif decisao == 2:
            with open("escolha.txt", "w") as arquivo:
                arquivo.write("vela")  # Atualiza a escolha no arquivo
            print("Você escolheu VELA. Retornando ao menu do produto...")
            return
        elif decisao == 3:
            with open("escolha.txt", "w") as arquivo:
                arquivo.write("sabonete")  # Atualiza a escolha no arquivo
            print("Você escolheu SABONETE. Retornando ao menu do produto...")
            return
def conversao_sabao():
    oleo_padrao = 1000.00 # Ml
    agua_padrao = 100.00 # Ml
    soda_padrao = 100.00 # G
    alcool_padrao = 5.00 # Ml

    #Verificação de número válido  
    while True:
        oleo = input("Quantos mLs de óleo serão usados: ").strip()
        print("=-"*15)
        # Verifica se a entrada contém apenas números
        if not oleo.isdigit():
            print("Digite um valor válido: apenas números inteiros são permitidos.(arredonde para baixo)")
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

    # Resultados
    print("-"*15)
    print(f"A quantidade de óleo é \033[1;32m{oleo:.2f} mLs\033[m")
    print(f"A quantidade de água é \033[1;32m{agua:.2f} mLs\033[m")
    print(f"A quantidade de soda cáustica é \033[1;32m{soda:.2f}g\033[m")
    print(f"A quantidade de álcool é \033[1;32m{alcool:.2f} mLs\033[m")
    print("-"*15)



def conversao_vela():
    oleo_padrao = 30.00 # Ml
    estearina_padrao = 10.00 # Ml
    essencia_padrao = 3 # Gotas
    
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
    
    # Cálculo estearina
    estearina = ((oleo*estearina_padrao)/oleo_padrao)

    # Cáuculo essencia
    essencia = ((oleo*essencia_padrao)/oleo_padrao)

    # Resultados
    print("-"*15)
    print(f"A quantidade de óleo é \033[1;32m{oleo:.2f} mLs\033[m")
    print(f"A quantidade de estarina é \033[1;32m{estearina:.2f} mLs\033[m")
    print(f"A quantidade de essencia (somente a base de óleo) é \033[1;32m{essencia:.2f} gotas\033[m")
    print(f"A quantidade de Corante em pó ou à base de óleo \033[1;32m{essencia:.2f} gotas ou pitadas\033[m")
    print(f"A quantidade de pedaços de barbante é \033[1;32m{essencia:.2f}, cada pedaço deve ser 3cm maior que o recipiente \033[m")
    print(f"A quantidade de prendedores de roupa é \033[1;32m{essencia:.2f}\033[m")
    print("-"*15)

def conversao_sabonete():
    oleo_padrao = 1000.00 # Ml
    agua_padrao = 340.00 # Ml
    soda_padrao = 135.00 # g

    #Verificação de número válido  
    while True:
        oleo = input("Quantos mLs de óleo serão usados: ").strip()
        print("=-"*15)
        # Verifica se a entrada contém apenas números
        if not oleo.isdigit():
            print("Digite um valor válido: apenas números inteiros são permitidos.(arredonde para baixo)")
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

    # Resultados
    print("-"*15)
    print(f"A quantidade de óleo é \033[1;32m{oleo:.2f} mLs\033[m")
    print(f"A quantidade de água é \033[1;32m{agua:.2f} mLs\033[m")
    print(f"A quantidade de soda cáustica é \033[1;32m{soda:.2f}g\033[m")
    print(f"A quantidade de fragrâncias e corantes (opcional) é \033[1;32ma gosto\033[m")
    print("-"*15)
# Protegendo a execução automática com if __name__ == "__main__"
if __name__ == "__main__":
    escolha()
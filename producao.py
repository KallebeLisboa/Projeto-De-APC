# Configuração para seguir e voltar nas informações
def escolha_produto():
    try:
    # Lendo a escolha do arquivo
        with open("escolha.txt", "r") as arquivo:
            produto = arquivo.read()
    except FileNotFoundError:
        print("Nenhuma escolha item foi feita. escolha qual item deseja produzir na opção 2.") 
    if produto == "sabao":
        producao_sabao()
    elif produto == "vela":
        producao_vela()
    elif produto == "sabonete":
        producao_sabonete()
    else: print("Nenhuma escolha de item foi feita. Escolha qual item deseja produzir na opção 2.")    

        
# Função para validar navegação
def fluxo(count, topicos):
    while True:
        seguir = input("opção: ").strip()
        if not seguir.isdigit():
            print("Digite um valor válido: apenas números inteiros (\033[1;33m0\033[m, \033[1;31m1\033[m ou \033[1;32m2\033[m).")
            continue
        seguir = int(seguir)
        if seguir == 2 and count < len(topicos):
            count += 1
            break
        elif seguir == 1 and count > 1:
            count -= 1
            break
        elif count == len(topicos):  # Menu especial ao final
            print("-" * 20)
            print("Estes são os passos para produção")
            print("Escolha uma opção:")
            print("\033[0;31m1 - Voltar para os tópicos anteriores\033[m")
            print("\033[0;32m2 - Reiniciar\033[m")
            print("\033[0;33m0 - Sair\033[m")
            print("-" * 20)

            # Captura a escolha no menu final
            menu_final = input("Opção no menu final: ").strip()
            if not menu_final.isdigit():
                print("Digite um número válido!")
                continue
            menu_final = int(menu_final)
            if menu_final == 1:  # Voltar aos tópicos anteriores
                count -= 1
                break
            elif menu_final == 2:  # Reiniciar a partir do primeiro tópico
                count = 1
                break
            elif menu_final == 0:  # Sair do programa
                return 0
            else:
                print("Opção inválida! Tente novamente.")
            continue
        elif seguir == 0:
            return 0  # Indica saída
        else:
            print("Opção inválida! Tente novamente.")
    return count

# Função para exibir o tópico atual
def exibir_topico(topico):
    print("-" * 20)
    print(topico)
    print("-" * 20)

# Função de produção de sabão
def producao_sabao():
    # Título
    print('-='*30)
    print(" "*20, "Produção de Sabão")
    print('-='*30)

    # Tópicos de informações
    topicos = [
        "1. Filtrar o óleo em um filtro de papel ou peneira com pano.",
        "2. Colocar o óleo usado em um recipiente plástico.",
        "3. Dissolver a soda cáustica em água fria\nCUIDADO! A soda cáustica queima e solta vapores tóxicos!",
        "4. Colocar, aos poucos, a solução de soda cáustica dissolvida em água no óleo e mexer vigorosamente até misturar bem.",
        "5. Adicionar um pouco de álcool de cozinha devagar até engrossar (ponto de doce de leite). Mexer até atingir o ponto.",
        "6. Colocar em uma forma de plástico e esperar secar por um dia."
    ]

    count = 1
    print("Pressione \033[1;31m1 para voltar\033[m, \033[1;32m2 para prosseguir\033[m, ou \033[1;33m0 para sair\033[m.\n")
    while True:
        exibir_topico(topicos[count - 1])
        count = fluxo(count, topicos)
        if count == 0:
            print("\033[4;33mVocê saiu da produção de sabão. Obrigado!\033[m")
            print("-" * 20)
            break

# Função de produção de vela
def producao_vela():
    # Título
    print('-='*30)
    print(" "*20, "Produção de Vela")
    print('-='*30)

    # Tópicos de informações
    topicos = [
        "1. Aquecer o óleo e a estearina juntos até derreter completamente. É necessário mexer. \n(Atenção: Mistura inflamável, aquecer com cuidado).",
        "2. Adicionar algumas gotas do corante e da essência.",
        "3. Retirar do aquecimento.",
        "4. Cortar um pedaço do barbante para usar como pavio. \nPrenda-o em um palito ou prendedor de roupa e posicione-o no centro do frasco com o palito ou com o prendedor apoiado nas bordas.",
        "5. Preencher o frasco pela metade com a mistura da vela. Deixar secar por 5 horas.",
    ]

    count = 1
    print("Pressione \033[1;31m1 para voltar\033[m, \033[1;32m2 para prosseguir\033[m, ou \033[1;33m0 para sair\033[m.\n")
    while True:
        exibir_topico(topicos[count - 1])
        count = fluxo(count, topicos)
        if count == 0:
            print("\033[4;33mVocê saiu da produção de vela. Obrigado!\033[m")
            print("-" * 20)
            break

# Função para produção de sabonete
def producao_sabonete():
     # Título
    print('-='*30)
    print(" "*20, "Produção de sabonete")
    print('-='*30)

     # Tópicos de informações
    topicos = [
        "1. Preparação do ambiente: Certifique-se de estar em um local bem ventilado e livre de crianças e animais. Use os equipamentos de segurança.",
        "2. Mistura da soda cáustica: Adicione cuidadosamente a soda cáustica à água destilada (nunca o contrário) e mexa até que esteja completamente dissolvida. \nA mistura vai esquentar, então tome cuidado.",
        "3. Aquecimento do óleo: Em um recipiente separado, aqueça o óleo até atingir aproximadamente 40-50°C.",
        "4. Mistura do óleo com a soda cáustica: Com cuidado, despeje a mistura de soda cáustica no óleo aquecido. \nMexa continuamente até que a mistura atinja a consistência de um mingau fino (isso pode levar de 15 a 30 minutos).",
        "5. Adicionar fragrâncias e corantes (opcional): Se desejar, adicione algumas gotas de óleo essencial ou corante natural e misture bem.",
        "6. Colocar nas formas: Despeje a mistura nas formas para sabão. Bata levemente as formas na superfície de trabalho para remover bolhas de ar.",
        "7. Cura: Cubra as formas com um pano ou plástico e deixe o sabonete descansar em um local seco e arejado por 24-48 horas, \naté que esteja firme o suficiente para ser desenformado.",
        "8. Cura final: Após desenformar, deixe o sabonete curar por mais 4 a 6 semanas. Isso permite que a soda cáustica reaja completamente e o sabão se torne seguro para uso."
    ]

    count = 1
    print("Pressione \033[1;31m1 para voltar\033[m, \033[1;32m2 para prosseguir\033[m, ou \033[1;33m0 para sair\033[m.\n")
    while True:
        exibir_topico(topicos[count - 1])
        count = fluxo(count, topicos)
        if count == 0:
            print("\033[4;33mVocê saiu da produção de vela. Obrigado!\033[m")
            print("-" * 20)
            break

# Protegendo a execução automática com if __name__ == "__main__"
if __name__ == "__main__":
    escolha_produto()
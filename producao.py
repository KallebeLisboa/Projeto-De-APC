# Configuração para seguir e voltar nas informações
def producao_sabao():

     # Título
    print('-='*30)
    print(" "*20, "produção")
    print('-='*30)

    # Tópicos de informações
    topicos = [
        "1. Filtrar o óleo em um filtro de papel ou peneira com pano.",
        "2. Colocar o óleo usado em um recipiente plástico.",
        "3. Dissolver a soda cáustica em na de água fria\nCUIDADO! A soda cáustica queima e solta vapores tóxicos!",
        "4. Colocar, aos poucos, a solução de soda cáustica dissolvida em água no óleo e mexer vigorosamente até misturar bem.",
        "5. Adicionar um pouco de álcool de cozinha devagar até engrossar (ponto de doce de leite). Mexer até atingir o ponto.",
        "6. Colocar em uma forma de plástico e esperar secar por um dia."
    ]

    # Função para validar navegação
    def fluxo(count):
        while True:
            seguir = input("opção: ").strip()
            if not seguir.isdigit():
                print("Digite um valor válido: apenas números inteiros (0, 1 ou 2).")
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
                print("Estes são os passos para produção de sabão")
                print("Escolha uma opção:")
                print("1 - Voltar para os tópicos anteriores")
                print("2 - Reiniciar do início")
                print("0 - Sair")
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

    # Exibição dos tópicos
    def exibir_topico(topico):
        print("-" * 20)
        print(topico)
        print("-" * 20)

    count = 1
    print("Pressione 1 para voltar, 2 para prosseguir, ou 0 para sair.\n")
    while True:
        exibir_topico(topicos[count - 1])
        count = fluxo(count)
        if count == 0:
            print("Você saiu da produção. Obrigado!")
            print("-" * 20)
            break


# Protegendo a execução automática com if __name__ == "__main__"
if __name__ == "__main__":
    producao_sabao()
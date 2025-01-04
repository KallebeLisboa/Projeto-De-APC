# Configuração para seguir e voltar nas informações
def informacoes_sabao():

     # Título
    print('-='*30)
    print(" "*20, "Informações")
    print('-='*30)

    # Tópicos de informações
    topicos = [
        "Você gosta de fritura? Pois é, elas são feitas com óleo de cozinha. E o que as pessoas fazem com o óleo que sobra na panela?",
        "O descarte inadequado gera uma série de problemas ambientais.",
        "Por não se misturar com a água, a presença de óleo nos rios cria uma barreira que dificulta a entrada de luz e a oxigenação da água,\ncomprometendo assim, a base da cadeia alimentar aquática e contribuindo para a ocorrência de enchentes e aquecimento do planeta\n(Revista Planeta Cidade, 2007).",
        "Entupimento do sistema de esgoto: O óleo solidifica quando esfria, levando ao entupimento de canos e sistemas de esgoto,\no que pode causar inundações e outros problemas de infraestrutura. ",
        "Deterioração do solo: O descarte inadequado em aterros pode infiltrar no solo, contaminando o lençol freático e prejudicando a qualidade do solo,\ntornando-o inadequado para a agricultura.",
        "Geração de mau cheiro: O acúmulo de óleo pode gerar odores desagradáveis, contribuindo para problemas de saúde pública\ne diminuição da qualidade de vida nas proximidades.",
        "Para evitar que o óleo de cozinha usado seja lançado na rede de esgoto, diversas são as possibilidades de reciclagem do óleo de fritura,\nvelas aromáticasm e sabão são exemplos de usos para reciclagem.",
        "Caso deseje apenas realizar o descarte de óleo, acesse o site abaixo e verifique o local de descarte mais próximo: \nhttps://www.ecycle.com.br/postos/reciclagem.php",
        "Fontes:\n\nScheffer, D., & Simonetto, E. O. (2011). 'Descarte do Óleo de Cozinha: Uma Análise dos Procedimentos nas Maiores Cidades do Rio Grande do Sul.' UFPE\n\nSantos, E. J. D. (2015). 'Estudo do Impacto Ambiental Ocasionado pelo Descarte Inadequado do Óleo de Cozinha no Ensino de Ciências.' Universidade Tecnológica Federal do Paraná\n\nSa, E., & Silva, R. (2020). 'Impactos Ambientais Causados pelo Descarte Inadequado do Óleo de Cozinha' ResearchGate",
    ]

    # Função para validar navegação
    def fluxo(count):
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
                print("Você está no final da lista de informações!")
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

    # Exibição dos tópicos
    def exibir_topico(topico):
        print("-" * 20)
        print(topico)
        print("-" * 20)

    count = 1
    print("Pressione \033[1;31m1 para voltar\033[m, \033[1;32m2 para prosseguir\033[m, ou \033[1;33m0 para sair\033[m.\n")
    while True:
        exibir_topico(topicos[count - 1])
        count = fluxo(count)
        if count == 0:
            print("\033[4;33mVocê saiu das informações. Obrigado!\033[m")
            print("-" * 20)
            break


# Protegendo a execução automática com if __name__ == "__main__"
if __name__ == "__main__":
    informacoes_sabao()
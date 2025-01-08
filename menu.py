import informacoes
import conversor
import producao
import finalizar

def menu():
    print('-='*30)
    print(" "*20, "Produção de Sabão")
    print('-='*30)

    print()

    # Menu de opções
    acoes = {
        1: informacoes.informacoes_sabao,
        2: conversor.escolha,
        3: producao.escolha_produto,
        4: finalizar.finalizar_programa,
    }

    # Loop do menu
    while True:
        print("\nPressione:")
        print("[1] Informações sobre meio ambiente")
        print("[2] Escolha do material produzido")
        print("[3] Produção de sabão")
        print("[4] Finalizar")
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
        if decisao in acoes:
            acoes[decisao]()  # Chama a função correspondente
        else:
            print("Opção inválida!")
            
# Protegendo a execução automática com if __name__ == "__main__"
if __name__ == "__main__":
    menu()
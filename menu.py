

def menu():
    print('-='*30)
    print(" "*20, "Produção de Sabão")
    print('-='*30)

    print()

    while True:
        print("Pressione: ")
        print("[1] Informações sobre meio ambiente")
        print("[2] Ingredientes")
        print("[3] Produção de sabão")
        print("[4] Finalizar")
        print()

        #verificação de valor
        while True:
            decisao = input().strip()
            print("=-"*15)
            if any(char.isalpha() for char in decisao):
                print("Digite um valor válido sem letras:")
                continue
            elif " " in decisao:
                print("Digite um valor válido sem espaços:")
                continue
            elif "." in decisao or "," in decisao:
                print("Digite um valor inteiro: ")
                continue
            elif any(char.isnumeric() for char in decisao):
                decisao = round(float(decisao))
                if decisao < 0 or decisao > 4:
                    print("Digite um valor válido entre 1 e 4:")
                    continue
            else:
                print("Digite um valor válido:")
                continue
            break
        if decisao == 2:
            import conversor
            conversor.conversao()
        if decisao == 4:
            break
    print("Obrigado pela atenção! tenha um ótimo dia.")
            
menu()
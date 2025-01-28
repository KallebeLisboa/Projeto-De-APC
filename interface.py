import customtkinter as ctk
from tkinter import messagebox

# Configuração do CustomTkinter
ctk.set_appearance_mode("System")  # "Light", "Dark" ou "System"
ctk.set_default_color_theme("blue")  # "blue", "green" ou "dark-blue"

# Dicionário com o passo a passo de cada produto
passo_a_passo = {
    "Sabão": [
        "1. Filtrar o óleo em um filtro de papel ou peneira com pano.",
        "2. Colocar o óleo usado em um recipiente plástico.",
        "3. Dissolver a soda cáustica em água fria CUIDADO! A soda cáustica queima e solta vapores tóxicos!",
        "4. Colocar, aos poucos, a solução de soda cáustica dissolvida em água no óleo e mexer vigorosamente até misturar bem.",
        "5. Adicionar um pouco de álcool de cozinha devagar até engrossar (ponto de doce de leite). Mexer até atingir o ponto.",
        "6. Colocar em uma forma de plástico e esperar secar por um dia."
    ],
    "Vela": [
        "1. Aquecer o óleo e a estearina juntos até derreter completamente. É necessário mexer. (Atenção: Mistura inflamável, aquecer com cuidado).",
        "2. Adicionar algumas gotas do corante e da essência.",
        "3. Retirar do aquecimento.",
        "4. Cortar um pedaço do barbante para usar como pavio. Prenda-o em um palito ou prendedor de roupa e posicione-o no centro do frasco com o palito ou com o prendedor apoiado nas bordas.",
        "5. Preencher o frasco pela metade com a mistura da vela. Deixar secar por 5 horas.",
    ],
    "Sabonete": [
        "1. Preparação do ambiente: Certifique-se de estar em um local bem ventilado e livre de crianças e animais. Use os equipamentos de segurança.",
        "2. Mistura da soda cáustica: Adicione cuidadosamente a soda cáustica à água destilada (nunca o contrário) e mexa até que esteja completamente dissolvida. A mistura vai esquentar, então tome cuidado.",
        "3. Aquecimento do óleo: Em um recipiente separado, aqueça o óleo até atingir aproximadamente 40-50°C.",
        "4. Mistura do óleo com a soda cáustica: Com cuidado, despeje a mistura de soda cáustica no óleo aquecido. Mexa continuamente até que a mistura atinja a consistência de um mingau fino (isso pode levar de 15 a 30 minutos).",
        "5. Adicionar fragrâncias e corantes (opcional): Se desejar, adicione algumas gotas de óleo essencial ou corante natural e misture bem.",
        "6. Colocar nas formas: Despeje a mistura nas formas para sabão. Bata levemente as formas na superfície de trabalho para remover bolhas de ar.",
        "7. Cura: Cubra as formas com um pano ou plástico e deixe o sabonete descansar em um local seco e arejado por 24-48 horas, até que esteja firme o suficiente para ser desenformado.",
        "8. Cura final: Após desenformar, deixe o sabonete curar por mais 4 a 6 semanas. Isso permite que a soda cáustica reaja completamente e o sabão se torne seguro para uso."
    ],
}

# Função para calcular proporções
def calcular_proporcao(oleo, valores_padrao):
    return {ingrediente: (oleo * qtd_padrao) / valores_padrao["oleo"] for ingrediente, qtd_padrao in valores_padrao.items()}

# Função para exibir o passo a passo dentro da aba principal
def mostrar_passo_a_passo(tipo):
    frame_principal.pack_forget()  # Esconde a tela principal
    frame_passo_a_passo.pack(fill="both", expand=True)  # Mostra a aba do passo a passo

    # Atualiza o título do passo a passo
    label_titulo_passo.configure(text=f"Passo a Passo - {tipo.capitalize()}")

    # Atualiza o texto do passo a passo
    texto_passo.configure(state="normal")
    texto_passo.delete("1.0", "end")
    for passo in passo_a_passo[tipo]:
        texto_passo.insert("end", passo + "\n\n")
    texto_passo.configure(state="disabled")

# Função para processar a conversão
def processar_conversao(tipo):
    try:
        oleo = float(entry_oleo.get())
        if oleo <= 0:
            messagebox.showwarning("Valor Inválido", "Digite um número maior que 0!")
            return
    except ValueError:
        messagebox.showwarning("Entrada Inválida", "Digite um valor numérico válido!")
        return

    # Dicionário de receitas
    receitas = {
        "Sabão": {"oleo": 1000, "agua": 100, "soda": 100, "alcool": 5},
        "Vela": {"oleo": 30, "estearina": 10, "essencia": 3, "corante": 1, "barbante": 1, "prendedor": 1},
        "Sabonete": {"oleo": 1000, "agua": 340, "soda": 135},
    }

    if tipo not in receitas:
        messagebox.showerror("Erro", "Tipo de conversão não encontrado.")
        return

    resultado = calcular_proporcao(oleo, receitas[tipo])

    # Formatação dos resultados
    texto_resultado = "-" * 15 + "\n"
    texto_resultado += f"Óleo: {oleo:.2f} mLs\n"

    if tipo == "Sabão":
        texto_resultado += f"Água: {resultado['agua']:.2f} mLs\n"
        texto_resultado += f"Soda Cáustica: {resultado['soda']:.2f}g\n"
        texto_resultado += f"Álcool: {resultado['alcool']:.2f} mLs\n"

    elif tipo == "Vela":
        texto_resultado += f"Estearina: {resultado['estearina']:.2f} mLs\n"
        texto_resultado += f"Essência: {resultado['essencia']:.2f} gotas\n"
        texto_resultado += f"Corante: {resultado['corante']:.2f} gotas ou pitadas\n"
        texto_resultado += f"Barbantes: {resultado['barbante']:.2f}, cada um 3cm maior que o recipiente(Um para cada potinho da vela)\n"
        texto_resultado += f"Prendedores de roupa: {resultado['prendedor']:.2f} (Um para cada potinho da vela)\n"

    elif tipo == "Sabonete":
        texto_resultado += f"Água: {resultado['agua']:.2f} mLs\n"
        texto_resultado += f"Soda Cáustica: {resultado['soda']:.2f}g\n"
        texto_resultado += "Fragrâncias e corantes (opcional): A gosto\n"

    texto_resultado += "-" * 15

    # Atualiza a interface gráfica com os resultados
    label_resultado.configure(text=texto_resultado)

    # Exibe o botão de passo a passo
    btn_passo_a_passo.configure(command=lambda: mostrar_passo_a_passo(tipo))
    btn_passo_a_passo.pack(pady=10)

# Função para voltar ao menu principal
def voltar_menu():
    frame_passo_a_passo.pack_forget()
    frame_principal.pack(fill="both", expand=True)
    btn_passo_a_passo.pack_forget()  # Esconde o botão "Passo a Passo" ao voltar

# Criando a janela principal
root = ctk.CTk()
root.title("Reciclagem de óleo")
root.geometry("650x650")

# Criando um frame principal (menu)
frame_principal = ctk.CTkFrame(root)
frame_principal.pack(fill="both", expand=True)

label_titulo = ctk.CTkLabel(frame_principal, text="Reciclagem de óleo", font=("Arial", 18, "bold"))
label_titulo.pack(pady=10)

label_instrucao = ctk.CTkLabel(frame_principal, text="Digite a quantidade de óleo que você usará na receita (mL):", font=("Arial", 14))
label_instrucao.pack()

entry_oleo = ctk.CTkEntry(frame_principal, font=("Arial", 14), width=200)
entry_oleo.pack(pady=5)

frame_botoes = ctk.CTkFrame(frame_principal)
frame_botoes.pack(pady=10)

btn_sabao = ctk.CTkButton(frame_botoes, text="Converter Sabão", font=("Arial", 12), command=lambda: processar_conversao("Sabão"))
btn_sabao.grid(row=0, column=0, padx=5, pady=5)

btn_vela = ctk.CTkButton(frame_botoes, text="Converter Vela", font=("Arial", 12), command=lambda: processar_conversao("Vela"))
btn_vela.grid(row=0, column=1, padx=5, pady=5)

btn_sabonete = ctk.CTkButton(frame_botoes, text="Converter Sabonete", font=("Arial", 12), command=lambda: processar_conversao("Sabonete"))
btn_sabonete.grid(row=0, column=2, padx=5, pady=5)

label_resultado = ctk.CTkLabel(frame_principal, text="", font=("Arial", 14), justify="left")
label_resultado.pack(pady=10)

btn_passo_a_passo = ctk.CTkButton(frame_principal, text="Ver Passo a Passo", font=("Arial", 14))
btn_passo_a_passo.pack_forget()


btn_sair = ctk.CTkButton(frame_principal, text="Sair", font=("Arial", 14), command=root.quit)
btn_sair.pack(pady=10)


# Criando o frame do passo a passo
frame_passo_a_passo = ctk.CTkFrame(root)

label_titulo_passo = ctk.CTkLabel(frame_passo_a_passo, text="", font=("Arial", 16, "bold"))
label_titulo_passo.pack(pady=10)

texto_passo = ctk.CTkTextbox(frame_passo_a_passo, font=("Arial", 12), wrap="word", height=300)
texto_passo.pack(fill="both", expand=True, padx=10, pady=5)
texto_passo.configure(state="disabled")

btn_voltar = ctk.CTkButton(frame_passo_a_passo, text="Voltar", font=("Arial", 14), command=voltar_menu)
btn_voltar.pack(pady=10)

# Tópicos de informações
topicos = [
    "Você gosta de fritura? Pois é, elas são feitas com óleo de cozinha. E o que as pessoas fazem com o óleo que sobra na panela?",
    "O descarte inadequado gera uma série de problemas ambientais.",
    "Por não se misturar com a água, a presença de óleo nos rios cria uma barreira que dificulta a entrada de luz e a oxigenação da água,\ncomprometendo assim, a base da cadeia alimentar aquática e contribuindo para a ocorrência de enchentes e aquecimento do planeta\n(Revista Planeta Cidade, 2007).",
    "Entupimento do sistema de esgoto: O óleo solidifica quando esfria, levando ao entupimento de canos e sistemas de esgoto,\no que pode causar inundações e outros problemas de infraestrutura.",
    "Deterioração do solo: O descarte inadequado em aterros pode infiltrar no solo, contaminando o lençol freático e prejudicando a qualidade do solo,\ntornando-o inadequado para a agricultura.",
    "Geração de mau cheiro: O acúmulo de óleo pode gerar odores desagradáveis, contribuindo para problemas de saúde pública\ne diminuição da qualidade de vida nas proximidades.",
    "Para evitar que o óleo de cozinha usado seja lançado na rede de esgoto, diversas são as possibilidades de reciclagem do óleo de fritura,\nvelas aromáticas e sabão são exemplos de usos para reciclagem.",
    "Caso deseje apenas realizar o descarte de óleo, acesse o site abaixo e verifique o local de descarte mais próximo: \nhttps://www.ecycle.com.br/postos/reciclagem.php",
    "Fontes:\n\nScheffer, D., & Simonetto, E. O. (2011). 'Descarte do Óleo de Cozinha: Uma Análise dos Procedimentos nas Maiores Cidades do Rio Grande do Sul.' UFPE\n\nSantos, E. J. D. (2015). 'Estudo do Impacto Ambiental Ocasionado pelo Descarte Inadequado do Óleo de Cozinha no Ensino de Ciências.' Universidade Tecnológica Federal do Paraná\n\nSa, E., & Silva, R. (2020). 'Impactos Ambientais Causados pelo Descarte Inadequado do Óleo de Cozinha' ResearchGate",
]

# Função para exibir as informações gerais
def mostrar_informacoes():
    frame_principal.pack_forget()  # Esconde a tela principal
    frame_informacoes.pack(fill="both", expand=True)  # Mostra a aba de informações gerais

    # Atualiza o título
    label_titulo_informacoes.configure(text="Informações Gerais sobre Reciclagem de Óleo")

    # Atualiza o texto com os tópicos
    texto_informacoes.configure(state="normal")
    texto_informacoes.delete("1.0", "end")  # Limpa o texto da caixa
    for topico in topicos:
        texto_informacoes.insert("end", topico + "\n\n")  # Insere os tópicos um por um
    texto_informacoes.configure(state="disabled")


# Função para voltar ao menu principal
def voltar_menu():
    # Esconde qualquer frame que não seja o menu
    # Esconde a aba do Passo a Passo
    frame_informacoes.pack_forget()  # Esconde a aba de Informações Gerais
    frame_principal.pack(fill="both", expand=True)  # Mostra a tela principal (menu)

# Criando o frame de informações gerais
frame_informacoes = ctk.CTkFrame(root)

label_titulo_informacoes = ctk.CTkLabel(frame_informacoes, text="", font=("Arial", 16, "bold"))
label_titulo_informacoes.pack(pady=10)

texto_informacoes = ctk.CTkTextbox(frame_informacoes, font=("Arial", 12), wrap="word", height=300)
texto_informacoes.pack(fill="both", expand=True, padx=10, pady=5)
texto_informacoes.configure(state="disabled")

btn_voltar_informacoes = ctk.CTkButton(frame_informacoes, text="Voltar", font=("Arial", 14), command=voltar_menu)
btn_voltar_informacoes.pack(pady=10)

# Criando o botão "Informações" na tela principal e centralizando-o
btn_informacoes = ctk.CTkButton(frame_botoes, text="Informações", font=("Arial", 12), command=mostrar_informacoes)
btn_informacoes.grid(row=1, column=0, columnspan=3, padx=5, pady=5)


# Inicia a interface gráfica
root.mainloop()

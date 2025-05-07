import os
import tkinter as tk
from tkinter import ttk

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

cidades = {
    "Rio de Janeiro": {
        "Estado": "RJ",
        "População": 6748000,
        "Área (km²)": 1182,
        "PIB (R$ bilhões)": 400,
        "Pontos Turísticos": 8
    },
    "São Paulo": {
        "Estado": "SP",
        "População": 12330000,
        "Área (km²)": 1521,
        "PIB (R$ bilhões)": 700,
        "Pontos Turísticos": 6
    },
    "Belo Horizonte": {
        "Estado": "MG",
        "População": 2523000,
        "Área (km²)": 331,
        "PIB (R$ bilhões)": 120,
        "Pontos Turísticos": 4
    },
    "Brasília": {
        "Estado": "DF",
        "População": 3055000,
        "Área (km²)": 5802,
        "PIB (R$ bilhões)": 260,
        "Pontos Turísticos": 5
    },
    "Montes Claros": {
        "Estado": "MOC",
        "População": 414240,
        "Área (km²)": 3470,
        "PIB (R$ bilhões)": 25,
        "Pontos Turísticos": 7,
    },
        "Campinas": {
     "Estado": "CAM",
     "População": 1139000,
     "Área (km²)": 795,
     "PIB (R$ bilhões)": 72,
     "Pontos Turísticos": 15,
        }
}


def mostrar_cidades():
    return list(cidades.keys())


def exibir_atributos(cidade):
    atributos_texto = f"\n📍 {cidade}\n"
    for atributo, valor in cidades[cidade].items():
        atributos_texto += f"- {atributo}: {valor}\n"
    return atributos_texto


def escolher_atributo():
    return atributo_combobox.get()


def comparar(cidade1, cidade2, atributo):
    valor1 = cidades[cidade1][atributo]
    valor2 = cidades[cidade2][atributo]

    resultado_texto = f"\n🔎 Comparando '{atributo}':\n"
    resultado_texto += f"{cidade1}: {valor1}\n"
    resultado_texto += f"{cidade2}: {valor2}\n"

    if valor1 > valor2:
        resultado_texto += f"\n🏆 {cidade1} venceu!"
    elif valor2 > valor1:
        resultado_texto += f"\n🏆 {cidade2} venceu!"
    else:
        resultado_texto += "\n⚖️ Empate!"

    return resultado_texto


def iniciar_comparacao():
    cidade1 = cidade_combobox1.get()
    cidade2 = cidade_combobox2.get()
    
    if not cidade1 or not cidade2:
        resultado_label.config(text="Por favor, escolha ambas as cidades.")
        return

    atributo = escolher_atributo()

    if not atributo:
        resultado_label.config(text="Por favor, escolha um atributo.")
        return

    atributos_cidade1 = exibir_atributos(cidade1)
    atributos_cidade2 = exibir_atributos(cidade2)

    resultado_comparacao = comparar(cidade1, cidade2, atributo)

    resultado_label.config(
        text=f"🃏 Cartas escolhidas:\n{atributos_cidade1}\n{atributos_cidade2}\n{resultado_comparacao}"
    )


def criar_interface():
    global cidade_combobox1, cidade_combobox2, atributo_combobox, resultado_label
    

    root = tk.Tk()
    root.title("Super Trunfo - Cidades")
    

    title_label = tk.Label(root, text="🌆 SUPER TRUNFO - CIDADES", font=("Arial", 16))
    title_label.pack(pady=10)
    

    cidade_label1 = tk.Label(root, text="Escolha a cidade para Jogador 1:")
    cidade_label1.pack()
    cidade_combobox1 = ttk.Combobox(root, values=mostrar_cidades())
    cidade_combobox1.pack(pady=5)
    

    cidade_label2 = tk.Label(root, text="Escolha a cidade para Jogador 2:")
    cidade_label2.pack()
    cidade_combobox2 = ttk.Combobox(root, values=mostrar_cidades())
    cidade_combobox2.pack(pady=5)
    

    atributo_label = tk.Label(root, text="Escolha o atributo para comparação:")
    atributo_label.pack()
    atributo_combobox = ttk.Combobox(root, values=["População", "Área (km²)", "PIB (R$ bilhões)", "Pontos Turísticos"])
    atributo_combobox.pack(pady=5)
    

    comparar_button = tk.Button(root, text="Comparar", command=iniciar_comparacao)
    comparar_button.pack(pady=10)


    resultado_label = tk.Label(root, text="Aguarde... Escolha as cidades e atributos.", justify="left", font=("Arial", 12))
    resultado_label.pack(pady=5)


    root.mainloop()


if __name__ == "__main__":
    criar_interface()

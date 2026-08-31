import tkinter as tk
import random

numero_secreto = 0
tentativas = 0
limiti = 20

janela = tk.TK()

janela.title("JOGO DE ADIVINHAÇÃO")
janela.geometry("450x500")

titulo = tk.Label(
janela,
text="JOGO ADIVINHAÇÃO",
font=("Arial", 20)
)

titulo.pack(pady=20)

campo_nome =tk.Entry(
janela,
font=("Arial", 14)
)

campo_nome.pack(pady=5)

texto_dificuldade =tk.Label(
janela,
text="ESCOLHA A DIFICULDADE"
)

texto_dificuldade.pack(pady=10)

DIFICULDADE =tk.StringVar()

dificuldade.set("Facil")

menu_dificuldade=tk.OpitionMenu(
janela,
dificuldade,
"Fcail"
"Medio"
)
menu_dificulade.pack
texto_palpite =tk.label(
janela,
text="Digite seu palpite:"
)
text_palpite.pack(pady=15)

campo_palpite.pack































botao_iniciar.pack(pady=10)


botao_tentar = tk.Button(
janela,
text="TENTAR",
command=verificar_palpite,
font=("Arial", 12)
)

botao_tentar.pack(pady=5)


# -----------------------------
# MANTÉM A JANELA ABERTA
# -----------------------------

janela.mainloop()

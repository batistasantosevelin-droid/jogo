)

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

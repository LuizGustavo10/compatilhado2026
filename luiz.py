import random
import tkinter as tk

janelas_abertas = []


def criar_janela():
 
    nova = tk.Toplevel(raiz)
    numero = len(janelas_abertas) + 1
    nova.title(f"Janela #{numero}")

    x = random.randint(80, 500)
    y = random.randint(80, 350)
    nova.geometry(f"260x120+{x}+{y}")

    rotulo = tk.Label(nova, text=f"Janela secundária #{numero}", font=("Arial", 11))
    rotulo.pack(pady=15)

    botao_fechar = tk.Button(nova, text="Fechar esta janela", command=lambda j=nova: fechar_janela(j))
    botao_fechar.pack()

    janelas_abertas.append(nova)
    atualizar_contador()


def fechar_janela(janela):
    if janela in janelas_abertas:
        janelas_abertas.remove(janela)
    janela.destroy()
    atualizar_contador()


def fechar_ultima():
    if janelas_abertas:
        ultima = janelas_abertas.pop()
        ultima.destroy()
        atualizar_contador()


def atualizar_contador():
    contador.config(text=f"Janelas secundárias abertas: {len(janelas_abertas)}")


raiz = tk.Tk()
raiz.title("Controlador de Janelas")
raiz.geometry("320x170+200+150")

tk.Label(raiz, text="Gerador de Janelas em Python", font=("Arial", 12, "bold")).pack(pady=(12, 4))

contador = tk.Label(raiz, text="Janelas secundárias abertas: 0", font=("Arial", 10))
contador.pack(pady=4)

tk.Button(raiz, text="Nova Janela", width=18, command=criar_janela).pack(pady=4)
tk.Button(raiz, text="Fechar Última", width=18, command=fechar_ultima).pack(pady=4)

raiz.mainloop()
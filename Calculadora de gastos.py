import tkinter as tk
from tkinter import messagebox
import json
import os

# Caminho do arquivo onde os dados serão salvos
ARQUIVO_DADOS = "dados.json"

# Função que carrega os dados salvos do arquivo (teto e débitos)
def carregar_dados():
    if os.path.exists(ARQUIVO_DADOS):
        with open(ARQUIVO_DADOS, "r") as f:
            dados = json.load(f)
            # Retorna o teto e a lista de débitos, com valores padrão se não existirem
            return dados.get("teto", 1000.0), dados.get("debitos", [])
    else:
        # Se o arquivo não existir, retorna os valores iniciais
        return 1000.0, []

# Função que salva os dados atuais no arquivo JSON
def salvar_dados():
    with open(ARQUIVO_DADOS, "w") as f:
        json.dump({"teto": teto, "debitos": debitos}, f)

# Função chamada quando o usuário clica no botão "Debitar"
def debitar_valor():
    global teto
    try:
        valor = float(entrada_valor.get())  # Tenta converter o valor digitado
        if valor == 0:
            messagebox.showinfo("Encerrado", "Você escolheu sair.")
            janela.quit()
        elif valor < 0:
            messagebox.showwarning("Valor inválido", "Não é permitido inserir valores negativos.")
        elif valor > teto:
            messagebox.showwarning("Excedeu o teto", f"O valor excede o teto restante de R$ {teto:.2f}.")
        else:
            # Debita valor, salva e atualiza interface
            teto -= valor
            debitos.append(valor)
            salvar_dados()
            atualizar_interface()
    except ValueError:
        # Caso o valor digitado não seja numérico
        messagebox.showerror("Erro", "Por favor, insira um valor numérico válido.")

# Atualiza a interface gráfica com a lista de débitos e o teto atual
def atualizar_interface():
    lista_debitos.delete(0, tk.END)  # Limpa a lista visual
    for i, valor in enumerate(debitos, 1):
        lista_debitos.insert(tk.END, f"{i}. R$ {valor:.2f}")  # Reinsere os valores atualizados
    label_teto.config(text=f"Teto restante: R$ {teto:.2f}")  # Atualiza o valor do teto
    entrada_valor.delete(0, tk.END)  # Limpa o campo de entrada

# Função que reseta o teto e os débitos para os valores iniciais
def resetar_dados():
    global teto, debitos
    resposta = messagebox.askyesno("Confirmação", "Tem certeza que deseja resetar tudo?")
    if resposta:
        teto = 1000.00
        debitos = []
        salvar_dados()
        atualizar_interface()

# Carrega os dados salvos ao iniciar o programa
teto, debitos = carregar_dados()

# Criação da janela principal do programa
janela = tk.Tk()
janela.title("Controle de Débitos")  # Título da janela
janela.geometry("350x450")           # Tamanho da janela
janela.resizable(False, False)       # Impede redimensionamento

# Texto de instrução
label_instrucao = tk.Label(janela, text="Digite o valor debitado:", font=("Arial", 12))
label_instrucao.pack(pady=10)

# Campo de entrada do valor
entrada_valor = tk.Entry(janela, font=("Arial", 12))
entrada_valor.pack(pady=5)

# Botão para debitar
botao_debitar = tk.Button(janela, text="Debitar", command=debitar_valor, font=("Arial", 12), bg="#4CAF50", fg="white")
botao_debitar.pack(pady=10)

# Botão para resetar tudo
botao_resetar = tk.Button(janela, text="Resetar Tudo", command=resetar_dados, font=("Arial", 12), bg="#f44336", fg="white")
botao_resetar.pack(pady=5)

# Label para mostrar o teto restante
label_teto = tk.Label(janela, text=f"Teto restante: R$ {teto:.2f}", font=("Arial", 14, "bold"))
label_teto.pack(pady=10)

# Lista onde aparecem os débitos realizados
lista_debitos = tk.Listbox(janela, width=40, height=10, font=("Courier", 11))
lista_debitos.pack(pady=10)

# Atualiza a interface com os dados já existentes (caso existam)
atualizar_interface()

# Inicia o loop da interface gráfica
janela.mainloop()

# Salva os dados ao encerrar o programa
salvar_dados()
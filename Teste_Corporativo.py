# ============= Importa a planilha e leitor de PDF para o código ===============================================
import pandas as pd
from fpdf import FPDF

# ==================== Função para ler a planilha funcionários ====================

def salarios_de_funcionarios():  #comando "def" AKA "definir" uma opção a ser ativada !
    try:
        caminho = r"M:\\GABRIEL\APOSTILAS\\programação ADS\\projetos\Salários dos funcionários .xlsx"
        df = pd.read_excel(caminho)
        print('\nPlanilha lida com sucesso!\n')
        print(df)
    except Exception as e:
        print(f"Erro ao ler a planilha: {e}")

# ==================== Função para ler a planilha fretes ====================

def fretes():
    try:
        caminho = r"M:\\GABRIEL\\APOSTILAS\\programação ADS\\projetos\\fretes.xlsx"
        df = pd.read_excel(caminho)
        print('\nPlanilha lida com sucesso!\n')
        print(df)
    except Exception as e:
        print(f"Erro ao ler a planilha: {e}")

# ==================== Função Gerar um PDF fretes ==================================

# caminho único reutilizável — use sempre raw-string ou barras duplas
CAMINHO_FRETES = r"M:\\GABRIEL\APOSTILAS\\programação ADS\\projetos\\fretes.xlsx"

def gerar_pdf_fretes(caminho_planilha=CAMINHO_FRETES):
    try:
        df = pd.read_excel(caminho_planilha)

        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=10)

        # cabeçalho
        for col in df.columns:
            pdf.cell(40, 8, str(col), border=1)
        pdf.ln()

        # linhas
        for _, linha in df.iterrows():
            for item in linha:
                pdf.cell(40, 8, str(item), border=1)
            pdf.ln()

        pdf.output("Tabela_de_Fretes.pdf")
        print("PDF gerado com sucesso!")

    except Exception as e:
        print("Erro ao gerar PDF:", e)


 # ==================== Função Gerar um PDF salarios ==================================

# caminho único reutilizável — use sempre raw-string ou barras duplas
CAMINHO_SAL = r"M:\\GABRIEL\APOSTILAS\\programação ADS\\projetos\Salários dos funcionários .xlsx"

def gerar_pdf_sal(caminho_planilha2=CAMINHO_SAL):
    try:
        df = pd.read_excel(caminho_planilha2)

        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=10)

        # cabeçalho
        for col in df.columns:
            pdf.cell(40, 8, str(col), border=1)
        pdf.ln()

        # linhas
        for _, linha in df.iterrows():
            for item in linha:
                pdf.cell(40, 8, str(item), border=1)
            pdf.ln()

        pdf.output("Tabela_de_salários.pdf")
        print("PDF gerado com sucesso!")

    except Exception as e:
        print("Erro ao gerar PDF:", e)        


# ==================== Função para calcular horas extras ====================
def Calcular_Horas_extras():
    print("\nBem-vindo!")
    while True:  # Laço principal
        while True:  # Valida o gatilho “on”
            resposta = input("Vamos dar início, digite 'on' para prosseguir: ").lower()
            if resposta == 'on':
                break
            print("Você digitou:", resposta)

        # ---------- bloco do cálculo ----------
        try:
            salario = float(input('Qual o seu salário? R$ '))   # O comando float serve para converter um número ou uma string para o tipo numérico com casas decimais.
            HORA_MES = 198   # Quantidade de horas trabalhadas no expediente de todos os funcionários
            horas_extras = float(input('Quantas horas extras você fez? '))
            valor_hora = salario / HORA_MES
            total = valor_hora * horas_extras * 1.5  # 50 % adicional

            print(f'Você deve receber R$ {total:.2f} pelos seus serviços!')
        except ValueError:
            print("Entrada inválida! Digite apenas números com ponto para decimais. Ex: 1703.99")
            continue

        if input('Quer saber o valor da hora extra? (sim/não) ').lower() == 'sim':
            print(f'O valor da sua hora extra é R$ {valor_hora:.2f}.')
        else:
            print('OK!')

        if input('Mais alguma coisa? (sim/não) ').lower() == 'sim':
            print('Siga o link: https://docs.google.com/spreadsheets/d/10C-nXcF-I-BmoAFlHspTJOUp2cgdyAY9/edit?usp=drive_link&ouid=110904478284834241787&rtpof=true&sd=true')
        else:
            print('Obrigado por confiar neste humilde código!')

        # ---------- decisão de reinício ----------
        if input('Deseja fazer outro cálculo? (sim/não) ').lower() == 'sim':
            print('\nReiniciando...\n')
        else:
            if input('Programa encerrado. Deseja abrir a planilha? (sim/não) ').lower() == 'sim':
                print('Siga o link:\nhttps://docs.google.com/spreadsheets/d/13TkwfRNowzGH3rVTq39giD9Jzs33ShBg/edit?usp=drive_link')
            else:
                print('Programa encerrado. Até a próxima!')
            break
#============================= CALCULADOR DE FERIAS ===============================================================

def calcular_ferias():
    print('\nBem vindo! ')
    
    while True:  # gatilho "on"
        respostaf = input('Vamos calcular suas férias, digite "on" para prosseguir: ').lower()
        if respostaf == 'on':
            break
        print('Você digitou:', respostaf)

    salario_base = float(input('Qual o seu salário? R$ ').replace(',', '.')) # Comando replace(',', '.') para substituir "," por "." já que no Python, as casas decimais são separadas por "."
    adicional_terco = salario_base / 3

    vendeu = input('Você vai vender 10 dias de férias? (sim/não) ').lower()
    abono = (salario_base / 30) * 10 if vendeu == 'sim' else 0

    tirar_quinzena = input('Você vai tirar apenas 15 dias de férias? (sim/não) ').lower()

    total_bruto = salario_base + adicional_terco + abono
    desconto_imposto = total_bruto * 0.16
    total_liquido = total_bruto - desconto_imposto
    
    vale_transporte = salario_base * 0.06
    total_liquido_com_vt = total_liquido - vale_transporte

    if tirar_quinzena == 'sim':
        meio_descanso = total_liquido_com_vt / 2
    else:
        meio_descanso = None

    print('\n=========== RESUMO ===========')
    print(f'Salário base .................: R$ {salario_base:,.2f}')
    print(f'Adicional 1/3 ................: R$ {adicional_terco:,.2f}')
    if abono:
        print(f'Abono (10 dias vendidos) .....: R$ {abono:,.2f}')
    print(f'Desconto IF (16%) ............. R$ {desconto_imposto:,.2f}')
    print(f'Total líquido ................: R$ {total_liquido:,.2f}')
    print(f'Vale-transporte (6%) .........: R$ {vale_transporte:,.2f}')
    print(f'Total líquido final ..........: R$ {total_liquido_com_vt:,.2f}')
    if tirar_quinzena:
        print(f'Total liquido final de 15 dias: R$ {meio_descanso:,.2f}')
    print('===============================')

# ==================== Cadastro de nomes ===================================
from fpdf import FPDF

def cadastro_de_nomes():
    print('==== Cadastro de nomes de funcionários ====')
    nomes = []  # A lista começa vazia

    while True:
        nome = input('Digite um nome para cadastrar ou "sair" para encerrar o programa: ').strip()
        if nome.lower() == 'sair':
            print('Encerrando o cadastro.')
            break
        elif nome in nomes:
            print(f'{nome} já cadastrado. Escreva um novo nome!')
        else:
            nomes.append(nome) # O append é um método usado para adicionar um item ao final de uma lista.
            print(f'{nome} cadastrado com sucesso!')

    print('\n=== Lista de nomes cadastrados ===')
    for n in nomes:
        print(f' - {n}')

    #gera PDF
    
    if nomes:
        gerar_pdf_nomes(nome)
    else:
        print('Nenhum nome cadastrado, PDF não será gerado !')
    
    def gerar_pdf_nomes():
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font('Arial', size= 10)
        
        pdf.cell(0, 10, txt="nomes cadastrados", In=True, align="C")
        pdf.In(10)
        for nome in nomes:
            pdf.cell(0, 10, txt=f"- {nome}", ln=True)

        nome_arquivo = "nomes_cadastrados.pdf"
        pdf.output(nome_arquivo)
    
        print(f"\nPDF gerado com sucesso: {nome_arquivo}")

# ==================== Menu Principal ===================================

def menu():
    while True:
        print('\n==== MENU PRINCIPAL ====')
        print('1 - Ler a planilha de salários')
        print('2 - Ler planilha de fretes')
        print('3 - Calcular horas extras')
        print('4 - Gerar PDF da planilha')
        print('5 - Calcular Férias')
        print('6 - Cadastro de nomes')
        print('0 - Sair')
        opcao = input('Escolha uma opção (1/2/3/4/5/6/0): ')

        if opcao == '1':
            salarios_de_funcionarios()

        elif opcao == '2':
            fretes()

        elif opcao == '3':
            Calcular_Horas_extras()

        elif opcao == '4':
            print("\nQual planilha você deseja exportar como PDF?")
            print("1 - Salários dos funcionários")
            print("2 - Fretes")
            escolha_pdf = input("Escolha uma opção (1/2): ")

            if escolha_pdf == '1':
                gerar_pdf_sal()
            elif escolha_pdf == '2':
                gerar_pdf_fretes()
            else:
                print("Opção inválida. Voltando ao menu principal.")

        elif opcao == '5':
            calcular_ferias()
        
        elif opcao == '6':
            cadastro_de_nomes()

        elif opcao == '0':
            print('Programa finalizado. Até logo!')
            break

        else:
            print('Opção inválida. Tente novamente.')

menu() 
import tkinter as tk  # Para criar interface gráfica
# Para abrir gerenciador de arquivos, e mostrar mensagens no windows
from tkinter import filedialog, messagebox
from os import path  # Para verificar se arquivo existe
# Importa função para processo de comparação de tabelas
from tabelas import conversao

root = tk.Tk()  # Variável raíz da interface tkinter
root.title('Comparação de tabelas de Notas')  # Título da interface

# Frames contendo cada campo de arquivo
frames = [
    {'texto': 'Tabela de contas a pagar FOCCO',
        'formatoArquivo': '.csv', },
    {'texto': 'Tabela de boletos do Banco',
        'formatoArquivo': '.xlsx .xls', }
]
lista_botoes = []


def guarda_arquivo(index):

    # Abre gerenciador de arquivos para selecionar o arquivo em excel
    nome_arquivo = filedialog.askopenfilename(initialdir='/', title='Selecione o arquivo', filetypes=[
                                              (f"Arquivo {frames[index]['formatoArquivo']}", frames[index]['formatoArquivo'])])

    # Deleta texto dentro da caixa de texto
    frames[index]['caixa'].delete(0, 'end')
    # Insere na caixa de texto o local do arquivo
    frames[index]['caixa'].insert(0, nome_arquivo)


def converter():

    for frame in frames:  # Para cada caixa de texto
        if frame['caixa'].get() == '':  # Se está vazia
            messagebox.showwarning(
                'Erro de arquivo', 'Um dos arquivos não foi especificado!')
            return
        # Se arquivo não existe (ou com nome errado)
        if not path.isfile(frame['caixa'].get()):
            messagebox.showwarning(
                'Erro de arquivo', 'Um dos arquivos não existe!')
            return

    # Se não houve nenhum erro acima, continua o código

    # Desabilita o clique de todos os botões
    for botao in lista_botoes:
        botao['state'] = tk.DISABLED

    try:
        # Chama função para converter
        conversao(frames[0]['caixa'].get(), frames[1]['caixa'].get())
    except:
        messagebox.showerror(
            'Erro', 'Houve um erro, tente novamente, por favor')
    else:
        # Mostra mensagem de conclusão
        messagebox.showinfo(
            'Concluído', 'Tabelas comparadas! Tenha um bom dia! :)')
    finally:
        # Apaga o texto de todas as caixas
        for frame in frames:
            frame['caixa'].delete(0, 'end')
        # Todos os botões voltam ao normal
        for botao in lista_botoes:
            botao['state'] = tk.NORMAL


for index, frame in enumerate(frames):

    # Cria um frame
    frame['frame'] = tk.LabelFrame(
        root, text=frame['texto'] + f'({frames[index]["formatoArquivo"]})', padx=5, pady=5)
    frame['frame'].pack(padx=10, pady=10)

    # Insere uma caixa de texto dentro do frame
    frame['caixa'] = tk.Entry(frame['frame'], width=70)
    frame['caixa'].grid(row=1, column=0)

    # Insere um botão dentro do frame
    lista_botoes.append(tk.Button(
        frame['frame'], text='Abrir arquivo', command=lambda index=index: guarda_arquivo(index)))
    lista_botoes[index].grid(row=1, column=1)

# Cria botão para habilitar conversão
lista_botoes.append(tk.Button(root, text='Converter', command=converter))
lista_botoes[-1].pack(pady=5)

# Dimensões da janela
app_width = 550
app_height = 200

# Centralizar a janela
root.geometry(f'{app_width}x{app_height}'
              f'+{int((root.winfo_screenwidth() / 2) - (app_width / 2))}'
              f'+{int((root.winfo_screenheight() / 2) - (app_height / 2))}')

root.mainloop()

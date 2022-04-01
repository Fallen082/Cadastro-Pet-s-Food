from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import sqlite3
from datetime import datetime
from time import strftime, gmtime
import shutil

# Conectar Banco de Dados
banco = sqlite3.connect("Clientes_Pet.db")
Cursor = banco.cursor()

banco.execute('''CREATE TABLE IF NOT EXISTS CLientes_PET(
              Data INTEGER,
              Nome TEXT,
              Número TEXT,
              Pet TEXT,
              Valor REAL,
              Serviço TEXT,
              Obs TEXT,
              Hora INTEGER)''')


def Tela_Init():
    # Configurações da tela
    Janela_Inicial = Tk()
    Janela_Inicial.title("Pets")
    Janela_Inicial.geometry('213x355+595+100')
    Janela_Inicial.resizable(False, False)
    Janela_Inicial.iconbitmap('Icone_barra.ico')
    Janela_Inicial.configure(bg="#999999")

    # Apresentação da loja
    Nome = Label(Janela_Inicial,
                 text="Pet's Food Graciliano", font="Ubuntu 15 bold",
                 bg="#999999", fg="#000000")
    Nome.grid(row=0, column=0, pady=5)

    # Botão Para Cadastrar novos Pets
    Cadastro = Button(Janela_Inicial,
                      text="Cadastrar", bg="#35a69a",
                      bd=6, width=15, height=2,
                      relief='ridge', font="Ubuntu 11 bold",
                      command=Tela_cadastro)
    Cadastro.grid(row=1, column=0, padx=23, pady=5)

    # Botão Para Acessar Os Registros Do Dia
    Registros = Button(Janela_Inicial,
                       text="Registros Do Dia", bg="#35a69a",
                       bd=6, width=15, height=2,
                       relief='ridge', font="Ubuntu 11 bold",
                       command=Tela_Registros)
    Registros.grid(row=2, column=0, pady=5)

    # Botão Para Filtrar Dia
    Filtrar = Button(Janela_Inicial,
                     text="Pesquisar Dia", bg="#35a69a",
                     bd=6, width=15, height=2,
                     relief='ridge', font="Ubuntu 11 bold",
                     command=Tela_Filtrar)
    Filtrar.grid(row=3, pady=3)

    # Botão Para Imprimir O valor total do dia

    '''Comando SQLITE Abaixo'''
    dados = "SELECT * FROM Clientes_Pet WHERE Data = ?"

    def Botao_Valor_Total():
        tot = 0
        for valor in Cursor.execute(dados, (f"{strftime('%d/%m/%Y', gmtime())}",)):
            if valor[5].isnumeric():
                acrescentar = int(valor[5])
                tot += acrescentar
        value = f'{tot:.2f} R$'

        Valor['text'] = value

    Valor_total = Button(Janela_Inicial,
                         text="Ver Valor do Dia", bg="#c48129",
                         bd=6, width=15, height=2,
                         relief='ridge', font="Ubuntu 11 bold",
                         command=Botao_Valor_Total)
    Valor_total.grid(row=4, pady=5)

    Valor = Label(Janela_Inicial,
                  text='', bg="#999999",
                  fg="#ff0000", font="Ubuntu 20")
    Valor.grid(row=5, pady=2)

    Janela_Inicial.mainloop()


def Tela_cadastro():
    janela_cadastro = Toplevel()
    janela_cadastro.title("Cadastro")
    janela_cadastro.geometry('350x350+595+150')
    janela_cadastro.resizable(False, False)
    janela_cadastro.iconbitmap('Icone_barra.ico')
    janela_cadastro.configure(bg="#999999")
    janela_cadastro.grab_set()

    # Nome do Dono
    Nome_Text = Label(janela_cadastro,
                      text="Nome do Dono", width=15, bg="#737373", fg="#000000",
                      font="Ubuntu 15 bold", relief='solid')
    Nome_Text.grid(row=0, column=0, pady=5)

    nome = Entry(janela_cadastro,
                 width=10, bg="#d0d1cf", bd=7, fg="#1219e3",
                 relief="sunken", font="Cambria 15 bold")
    nome.grid(row=0, column=1, pady=5)

    # Número de Telefone
    num_text = Label(janela_cadastro,
                     text="Número Telefonico", width=15, bg="#737373",
                     fg="#000000", font="Ubuntu 15 bold", relief='solid')
    num_text.grid(row=1, column=0, pady=5)

    num = Entry(janela_cadastro,
                width=10, bg="#d0d1cf", bd=7, fg="#1219e3",
                relief="sunken", font="Cambria 15 bold")
    num.grid(row=1, column=1, pady=5)

    # Nome Pet
    pet_nome = Label(janela_cadastro,
                     text="Nome do Pet", width=15, bg="#737373", relief='solid',
                     fg="#000000", font="Ubuntu 15 bold")
    pet_nome.grid(row=2, column=0, pady=5)

    pet = Entry(janela_cadastro,
                width=10, bg="#d0d1cf", bd=7, fg="#1219e3",
                relief="sunken", font="Cambria 15 bold")
    pet.grid(row=2, column=1, pady=5)

    # Serviço Feito
    servico_nome = Label(janela_cadastro,
                         text="Serviço Feito", width=15, bg="#737373", relief='solid',
                         fg="#000000", font="Ubuntu 15 bold")
    servico_nome.grid(row=3, column=0, pady=5)

    servico = Entry(janela_cadastro,
                    width=10, bg="#d0d1cf", bd=7, fg="#1219e3",
                    relief="sunken", font="Cambria 15 bold")
    servico.grid(row=3, column=1, pady=5)

    # Valor Total
    valor_nome = Label(janela_cadastro,
                       text="Valor Total", width=15, bg="#737373", relief='solid',
                       fg="#000000", font="Ubuntu 15 bold")
    valor_nome.grid(row=4, column=0, pady=5)

    valor = Entry(janela_cadastro,
                  width=10, bg="#d0d1cf", bd=7, fg="#1219e3",
                  relief="sunken", font="Cambria 15 bold")
    valor.grid(row=4, column=1, pady=5)

    # Observação
    observacao_nome = Label(janela_cadastro,
                            text="Observações", width=15, bg="#737373", relief='solid',
                            fg="#000000", font="Ubuntu 15 bold")
    observacao_nome.grid(row=5, column=0, pady=5)

    observacao = Entry(janela_cadastro,
                       width=10, bg="#d0d1cf", bd=7, fg="#db001a",
                       relief="sunken", font="Cambria 15 bold")
    observacao.grid(row=5, column=1, pady=5)

    def cadastrar():
        data = f'{strftime("%d/%m/%Y", gmtime())}'
        n = nome.get()
        telefone = num.get()
        nome_pet = pet.get()
        servico_feito = servico.get()
        valor_to = valor.get()
        obs = observacao.get()
        hora = f"{datetime.now().hour}:{strftime('%M', gmtime())}"

        if n == '' and telefone == '' and nome_pet == '' and servico_feito == '' and valor_to == '' and obs == '':
            messagebox.showerror('Nenhuma Informação', "Para Cadastrar Algum Pet é Necessario ao Menos uma Informação")

        else:
            Cursor.execute(f"""INSERT INTO Clientes_PET VALUES('{data}', '{n}', '{telefone}', '{nome_pet}',
            '{servico_feito}', '{valor_to}', '{obs}', '{hora}') """)
            banco.commit()

        janela_cadastro.destroy()

    def Fechar():
        janela_cadastro.destroy()

    # Botão para Cadastrar e Fechar a tela
    cadastrar = Button(janela_cadastro,
                       text="Cadastrar", bg="#32a4e6", bd=8, height=1,
                       width=15, relief='raised', font="Ubuntu 11 bold",
                       command=cadastrar)
    cadastrar.grid(row=6, pady=3, padx=4, column=1)

    # Cancelar Cadastro
    Cancelar = Button(janela_cadastro,
                      text="Cancelar", bg="#e6151f", bd=8, height=1,
                      width=13, relief='raised', font="Ubuntu 11 bold",
                      command=Fechar)
    Cancelar.grid(row=6, column=0, pady=3)


def Tela_Registros():
    # Comando SQLITE
    dados = "SELECT * FROM Clientes_Pet WHERE Data = ?"

    # Congigurações janela
    janela_registros = Toplevel()
    janela_registros.title(f'Registros  {strftime("%d/%m/%Y", gmtime())}')
    janela_registros.geometry('692x365+350+150')
    janela_registros.resizable(False, False)
    janela_registros.iconbitmap('Icone_barra.ico')
    janela_registros.configure(bg="#999999")
    janela_registros.grab_set()

    # Definindo Tema Treeview
    tema = ttk.Style()
    tema.theme_use('alt')
    tema.configure("Treeview", background="#fcd4d2", fieldbackground="#fcd4d2")

    # Tree view
    arvore = ttk.Treeview(janela_registros, selectmode='browse', height=13,
                          columns=('d', 'n', 'num', 'p', 's', 'v', 'obs', 'hrs'), show='headings')

    arvore.column('d', width=75, stretch=YES)
    arvore.heading("#1", text="Data", anchor=CENTER)

    arvore.column('n', width=90, stretch=YES)
    arvore.heading("#2", text="Nome", anchor=CENTER)

    arvore.column('num', width=92, stretch=YES)
    arvore.heading("#3", text="Telefone", anchor=CENTER)

    arvore.column('p', width=80, stretch=YES)
    arvore.heading("#4", text="Pet", anchor=CENTER)

    arvore.column('s', width=90, stretch=YES)
    arvore.heading("#5", text="Serviço")

    arvore.column('v', width=60, stretch=YES)
    arvore.heading("#6", text="Valor", anchor=CENTER)

    arvore.column('obs', width=130, stretch=YES)
    arvore.heading("#7", text="Observação", anchor=CENTER)

    arvore.column('hrs', width=43, stretch=YES)
    arvore.heading("#8", text="Hora")

    arvore.grid(row=1, column=1, columnspan=10, padx=5, pady=5)

    sroll_bar = ttk.Scrollbar(janela_registros, orient='vertical', command=arvore.yview)
    arvore.configure(yscrollcommand=sroll_bar.set(1, 2))
    sroll_bar.grid(row=1, column=11, sticky='ns')
    for dado in Cursor.execute(dados, (f"{strftime('%d/%m/%Y', gmtime())}",)):
        arvore.insert('', END, values=dado)

    def Botao_Valor_Total():
        tot = 0
        dogs = 0
        for valor in Cursor.execute(dados, (f"{strftime('%d/%m/%Y', gmtime())}",)):
            if valor[5].isnumeric():
                acrescentar = int(valor[5])
                tot += acrescentar
            dogs += 1
        value = f'{tot:.2f} R$'
        Quantidade['text'] = dogs
        Valor_reg['text'] = value

    def deletar_comand():

        try:
            Selecao = arvore.selection()[0]
            valores = arvore.item(Selecao, "values")
            arvore.delete(Selecao)
            deletar_BD = f"DELETE FROM Clientes_PET WHERE Data = '{valores[0]}' " \
                         f"AND Nome = '{valores[1]}' AND Pet ='{valores[3]}' "
            Cursor.execute(deletar_BD)
            banco.commit()

        except:
            pass

    Deletar = Button(janela_registros,
                     text="DELETAR", bg="#e6151f",
                     bd=8, width=13, height=2,
                     relief='raised', font="Ubuntu 11 bold",
                     command=deletar_comand)
    Deletar.grid(row=0, column=1, pady=5, )

    Quantidade = Label(janela_registros,
                       text='    ', bg="#d0d1cf", bd=8,
                       fg="#000000", font="Cambria 15 bold", relief='sunken')
    Quantidade.grid(row=0, column=6, pady=5)

    Valor_total = Button(janela_registros,
                         text="Quantidade e Valor", bg="#53c9c9",
                         bd=7, width=18, height=2,
                         relief='raised', font="Ubuntu 9 bold",
                         command=Botao_Valor_Total)
    Valor_total.grid(row=0, column=3, pady=5, padx=20)

    Valor_reg = Label(janela_registros,
                      text='                       ', bg="#d0d1cf", bd=8,
                      fg="#000000", font="Cambria 15 bold", relief='sunken')
    Valor_reg.grid(row=0, column=8, pady=5)

    janela_registros.mainloop()


def Tela_Filtrar():
    tela_filtro = Tk()
    tela_filtro.title("Filtragem")
    tela_filtro.geometry('220x350+595+150')
    tela_filtro.resizable(False, False)
    tela_filtro.iconbitmap('Icone_barra.ico')
    tela_filtro.configure(bg="#999999")

    def Filtro_Data():
        # Comando SQLITE
        dados = "SELECT * FROM Clientes_Pet WHERE Data = ?"
        Datasinha = Data_search.get()
        if Datasinha == '':
            messagebox.showerror('NENHUMA DATA INFORMADA', "É Necessario Inserir alguma Data Para Acessar os Registros")
            tela_filtro.destroy()
        else:
            # Congigurações janela
            janela_registros = Toplevel()
            janela_registros.title(f'Registros  {strftime("%d/%m/%Y", gmtime())}')
            janela_registros.geometry('692x365+350+150')
            janela_registros.resizable(False, False)
            janela_registros.iconbitmap('Icone_barra.ico')
            janela_registros.configure(bg="#999999")
            janela_registros.grab_set()

            # Definindo Tema Treeview
            tema = ttk.Style()
            tema.theme_use('alt')
            tema.configure("Treeview", background="#fcd4d2", fieldbackground="#fcd4d2")

            # Tree view
            arvore = ttk.Treeview(janela_registros, selectmode='browse', height=13,
                                  columns=('d', 'n', 'num', 'p', 's', 'v', 'obs', 'hrs'), show='headings')

            arvore.column('d', width=75, stretch=YES)
            arvore.heading("#1", text="Data", anchor=CENTER)

            arvore.column('n', width=90, stretch=YES)
            arvore.heading("#2", text="Nome", anchor=CENTER)

            arvore.column('num', width=92, stretch=YES)
            arvore.heading("#3", text="Telefone", anchor=CENTER)

            arvore.column('p', width=80, stretch=YES)
            arvore.heading("#4", text="Pet", anchor=CENTER)

            arvore.column('s', width=90, stretch=YES)
            arvore.heading("#5", text="Serviço")

            arvore.column('v', width=60, stretch=YES)
            arvore.heading("#6", text="Valor", anchor=CENTER)

            arvore.column('obs', width=130, stretch=YES)
            arvore.heading("#7", text="Observação", anchor=CENTER)

            arvore.column('hrs', width=43, stretch=YES)
            arvore.heading("#8", text="Hora")

            arvore.grid(row=1, column=1, columnspan=10, padx=5, pady=5)

            sroll_bar = ttk.Scrollbar(janela_registros, orient='vertical', command=arvore.yview)
            arvore.configure(yscrollcommand=sroll_bar.set(1, 1))
            sroll_bar.grid(row=1, column=11, sticky='ns')

            for dado in Cursor.execute(dados, (f"{Datasinha}",)):
                arvore.insert('', END, values=dado)

            def Botao_Valor_Total():
                tot = 0
                dogs = 0
                for valor in Cursor.execute(dados, (f'{Datasinha}',)):
                    if valor[5].isnumeric():
                        acrescentar = int(valor[5])
                        tot += acrescentar
                    dogs += 1
                value = f'{tot:.2f} R$'
                Quantidade['text'] = dogs
                Valor_reg['text'] = value

            def deletar_comand():
                try:
                    itens1 = arvore.selection()[0]
                    item = arvore.item(itens1, 'values')
                    arvore.delete(itens1)
                    delete = f"DELETE FROM Clientes_PET WHERE Data = '{item[0]}' " \
                             f"AND Nome = '{item[1]}' AND Pet = '{item[3]}'"
                    Cursor.execute(delete)
                    banco.commit()

                except:
                    pass

            Deletar = Button(janela_registros,
                             text="DELETAR", bg="#e6151f",
                             bd=7, width=13, height=2,
                             relief='raised', font="Ubuntu 11 bold",
                             command=deletar_comand)
            Deletar.grid(row=0, column=1, pady=5)

            Quantidade = Label(janela_registros,
                               text='    ', bg="#d0d1cf", bd=8,
                               fg="#000000", font="Cambria 15 bold", relief='sunken')
            Quantidade.grid(row=0, column=6, pady=5)

            Valor_total = Button(janela_registros,
                                 text="Quantidade e Valor", bg="#53c9c9",
                                 bd=7, width=18, height=2,
                                 relief='raised', font="Ubuntu 9 bold",
                                 command=Botao_Valor_Total)
            Valor_total.grid(row=0, column=3, pady=5, padx=20)

            Valor_reg = Label(janela_registros,
                              text='                       ', bg="#d0d1cf", bd=8,
                              fg="#000000", font="Cambria 15 bold", relief='sunken')
            Valor_reg.grid(row=0, column=8, pady=5)

            janela_registros.mainloop()

    def Filtro_Nome():
        # Comando SQLITE
        nome = "SELECT * FROM Clientes_Pet WHERE Nome = ?"
        nomesin_filtro = Nome_search.get()
        if nomesin_filtro == '':
            messagebox.showerror("NENHUM NOME", 'Para Acessar Os Registros é necessario Inserir Alguma Informação')
            tela_filtro.destroy()
        else:
            # Congigurações janela
            janela_registros = Toplevel()
            janela_registros.title(f'Registros  {strftime("%d/%m/%Y", gmtime())}')
            janela_registros.geometry('692x365+350+150')
            janela_registros.resizable(False, False)
            janela_registros.iconbitmap('Icone_barra.ico')
            janela_registros.configure(bg="#999999")
            janela_registros.grab_set()

            # Definindo Tema Treeview
            tema = ttk.Style()
            tema.theme_use('alt')
            tema.configure("Treeview", background="#fcd4d2", fieldbackground="#fcd4d2")

            # Tree view
            arvore = ttk.Treeview(janela_registros, selectmode='browse', height=13,
                                  columns=('d', 'n', 'num', 'p', 's', 'v', 'obs', 'hrs'), show='headings')

            arvore.column('d', width=75, stretch=YES)
            arvore.heading("#1", text="Data", anchor=CENTER)

            arvore.column('n', width=90, stretch=YES)
            arvore.heading("#2", text="Nome", anchor=CENTER)

            arvore.column('num', width=92, stretch=YES)
            arvore.heading("#3", text="Telefone", anchor=CENTER)

            arvore.column('p', width=80, stretch=YES)
            arvore.heading("#4", text="Pet", anchor=CENTER)

            arvore.column('s', width=90, stretch=YES)
            arvore.heading("#5", text="Serviço")

            arvore.column('v', width=60, stretch=YES)
            arvore.heading("#6", text="Valor", anchor=CENTER)

            arvore.column('obs', width=130, stretch=YES)
            arvore.heading("#7", text="Observação", anchor=CENTER)

            arvore.column('hrs', width=43, stretch=YES)
            arvore.heading("#8", text="Hora")

            arvore.grid(row=1, column=1, columnspan=10, padx=5, pady=5)

            sroll_bar = ttk.Scrollbar(janela_registros, orient='vertical', command=arvore.yview)
            arvore.configure(yscrollcommand=sroll_bar.set(1, 1))
            sroll_bar.grid(row=1, column=11, sticky='ns')

            for pessoa in Cursor.execute(nome, (f'{nomesin_filtro}',)):
                arvore.insert('', END, values=pessoa)

            def Botao_Valor_Total():
                tot = 0
                dogs = 0
                for valor in Cursor.execute(nome, (f"{nomesin_filtro}",)):
                    if valor[5].isnumeric():
                        acrescentar = int(valor[5])
                        tot += acrescentar
                        dogs += 1
                value = f'{tot:.2f} R$'
                Quantidade['text'] = dogs
                Valor_reg['text'] = value

            def deletar_comand():
                try:
                    itens1 = arvore.selection()[0]
                    item = arvore.item(itens1, 'values')
                    arvore.delete(itens1)
                    deletar = f"DELETE FROM Clientes_PET WHERE Data = '{item[0]}'" \
                              f" AND Nome = '{item[1]}' AND Pet = '{item[3]}'"
                    Cursor.execute(deletar)
                    banco.commit()

                except:
                    pass

            Deletar = Button(janela_registros,
                             text="DELETAR", bg="#e6151f",
                             bd=7, width=13, height=2,
                             relief='raised', font="Ubuntu 11 bold",
                             command=deletar_comand)
            Deletar.grid(row=0, column=2, pady=5)

            Quantidade = Label(janela_registros,
                               text='   ', bg="#d0d1cf", bd=8,
                               fg="#000000", font="Cambria 15 bold", relief='sunken')
            Quantidade.grid(row=0, column=6, pady=5)

            Valor_total = Button(janela_registros,
                                 text="Quantidade e Valor", bg="#53c9c9",
                                 bd=7, width=18, height=2,
                                 relief='raised', font="Ubuntu 9 bold",
                                 command=Botao_Valor_Total)
            Valor_total.grid(row=0, column=3, pady=5, padx=20)

            Valor_reg = Label(janela_registros,
                              text='                       ', bg="#d0d1cf", bd=8,
                              fg="#000000", font="Cambria 15 bold", relief='sunken')
            Valor_reg.grid(row=0, column=8, pady=5)

    def Filtro_Pet():
        # Comando SQLITE
        Pet = "SELECT * FROM Clientes_Pet WHERE Pet = ?"
        Petsin_Filtro = Pet_search.get()
        if Petsin_Filtro == '':
            messagebox.showerror("NENHUM PET", 'Para Acessar Os Registros é necessario Inserir Alguma Informação')
            tela_filtro.destroy()
        else:
            # Congigurações janela
            janela_registros = Toplevel()
            janela_registros.title(f'Registros  {strftime("%d/%m/%Y", gmtime())}')
            janela_registros.geometry('692x365+350+150')
            janela_registros.resizable(False, False)
            janela_registros.iconbitmap('Icone_barra.ico')
            janela_registros.configure(bg="#999999")
            janela_registros.grab_set()

            # Definindo Tema Treeview
            tema = ttk.Style()
            tema.theme_use('alt')
            tema.configure("Treeview", background="#fcd4d2", fieldbackground="#fcd4d2")

            # Tree view
            arvore = ttk.Treeview(janela_registros, selectmode='browse', height=13,
                                  columns=('d', 'n', 'num', 'p', 's', 'v', 'obs', 'hrs'), show='headings')

            arvore.column('d', width=75, stretch=YES)
            arvore.heading("#1", text="Data", anchor=CENTER)

            arvore.column('n', width=90, stretch=YES)
            arvore.heading("#2", text="Nome", anchor=CENTER)

            arvore.column('num', width=92, stretch=YES)
            arvore.heading("#3", text="Telefone", anchor=CENTER)

            arvore.column('p', width=80, stretch=YES)
            arvore.heading("#4", text="Pet", anchor=CENTER)

            arvore.column('s', width=90, stretch=YES)
            arvore.heading("#5", text="Serviço")

            arvore.column('v', width=60, stretch=YES)
            arvore.heading("#6", text="Valor", anchor=CENTER)

            arvore.column('obs', width=130, stretch=YES)
            arvore.heading("#7", text="Observação", anchor=CENTER)

            arvore.column('hrs', width=43, stretch=YES)
            arvore.heading("#8", text="Hora")

            arvore.grid(row=1, column=1, columnspan=10, padx=5, pady=5)

            sroll_bar = ttk.Scrollbar(janela_registros, orient='vertical', command=arvore.yview)
            arvore.configure(yscrollcommand=sroll_bar.set(1, 1))
            sroll_bar.grid(row=1, column=11, sticky='ns')

            for pessoa in Cursor.execute(Pet, (f'{Petsin_Filtro}',)):
                arvore.insert('', END, values=pessoa)

            def Botao_Valor_Total():
                tot = 0
                dogs = 0
                for valor in Cursor.execute(Pet, (f"{Petsin_Filtro}",)):
                    if valor[5].isnumeric():
                        acrescentar = int(valor[5])
                        tot += acrescentar
                    dogs += 1
                value = f'{tot:.2f} R$'
                Quantidade['text'] = dogs
                Valor_reg['text'] = value

            def deletar_comand():
                try:
                    Selecao = arvore.selection()[0]
                    valores = arvore.item(Selecao, "values")
                    arvore.delete(Selecao)
                    deletar_BD = f"DELETE FROM Clientes_PET WHERE Data = '{valores[0]}' " \
                                 f"AND Nome = '{valores[1]}' AND Pet ='{valores[3]}' "
                    Cursor.execute(deletar_BD)
                    banco.commit()

                except:
                    pass

            Deletar = Button(janela_registros,
                             text="DELETAR", bg="#e6151f",
                             bd=7, width=13, height=2,
                             relief='raised', font="ubuntu 11 bold",
                             command=deletar_comand)
            Deletar.grid(row=0, column=2, pady=5)

            Quantidade = Label(janela_registros,
                               text='    ', bg="#d0d1cf", bd=8,
                               fg="#000000", font="Cambria 15 bold", relief='sunken')
            Quantidade.grid(row=0, column=6, pady=5)

            Valor_total = Button(janela_registros,
                                 text="Quantidade e Valor", bg="#53c9c9",
                                 bd=7, width=18, height=2,
                                 relief='raised', font="Ubuntu 9 bold",
                                 command=Botao_Valor_Total)
            Valor_total.grid(row=0, column=3, pady=5, padx=20)

            Valor_reg = Label(janela_registros,
                              text='                       ', bg="#d0d1cf", bd=8,
                              fg="#000000", font="Cambria 15 bold", relief='sunken')
            Valor_reg.grid(row=0, column=8, pady=5)

    def Filtro_Mes():
        # Comando SQLITE
        mes = box.get()

        if mes == "Janeiro":
            mes = "01"
        elif mes == "Fevereiro":
            mes = "02"
        elif mes == "Março":
            mes = "03"
        elif mes == "Abril":
            mes = "04"
        elif mes == "Maio":
            mes = "05"
        elif mes == "Junho":
            mes = "06"
        elif mes == "Julho":
            mes = "07"
        elif mes == "Agosto":
            mes = "08"
        elif mes == "Setembro":
            mes = "09"
        elif mes == "Outubro":
            mes = "10"
        elif mes == "Novembro":
            mes = "11"
        elif mes == "Dezembro":
            mes = "12"

        dados = f"SELECT * FROM Clientes_Pet"
        if mes == '':
            messagebox.showerror("MÊS INVALIDO", "Para Prosseguir Selecione Algum Mês Válido")
            tela_filtro.destroy()
        else:
            # Congigurações janela
            janela_registros = Toplevel()
            janela_registros.title(f'Registros Mês {mes}')
            janela_registros.geometry('692x365+350+150')
            janela_registros.resizable(False, False)
            janela_registros.iconbitmap('Icone_barra.ico')
            janela_registros.configure(bg="#999999")
            janela_registros.grab_set()

            # Definindo Tema Treeview
            tema = ttk.Style()
            tema.theme_use('alt')
            tema.configure("Treeview", background="#fcd4d2", fieldbackground="#fcd4d2")

            # Tree view
            arvore = ttk.Treeview(janela_registros, selectmode='browse', height=13,
                                  columns=('d', 'n', 'num', 'p', 's', 'v', 'obs', 'hrs'), show='headings')

            arvore.column('d', width=75, stretch=YES)
            arvore.heading("#1", text="Data", anchor=CENTER)

            arvore.column('n', width=90, stretch=YES)
            arvore.heading("#2", text="Nome", anchor=CENTER)

            arvore.column('num', width=92, stretch=YES)
            arvore.heading("#3", text="Telefone", anchor=CENTER)

            arvore.column('p', width=80, stretch=YES)
            arvore.heading("#4", text="Pet", anchor=CENTER)

            arvore.column('s', width=90, stretch=YES)
            arvore.heading("#5", text="Serviço")

            arvore.column('v', width=60, stretch=YES)
            arvore.heading("#6", text="Valor", anchor=CENTER)

            arvore.column('obs', width=130, stretch=YES)
            arvore.heading("#7", text="Observação", anchor=CENTER)

            arvore.column('hrs', width=43, stretch=YES)
            arvore.heading("#8", text="Hora")

            arvore.grid(row=1, column=1, columnspan=10, padx=5, pady=5)

            sroll_bar = ttk.Scrollbar(janela_registros, orient='vertical', command=arvore.yview)
            arvore.configure(yscrollcommand=sroll_bar.set(1, 1))
            sroll_bar.grid(row=1, column=11, sticky='ns')

            for dado in Cursor.execute(dados):
                data = dado[0]
                if data[3:5] == mes:
                    arvore.insert('', END, values=dado)

            def Botao_Valor_Total():
                tot = 0
                dogs = 0
                for valor in Cursor.execute(dados):
                    price = valor[0]
                    if price[3:5] == mes:
                        if valor[5].isnumeric():
                            acrescentar = int(valor[5])
                            tot += acrescentar
                        dogs += 1
                    value = f'{tot:.2f} R$'
                    Quantidade['text'] = dogs
                    Valor_reg['text'] = value

            def deletar_comand():
                try:
                    itens1 = arvore.selection()[0]
                    item = arvore.item(itens1, 'values')
                    arvore.delete(itens1)
                    delete = f"DELETE FROM Clientes_PET WHERE Data = '{item[0]}' " \
                             f"AND Nome = '{item[1]}' AND Pet = '{item[3]}'"
                    Cursor.execute(delete)
                    banco.commit()

                except:
                    pass

            Deletar = Button(janela_registros,
                             text="DELETAR", bg="#e6151f",
                             bd=7, width=13, height=2,
                             relief='raised', font="Ubuntu 11 bold",
                             command=deletar_comand)
            Deletar.grid(row=0, column=1, pady=5)

            Quantidade = Label(janela_registros,
                               text='    ', bg="#d0d1cf", bd=8,
                               fg="#000000", font="Cambria 15 bold", relief='sunken')
            Quantidade.grid(row=0, column=6, pady=5)

            Valor_total = Button(janela_registros,
                                 text="Quantidade e Valor", bg="#53c9c9",
                                 bd=7, width=18, height=2,
                                 relief='raised', font="Ubuntu 9 bold",
                                 command=Botao_Valor_Total)
            Valor_total.grid(row=0, column=3, pady=5, padx=20)

            Valor_reg = Label(janela_registros,
                              text='                       ', bg="#d0d1cf", bd=8,
                              fg="#000000", font="Cambria 15 bold", relief='sunken')
            Valor_reg.grid(row=0, column=8, pady=5)

            janela_registros.mainloop()

    Nome_Botao = Button(tela_filtro,
                        text="Nome", bg="#088A08",
                        bd=7, width=19, height=2,
                        relief='groove', font="Ubuntu 11 bold",
                        command=Filtro_Nome, anchor=CENTER)
    Nome_Botao.grid(row=0, column=0, columnspan=2, padx=15, pady=5)

    Nome_search = Entry(tela_filtro, width=15, bg="#d0d1cf", bd=7, fg="#191970",
                        relief="sunken", font="Cambria 15 bold")

    Nome_search.grid(row=1, column=0, columnspan=2)

    Pet_Botao = Button(tela_filtro,
                       text="Pet", bg="#088A08",
                       bd=7, width=19, height=2,
                       relief='groove', font="Ubuntu 11 bold",
                       command=Filtro_Pet, anchor=CENTER)
    Pet_Botao.grid(row=2, column=0, columnspan=2, padx=4, pady=5)

    Pet_search = Entry(tela_filtro, width=15, bg="#d0d1cf", bd=6, fg="#191970",
                       relief="sunken", font="Cambria 15 bold")
    Pet_search.grid(row=3, column=0, columnspan=2)

    Data_Botao = Button(tela_filtro,
                        text="Data", bg="#088A08",
                        bd=7, width=8, height=2,
                        relief='groove', font="Ubuntu 11 bold",
                        command=Filtro_Data, anchor=CENTER)
    Data_Botao.grid(row=4, column=0, padx=2, pady=5)

    Data_search = Entry(tela_filtro, width=5, bg="#d0d1cf", bd=5, fg="#191970",
                        relief="sunken", font="Cambria 15 bold")
    Data_search.grid(row=5, column=0)

    Mes_Botao = Button(tela_filtro,
                       text="|Mês|", bg="#088A08",
                       bd=7, width=8, height=2,
                       relief='groove', font="Ubuntu 11 bold",
                       command=Filtro_Mes, anchor=CENTER)
    Mes_Botao.grid(row=4, column=1, padx=4, pady=5)

    box = ttk.Combobox(tela_filtro, width=12, height=6, values=["Janeiro", "Fevereiro", "Março",
                                                                "Abril", "Maio", "Junho",
                                                                "Julho", "Agosto", "Setembro",
                                                                "Outubro", "Nobembro", "Dezembro"])
    box.current(int(strftime("%m", gmtime())) - 1)
    box.grid(row=5, column=1, padx=1, pady=5)

    autor = Label(tela_filtro, text='Author: F4llen082', font="Arial 7 bold", bg="#141313", fg="#F8F8FF")
    autor.grid(row=6, column=0, pady=6, columnspan=2)

    tela_filtro.mainloop()


Tela_Init()

# Local Onde Está O Arquivo
arquivo = "Local Onde Está o Arquivo"

# Local Onde será enviado
destino = "Pasta one drive para onde será enviada"
shutil.copy(arquivo, destino)

import util
from util import pasta_planilhas
# from tkinter import *
# from tkinter.ttk import * # Temas para o tkinter
import customtkinter

## para transformar em um .exe precisa instalar pyinstaller 
## digitar no cmd: pyinstaller --one nm_script.py
## caso o programa tenha uma interface digitar: pyinstaller --one -w nm_script.py

if __name__ == '__main__':

    janela = customtkinter.CTk()
    janela.title("Vagas V.0.1.1")
    # janela.geometry('400x600')

    texto_orientacao = customtkinter.CTkLabel(janela, text="Escolha o site para pesquisar as vagas!")
    texto_orientacao.grid(column=0, row=0)

    # texto_input = customtkinter.CTkTextbox(janela, height=1, width=200, text="Tipo da vaga")
    texto_input = customtkinter.CTkEntry(janela, height=28, width=200, placeholder_text="Tipo da vaga")
    texto_input.grid(column=0, row=1)


    def search_indeed():
        # Get the input text from the CTkEntry widget
        search_term = texto_input.get()
        resultado = util.get_vagas_indeed(pesquisar_por=search_term)
        output.configure(text=f"Quantidade de vagas Indeed: {resultado.shape[0]}")
        util.criar_planilha(resultado,salvar_como='EXCEL',nm_sheet='Indeed')

    def search_nerdin():
        # Get the input text from the CTkEntry widget
        search_term = texto_input.get()
        resultado = util.get_vagas_nerdin(pesquisar_por=search_term)
        output.configure(text=f"Quantidade de vagas Nerdin: {resultado.shape[0]}")
        util.criar_planilha(resultado,salvar_como='EXCEL',nm_sheet='Nerdin')

    # Creating buttons for Indeed and Nerdin searches
    botao1 = customtkinter.CTkButton(janela, text='Indeed', command=search_indeed)
    botao2 = customtkinter.CTkButton(janela, text='Nerdin', command=search_nerdin)
    botao3 = customtkinter.CTkButton(janela, text='Sair', command=janela.quit)
    output = customtkinter.CTkLabel(janela, text = "")
    

    botao1.grid(column=0, row=2, padx=5, pady=5)
    botao2.grid(column=0, row=3, padx=5, pady=5)
    botao3.grid(column=0, row=4, padx=5, pady=5)
    output.grid(column=0, row=5, padx=5, pady=5)

    janela.mainloop()





    # pesquisar_sites = 0
 
    # while pesquisar_sites != 3:

    #     pesquisar_sites = int(input("""Escolha qual site para pesquisar as vagas:
    # 1 - Indeed
    # 2 - Nerdin
    # 3 - Sair                        
    # """))
    #     if (pesquisar_sites == 3):
    #         print("Saindo...")
    #         break
    #     # nm_vaga = input("Digite qual a vaga: \n")

    #     elif (pesquisar_sites == 1):
    #         nm_vaga = input("Digite qual a vaga: \n")
    #         df_vagas_indeed = util.get_vagas_indeed(pesquisar_por=nm_vaga)
    #         util.criar_planilha(df_vagas_indeed,salvar_como='EXCEL',nm_sheet='Indeed')
            
    #     elif (pesquisar_sites == 2):
    #         nm_vaga = input("Digite qual a vaga: \n")
    #         df_vagas_nerdin = util.get_vagas_nerdin(pesquisar_por=nm_vaga)
    #         util.criar_planilha(df_vagas_nerdin,salvar_como='EXCEL',nm_sheet='Nerdin')
    #     else:
    #         print("Opção inválida. Por favor, tente novamente.")
    #         continue
    
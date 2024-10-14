import util
from util import pasta_planilhas
from tkinter import *
from tkinter.ttk import * # Temas para o tkinter

## para transformar em um .exe precisa instalar pyinstaller 
## digitar no cmd: pyinstaller --one nm_script.py
## caso o programa tenha uma interface digitar: pyinstaller --one -w nm_script.py

if __name__ == '__main__':

    janela = Tk()
    janela.title("Vagas V.0.1.1")
    # janela.geometry('400x600')

    texto_orientacao = Label(janela, text="Escolha o site para pesquisar as vagas!")
    texto_orientacao.grid(column=0, row=0)

    texto_input = Text(janela, height=1, width=20)
    texto_input.grid(column=0, row=1)

    # def printInput(): 
    #     inp = texto_input.get(1.0, "end-1c") 
    #     lbl.config(text = "Pesquisar por: "+inp)
    
    def search_indeed():
        resultado = util.get_vagas_nerdin(pesquisar_por=texto_input.get(1.0, "end-1c"))
        output.config(text = f"Quantidade de vagas Indeed: {resultado.shape[0]}")
    
    def search_nerdin():
        resultado = util.get_vagas_nerdin(pesquisar_por=texto_input.get(1.0, "end-1c"))
        output.config(text = f"Quantidade de vagas Nerdin: {resultado.shape[0]}")
    

    botao1 = Button(janela, text='Indeed', command=search_indeed)
    botao2 = Button(janela, text='Nerdin', command=search_nerdin)
    botao3 = Button(janela, text='Sair', command=janela.quit)
    output = Label(janela, text = "") 

    botao1.grid(column=0, row=2)
    botao2.grid(column=0, row=3)
    botao3.grid(column=0, row=4)
    output.grid(column=0, row=5)

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
    
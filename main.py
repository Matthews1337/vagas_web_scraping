import util


if __name__ == '__main__':
    pesquisar_sites = 0
    while pesquisar_sites != 3:

        pesquisar_sites = int(input("""Escolha qual site para pesquisar as vagas:
    1 - Indeed
    2 - Nerdin
    3 - Sair                        
    """))
        if pesquisar_sites == 3:
            print("Saindo...")
            break

        nm_vaga = input("Digite qual a vaga: \n")
    
        if (pesquisar_sites == 1):
            df_vagas_indeed = util.get_vagas_indeed(pesquisar_por=nm_vaga)
            util.criar_planilha(df_vagas_indeed, path='c:/Users/Matheus/Documents/PROGRAMACAO/PYTHON_ESTUDOS/web_scraping/vagas_jr/planilhas'
                           , salvar_como='EXCEL',nm_sheet='Indeed')
            
        elif (pesquisar_sites == 2):
            df_vagas_nerdin = util.get_vagas_nerdin(pesquisar_por=nm_vaga)
            util.criar_planilha(df_vagas_nerdin, path='c:/Users/Matheus/Documents/PROGRAMACAO/PYTHON_ESTUDOS/web_scraping/vagas_jr/planilhas'
                           , salvar_como='EXCEL',nm_sheet='Nerdin')
        
        else:
            print("Opção inválida. Por favor, tente novamente.")
            continue
        
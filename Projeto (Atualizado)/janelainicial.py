import tkinter as tk
from tkinter import ttk
from login import JanelaCadastro
from tkinter import messagebox
from elementos_tkinter import JanelaPronta, LabelPronta, EntradaTexto, CriarMenus

class JanelaPrincipal(JanelaPronta):
  def __init__(self,nome_da_janela):
        super().__init__(nome_da_janela)
        self.menu_inicio()
        self.iniciar_janela()
  
  def menu_inicio(self):
    def abrir_janela_cadastro():
      self.janela_cadastro = JanelaCadastro('Novo cadastro')
    #criação da barra
    self.menu_bar = CriarMenus(self.principal, tearoff=0)
    self.principal.config(menu=self.menu_bar)

    def Sair():
        resposta_sair = messagebox.askyesno('Fechar','Deseja sair do aplicativo ?')
        if resposta_sair:
           self.principal.quit()
           
    #menu configurações
    self.menu_configuracao = [{'label': 'Sair', 'command' : Sair}]
    self.submenu_opcao = CriarMenus(self.menu_bar, tearoff=0)

    self.submenu_opcao.adiciona_comando_no_menu(self.submenu_opcao,self.menu_configuracao)

    self.menu_bar.adiciona_menu_na_barra('Configurações',self.menu_bar,self.submenu_opcao )

    #menu login
    self.menu_login = [{'label': 'Reallizar novo cadastro', 'command' : abrir_janela_cadastro}]
    self.submenu_login = CriarMenus(self.menu_bar, tearoff=0)

    self.submenu_login.adiciona_comando_no_menu(self.submenu_login,self.menu_login)

    self.menu_bar.adiciona_menu_na_barra('Login',self.menu_bar,self.submenu_login )

if __name__=='__main__':
  JanelaPrincipal('Aplicativo de baixar jogos.')





  
  






    
  
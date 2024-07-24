import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
#objeto menu
class CriarMenus(tk.Menu):
    def __init__(self,master, **kwargs):
        super().__init__(master, **kwargs)
    
    

    def adiciona_menu_na_barra(self,nome_menu, menu_pai : tk.Menu, menu_fllho : tk.Menu):
        menu_pai.add_cascade(label=nome_menu, menu=menu_fllho)

    def adiciona_comando_no_menu(self,menu_que_add_comando : tk.Menu,elementos_do_menu):
        for elements in elementos_do_menu:
            menu_que_add_comando.add_command(label= elements ['label'], command= elements['command'])

#obejto label
class LabelPronta(tk.Label):
    def __init__(self,master, **kwargs):
        super().__init__(master, **kwargs)
        self.configgrid_label

    def configgrid_label(self,linha_label, coluna_label):
        self.grid(row=linha_label, column=coluna_label)

class EntradaTexto(tk.Text):
    def __init__(self,master, **kwargs):
        super().__init__(master, **kwargs)
        self.configgrid_text

    def configgrid_text(self,linha_text, coluna_text):
        self.grid(row=linha_text, column=coluna_text)
        
#objeto janela     
class JanelaPronta:
    def __init__(self, nome_da_janela ):
        self.nome_da_janela = nome_da_janela
        self.principal = tk.Tk()
        self.iniciar_janela
        self.principal.title(self.nome_da_janela)
    
    def iniciar_janela(self):
        self.principal.mainloop()

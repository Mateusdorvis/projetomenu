import tkinter as tk
from tkinter import ttk
from elementos_tkinter import JanelaPronta, LabelPronta, EntradaTexto, CriarMenus

#filhas da classe janela
class JanelaCadastro(JanelaPronta):
    def __init__(self, nome_da_janela ):
        super().__init__(nome_da_janela)
        self.principal.resizable(False, False)
        self.inicio()

    def inicio(self):
        self.label_nome = LabelPronta(self.principal, text='Digite nome ')
        self.label_nome.configgrid_label(0,0)
        self.entrada_nome = EntradaTexto(self.principal, width=20, height=0)
        self.entrada_nome.configgrid_text(0,1)

        self.label_data_de_nascimento = LabelPronta(self.principal, text='Digite sua data de nascimento')

        self.label_data_de_nascimento.configgrid_label(3,0)
        self.entrada_data = EntradaTexto(self.principal, width=20, height=0)
        self.entrada_data.configgrid_text(3,1)

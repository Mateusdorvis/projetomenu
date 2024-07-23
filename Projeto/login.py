
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import os

os.system('cls')
class Novologin:
    def __init__(self):
     self.root = tk.Tk()
     self.root.resizable(False, False)
     self.root.title('Novo Cadastro')
     self.contar_click = 0
     self.NovoCadastro()
     self.root.mainloop()
    
    
     
    def NovoCadastro(self):
      #espaçamento interno e externo padrão
     espacamento_padrao = 5
     #janelas de aviso:
     def JanelaAtencao(mensagem):
         messagebox.showwarning('Atenção', mensagem)
        
     def JanelaInformcao(mensagem2):
         messagebox.showinfo('Informação', mensagem2)
         
     def JanelaQuetao(mensagem3):
         messagebox.askquestion('Pergunta', mensagem3)
     #entradas text e labels
     self.label_nome = tk.Label(self.root, text='Digite seu novo nome de usuário  :')
     self.label_nome.grid(row=0, column=0, pady=espacamento_padrao, padx=espacamento_padrao)
    
     self.entrada_texto__nome = tk.Text(self.root, width=30, height=0)
     self.entrada_texto__nome.grid(row=0, column=1, padx=espacamento_padrao, pady=espacamento_padrao)
     
     
     self.label_datanascimento = tk.Label(self.root, text='Digite sua data de nascimento por completo : (ex. 12/02/2005) :')
     self.label_datanascimento.grid(row=3, column=0, pady=espacamento_padrao, padx=espacamento_padrao)
     
     self.entrada_texto__datanascimento = tk.Text(self.root, width=30, height=0)
     self.entrada_texto__datanascimento.grid(row=3, column=1, padx=espacamento_padrao, pady=espacamento_padrao)
     
     self.label_senha = tk.Label(self.root, text='Digite sua nova senha :')
     self.label_senha.grid(row=6, column=0, pady=espacamento_padrao, padx=espacamento_padrao)
     
     self.entrada_texto__senha = tk.Text(self.root, width=30, height=0)
     self.entrada_texto__senha.grid(row=6, column=1, padx=espacamento_padrao, pady=espacamento_padrao)
     #função que ler caracteres de cada texto.
     #verificando a entrada nome
     def Verificar_texto_nome(event):
        pegue_entrada_texto_nome = self.entrada_texto__nome.get(1.0, tk.END)
        if len(pegue_entrada_texto_nome)<=3 :
            JanelaAtencao(f' Preencha mais pois está {len(pegue_entrada_texto_nome)}!')
     self.entrada_texto__nome.bind('<KeyRelease>', Verificar_texto_nome)
     #verificando a entrada data nascimento
     def Verificar_texto_datanascimento(event):
        pegue_entrada_texto_datanascimento = self.entrada_texto__datanascimento.get(1.0, tk.END)
        if len(pegue_entrada_texto_datanascimento)<=3 :
            JanelaAtencao(f' Preencha mais pois está {len(pegue_entrada_texto_datanascimento)}!')
     self.entrada_texto__datanascimento.bind('<KeyRelease>', Verificar_texto_datanascimento)
     #verificando a entrada senha  
     def Verificar_texto_senha(event):
        pegue_entrada_texto_senha = self.entrada_texto__senha.get(1.0, tk.END)
        if len(pegue_entrada_texto_senha)<=3 :
            JanelaAtencao(f' Preencha mais pois está {len(pegue_entrada_texto_senha)}!')
     self.entrada_texto__senha.bind('<KeyRelease>', Verificar_texto_senha)
     
     #função de enviar botão
     def EnviarCadastro(event):
       
        self.contar_click+=1
         
        pegue_entrada_texto_nome = self.entrada_texto__nome.get(1.0, tk.END)
         
        pegue_entrada_texto_datanascimento = self.entrada_texto__datanascimento.get(1.0, tk.END)
         
        pegue_entrada_texto_senha = self.entrada_texto__senha.get(1.0, tk.END)
        
        #Checa se todos os campos foram preenchidos
        if len(pegue_entrada_texto_senha)==1 or len(pegue_entrada_texto_senha)==1 or len(pegue_entrada_texto_datanascimento):
             JanelaAtencao('Os campos estão vazios ! Preencha por favor !')
        
       
        else:
            label_button = tk.Label(self.root, text='Enviado')
            label_button.grid(row=12, column=0)
             
        pergunta = messagebox.askquestion('Pergunta', 'Deseja logar agora ?')
        if pergunta=='yes':
               Cadastro()
        
         
        
            
        
        
        return True
             
             

         
     #Botão de enviar cadastro
     self.button_enviar_cadastro = tk.Button(self.root, text='Enviar Cadastro')
     self.button_enviar_cadastro.grid(row=9, column=0, pady=espacamento_padrao, padx=espacamento_padrao)
     self.button_enviar_cadastro.bind('<Button-1>', EnviarCadastro)
     
     
     
 
        
        
     
    
    
class Cadastro:
    def __init__(self):
     self.root = tk.Tk()
     self.root.resizable(False, False)
     self.root.title('Cadastro')
     self.contar_click = 0
     self.Cadastro()
     self.root.mainloop()
    
    
     
    def Cadastro(self):
     espacamento_padrao = 5
     self.label_nome = tk.Label(self.root, text='Digite seu nome de usuário  cadastrado :')
     self.label_nome.grid(row=0, column=0, pady=espacamento_padrao, padx=espacamento_padrao)
    
     self.entrada_texto__nome = tk.Text(self.root, width=30, height=0)
     self.entrada_texto__nome.grid(row=0, column=1, padx=espacamento_padrao, pady=espacamento_padrao)
     
     self.label_senha = tk.Label(self.root, text='Digite sua senha :')
     self.label_senha.grid(row=1, column=0, pady=espacamento_padrao, padx=espacamento_padrao)
     
     self.entrada_texto__senha = tk.Text(self.root, width=30, height=0)
     self.entrada_texto__senha.grid(row=1, column=1, padx=espacamento_padrao, pady=espacamento_padrao)
     
     
     
     

 
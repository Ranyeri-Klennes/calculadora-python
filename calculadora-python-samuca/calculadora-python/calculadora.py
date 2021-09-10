# Importando a lib do interpretador(janela visual) em Python:
from tkinter import *
from tkinter import ttk

# PALETA DE CORES
cor_escura = '#32303b'
cor_detalhes = '#8460f0'
cor_bg = '#d3d0db'

# Layout da janela(interpretado):
janela =Tk()
janela.title('Calculadora')
janela.geometry('235x318')#tamanho da janela
janela.config

# DIVISÃO DAS PARTES (VISOR E TECLADO)
frame_tela = Frame(janela, width=235,height=50)
frame_tela.grid(row=0,column=0)

# Menu da janela
janela.mainloop()
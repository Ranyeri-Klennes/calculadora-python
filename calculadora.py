from tkinter import *
from tkinter import ttk
from tkinter import font
from tkinter.font import BOLD

# CORES DA CALCULADORA
cor_bg = '#dfd5e8'
cor_visor = '#0d0b0f'
cor_teclado = '#b8b8b8'
cor_numeros = '#7a00f5'

# CONFIGURAÇÃO DA JANELA
janela = Tk()
janela.title('Calculadora')
janela.geometry('235x318')
janela.config(bg=cor_bg)

# TELA
frame_tela = Frame(janela, width=235, height=50, bg=cor_visor)
frame_tela.grid(row=0, column=0)

# TECLADO
frame_teclado = Frame(janela, width=235, height=268, bg=cor_bg)
frame_teclado.grid(row=1, column=0)

# BOTÕES
b1 = Button(frame_teclado, text='C', width=11, height=2, font=('Ivy 13q bold'), relief=(RAISED))
b1.place(x=0, y=0)
b2 = Button(frame_teclado, text='%', width=5, height=2)
b2.place(x=90, y=0)
b3 = Button(frame_teclado, text='/', width=5, height=2, bg=cor_teclado, fg=cor_numeros)
b3.place(x=138, y=0)

# VISUALIZAR A CALCULADORA
janela.mainloop()
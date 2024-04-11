from tkinter import *
from random import randint
#-------------------------------------------------------------
root = Tk()
#Dimensões da tela
comp = root.winfo_screenwidth()
alt = root.winfo_screenheight()
#Dimensões da aplicação
compR = 750
altR = 450
#Posicionamento da aplicação na tela
inf1 = comp/2 - compR/2 - 200
inf2 = alt/2 - altR/2 - 100
#Geometry
root.geometry('%dx%d+%d+%d'%(compR,altR,inf1,inf2))
#-------------------------------------------------------------
#Algorítmo
#Comandos
respostas = ()

class Exercícios(Frame):
    def __init__(self,p):
        for c in SPb.get():
            super()__init__()
            self['height'] - 360
            self['width'] = 200
            self['bd'] = 3
            self['relief'] = SOLID
            

            

    def soma():
        a = randint(1,99)
        b = randint(1,99)
        res = a+b
        res2 = a
    def mult():
        a = randint(1,9)
        b = randint(1,9)
        res = a*b
        res2 = a
    def sub():
        while True:
            a = randint(1,99)
            b = randint(1,99)
            res = a-b
            if res > 0:
                break
        res2 = a
    def div():
        while True:
            a = randint(1,99)
            b = randint(1,9)
            res = a/b
            if res in range(1,99):
                break
        res2 = a
#Layout e funcionalidades
FrameOpc = Frame(root)
variavel = IntVar()
RBsom = Radiobutton(FrameOpc, text='Soma',font= ' 12',variable= variavel, value=1).grid(row= 0,column= 0)
RBmul = Radiobutton(FrameOpc, text='Multiplicação',font= ' 12',variable= variavel, value=2).grid(row= 0,column= 1)
RBsub = Radiobutton(FrameOpc, text='Subtração',font= ' 12',variable= variavel, value=3).grid(row= 0,column= 2)
RBdiv = Radiobutton(FrameOpc, text='Divisão',font= ' 12',variable= variavel, value=4).grid(row= 0,column= 3)
FrameExec = Frame(root)
BExe = Button(FrameExec, text='Executar', relief=SOLID).grid(row=1,column=0)
SPb= Spinbox(FrameExec, from_=1, to=12).grid(row=1, column=1)
FrameExer = Frame(root)


#Grids
FrameOpc.grid()
FrameExec.grid()
FrameExer.grid()






root.mainloop()
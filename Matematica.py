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
#Variáveis
FrameOpc = Frame(root)
variavel = StringVar()
FrameExec = Frame(root)
SPb_v = IntVar()
SPb_v.set(value=1)
FrameExer = Frame(root)
#Comandos
respostas = ()

class Exercícios():
            
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
class ExeFrame(Frame):
    def __init__(self,p):
        super().__init__()
        self['height'] - 360
        self['width'] = 200
        self['bd'] = 3
        self['relief'] = SOLID
def linkbotao():
    nume = SPb_v.get()
    opc = variavel.get()
    for c in range(nume):
        Lab1 = Label(FrameExer, text='ok')
        Lab1.grid(row = c, column = c+1)
    
            
            
#Layout e funcionalidades

RBsom = Radiobutton(FrameOpc, text='Soma',font= '14',variable= variavel, value='soma')
RBsom.grid(row= 0,column= 0)
RBmul = Radiobutton(FrameOpc, text='Multiplicação',font= '14',variable= variavel, value='multiplicacao')
RBmul.grid(row= 0,column= 1)
RBsub = Radiobutton(FrameOpc, text='Subtração',font= '14',variable= variavel, value='subtracao')
RBsub.grid(row= 0,column= 2)
RBdiv = Radiobutton(FrameOpc, text='Divisão',font= '14',variable= variavel, value='divisao')
RBdiv.grid(row= 0,column= 3)
RBsom.select()

BExe = Button(FrameExec, text='Executar', relief=SOLID, command=linkbotao).grid(row=1,column=0)

SPb = Spinbox(FrameExec, from_=1, to=12, textvariable=SPb_v)
SPb.grid(row=1, column=1)



#Grids
FrameOpc.pack()
FrameExec.pack()
FrameExer.pack()






root.mainloop()
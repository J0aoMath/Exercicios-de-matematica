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
#
class ExeFrame(Frame):
    def __init__(self,p):
        super().__init__()
        self['bd'] = 2
        self['padx'] = 2
        self['pady'] = 2
        self['relief'] = SOLID

#Variáveis
FrameOpc = Frame(root)
variavel = StringVar()
FrameExec = Frame(root)
SPb_v = IntVar()
SPb_v.set(value=1)
FrameExer = ExeFrame(root)
FrameRespet = Frame(root)
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

class botoes():
    def linkbotao():
        nume = SPb_v.get()
        opc = variavel.get()
        for c in range(nume):
            Lab1 = Label(FrameExer,
                        text='ok',font='Arial 16',
                        height=2,
                        width=8,
                        bd=2,                                          
                        relief=SOLID)
            Resp = Entry(FrameExer)

            
            if c <= 2:
                Lab1.grid(row = 0, column = c+1)
                Resp.grid(row = 1, column = c+1)
            elif 2 < c <= 5:
                Lab1.grid(row = 2, column = c-2)
                Resp.grid(row = 3, column = c-2)
            elif 5 < c <= 8:
                Lab1.grid(row = 4, column = c - 5)
                Resp.grid(row = 5, column = c - 5)
            elif 8 < c <= 11:
                Lab1.grid(row = 6, column = c - 8)
                Resp.grid(row = 7, column = c - 8)
            Lab1.grid_configure(padx=4, pady=3)
            Resp.grid_configure(padx=4, pady=3)
            BRes = Button(FrameRespet,text='Responder').grid(row=0,column=0)
            BReset = Button(FrameRespet, text='Reset').grid(row=0, column=1)
    def responder():
        a = 2
    def reset():
        a = 3
            
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

BExe = Button(FrameExec, text='Executar', relief=SOLID, command=botoes.linkbotao).grid(row=1,column=0)

SPb = Spinbox(FrameExec, from_=1, to=12, textvariable=SPb_v)
SPb.grid(row=1, column=1)



#Grids
FrameOpc.pack()
FrameExec.pack()
FrameExer.pack()
FrameRespet.pack()




root.mainloop()
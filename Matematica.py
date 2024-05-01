from tkinter import *
from random import randint
#-------------------------------------------------------------
root = Tk()
#Dimensões da tela
comp = root.winfo_screenwidth()
alt = root.winfo_screenheight()
#Dimensões da aplicação
compR = 750
altR = 525
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
Equacoes = []
Respostas = []
limitador = 59
tempo = '00:00'
contar = False
contador = 0
Cronos = Label(FrameExec, text=tempo,bg='#ffffcc', font='14', relief=SUNKEN)
#Funcoes
def cronometro():
    global tempo
    global contar
    global contador
    if contar:
        temporaria = str(tempo)
        m,s = map(int,temporaria.split(':'))
        m = int(m)
        s = int(contador)
        if (s >= limitador):
            contador = 0
            m += 1
        s = str(0)+str(s)
        m = str(0)+str(m)
        temporaria = str(m[-2:])+':'+str(s[-2:])
        tempo = temporaria
        Cronos.after(1000,cronometro)
        contador += 1
        Cronos['text']=temporaria
        tempo = temporaria

class Exercicios():
            
    def soma():
        a = randint(1,99)
        b = randint(1,99)
        res = a+b
        Equacoes.append([a,'+',b])
        Respostas.append(res)
    def mult():
        a = randint(1,9)
        b = randint(1,9)
        res = a*b
        Equacoes.append([a,'x',b])
        Respostas.append(res)
    def sub():
        while True:
            a = randint(1,99)
            b = randint(1,99)
            res = a-b
            if res > 0:
                break
        Equacoes.append([a,'-',b])
        Respostas.append(res)
    def div():
        while True:
            a = randint(1,99)
            b = randint(1,9)
            c = randint(1,3)
            d = randint(1,3)
            res = a/b
            if res in range(1,99):
                if d == 2 and b == 2:
                    break
                if c == 1 and b == 1 and d == 1:
                    break
                if b != 1 and b != 2:
                    break
        Equacoes.append([a,'/',b])
        Respostas.append(int(res))

class botoes():

    def linkbotao():
        global contar
        contar = True
        cronometro()
        #Entries
        ent1 = IntVar()
        entr1 = Entry(FrameExer, textvariable=ent1)
        ent2 = IntVar()
        entr2 = Entry(FrameExer, textvariable=ent2)
        ent3 = IntVar()
        entr3 = Entry(FrameExer, textvariable=ent3)
        ent4 = IntVar()
        entr4 = Entry(FrameExer, textvariable=ent4)
        ent5 = IntVar()
        entr5 = Entry(FrameExer, textvariable=ent5)
        ent6 = IntVar()
        entr6 = Entry(FrameExer, textvariable=ent6)
        ent7 = IntVar()
        entr7 = Entry(FrameExer, textvariable=ent7)
        ent8 = IntVar()
        entr8 = Entry(FrameExer, textvariable=ent8)
        ent9 = IntVar()
        entr9= Entry(FrameExer, textvariable=ent9)
        ent10 = IntVar()
        entr10 = Entry(FrameExer, textvariable=ent10)
        ent11 = IntVar()
        entr11 = Entry(FrameExer, textvariable=ent11)
        ent12 = IntVar()
        entr12 = Entry(FrameExer, textvariable=ent12)
        nume = SPb_v.get()
        opc = variavel.get()
        BExe["state"] = "disabled"
        Entries = []
        def gridentry():
            nume1= int(SPb_v.get())
            if nume1 >= 1: entr1.grid(row = 1, column = 1,padx=4, pady=3)
            if nume1 >= 2: entr2.grid(row = 1, column = 2,padx=4, pady=3)
            if nume1 >= 3: entr3.grid(row = 1, column = 3,padx=4, pady=3)
            if nume1 >= 4: entr4.grid(row = 4, column = 1,padx=4, pady=3)
            if nume1 >= 5: entr5.grid(row = 4, column = 2,padx=4, pady=3)
            if nume1 >= 6: entr6.grid(row = 4, column = 3,padx=4, pady=3)
            if nume1 >= 7: entr7.grid(row = 7, column = 1,padx=4, pady=3)
            if nume1 >= 8: entr8.grid(row = 7, column = 2,padx=4, pady=3)
            if nume1 >= 9: entr9.grid(row = 7, column = 3,padx=4, pady=3)
            if nume1 >= 10: entr10.grid(row = 10, column = 1,padx=4, pady=3)
            if nume1 >= 11: entr11.grid(row = 10, column = 2,padx=4, pady=3)
            if nume1 >= 12: entr12.grid(row = 10, column = 3,padx=4, pady=3)
        

        def resetbutton():
            global contador
            global tempo
            global contador
            global contar
            contar = False
            Cronos['bg'] = '#ffffcc'
            contador = 0
            tempo = '00:00'
            for widget in FrameExer.winfo_children():
                widget.destroy()
            for widget in FrameRespet.winfo_children():
                widget.destroy()
            Respostas.clear()
            Entries.clear()
            Equacoes.clear()
            BExe['state'] = 'normal'

        def responder():
            global contar
            contar=False
            Cronos['bg'] = '#66ff66'
            Entries = [ent1.get(),ent2.get(),ent3.get(),ent4.get(),ent5.get(),ent6.get(),
                       ent7.get(),ent8.get(),ent9.get(),ent10.get(),ent11.get(),ent12.get()]
            
            total = 0
            for c in range(nume):
                if c <= 2:
                    if Entries[c] == Respostas[c]:
                        Label(FrameExer,text='Correto!',bg='#66ff66').grid(row=2,column=c+1)
                        total += 1
                    else:
                        Label(FrameExer,text=f'Errado! O certo: {Respostas[c]}.',bg='#ff1a1a').grid(row=2,column=c+1)
                elif c <= 5:
                    if Entries[c] == Respostas[c]:
                        Label(FrameExer,text='Correto!',bg='#66ff66').grid(row=5,column=c-2)
                        total += 1
                    else:
                        Label(FrameExer,text=f'Errado! O certo: {Respostas[c]}.',bg='#ff1a1a').grid(row=5,column=c-2)
                elif c <= 8:
                    if Entries[c] == Respostas[c]:
                        Label(FrameExer,text='Correto!',bg='#66ff66').grid(row=8,column=c-5)
                        total += 1
                    else:
                        Label(FrameExer,text=f'Errado! O certo: {Respostas[c]}.',bg='#ff1a1a').grid(row=8,column=c-5)
                elif c <= 11:
                    if Entries[c] == Respostas[c]:
                        Label(FrameExer,text='Correto!',bg='#66ff66').grid(row=11,column=c-8)
                        total += 1
                    else:
                        Label(FrameExer,text=f'Errado! O certo: {Respostas[c]}.',bg='#ff1a1a').grid(row=11,column=c-8)
            if total >= 1 and total < 12:
                Label(FrameRespet, text=f'Total de acertos: {total}.',font='11').grid(row=0,column=2)
            if total == 12:
                Label(FrameRespet, text='Parabéns! Você acertou todas! :D',font='11').grid(row=0,column=2)
            if total == 0:
                Label(FrameRespet, text='Total de acertos: Nenhum. ;(',font='11').grid(row=0,column=2,padx=4)
        if opc == 'soma':
            for c in range(nume):
                Exercicios.soma()
        if opc == 'multiplicacao':
            for c in range(nume):
                Exercicios.mult()
        if opc == 'subtracao':
            for c in range(nume):
                Exercicios.sub()
        if opc == 'divisao':
            for c in range(nume):
                Exercicios.div()
        for c in range(nume):
            Lab1 = Label(FrameExer,
                            text='ok', font='Arial 16',
                            height=2,
                            width=8,
                            bd=2,                                          
                            relief=SOLID)
            if c <= 2:
                Lab1.grid(row = 0, column = c+1)
                Lab1.config(text=Equacoes[c])
            elif 2 < c <= 5:
                Lab1.grid(row = 3, column = c-2)
                Lab1.config(text=Equacoes[c])
            elif 5 < c <= 8:
                Lab1.grid(row = 6, column = c - 5)
                Lab1.config(text=Equacoes[c])
            elif 8 < c <= 11:
                Lab1.grid(row = 9, column = c - 8)
                Lab1.config(text=Equacoes[c])
            gridentry()
            Lab1.grid_configure(padx=4, pady=3)

            Button(FrameRespet,text='Responder', command=responder).grid(row=0,column=0,padx=1,pady=3)
            Button(FrameRespet, text='Reiniciar',command=resetbutton).grid(row=0, column=1,padx=1,pady=5)
        Cronos.grid(row=1,column=0, ipadx=8, padx=16)
     
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

BExe = Button(FrameExec, text='Executar', relief=RAISED, command=botoes.linkbotao)
BExe.grid(row=1,column=1,padx=2)

SPb = Spinbox(FrameExec, from_=1, to=12, textvariable=SPb_v, state='readonly')
SPb.grid(row=1, column=2)

#packs
FrameOpc.pack()
FrameExec.pack()
FrameExer.pack()
FrameRespet.pack()

root.mainloop()
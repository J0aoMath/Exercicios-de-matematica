from tkinter import *
from pyautogui import *
from time import sleep
'''
339,63 - soma
528,66 - subtraçao
446,66 - mult
638,68 - div
623,86 - spinbox
469,92 - executar
384,180 - Entry
450,472 - responder
400,553 - reiniciar
'''
menu = Tk()
tela_height = menu.winfo_screenheight()
tela_width = menu.winfo_screenwidth()
menu_height = 100
menu_width = 200
posy = tela_height / 2 - menu_height / 2
posx = tela_width / 2 - menu_width / 2 + 300
menu.geometry('%dx%d+%d+%d'%(menu_width,menu_height,posx,posy))

def Execute():
    sleep(2)
    moveTo(x =339,y=63,duration=1)
    click()
    moveTo(x=528,y=66,duration=0.75)
    click()
    moveTo(x=446,y=66,duration=0.75)
    click()
    moveTo(x=638,y=68,duration=0.75)
    click()
    moveTo(x=623,y=86,duration=0.75)
    click(clicks=11,interval=0.25)
    moveTo(x=469,y=92,duration=0.75)
    click()
    moveTo(x=384,y=180,duration=0.75)
    doubleClick()
    for c in range (1,12):
        sleep(0.33)
        hotkey('tab')
    moveTo(x=450,y=472,duration=0.5)
    click()
    sleep(3)
    moveTo(x=400,y=553,duration=0.33)
    click()

frame_ex = Frame(menu)
frame_ex.pack(padx=0, pady=20)
btn = Button(frame_ex,text='execute', relief=RAISED, command=Execute)
btn.pack()
menu.mainloop()
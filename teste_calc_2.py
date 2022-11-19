from tkinter import *
atual = ""
def apagar():
    global atual
    atual = ""
    valor_visor.set(atual)
    



def calcular(numero):
    global valor_visor
    global atual
    atual = str(atual) + str(numero)
    valor_visor.set(atual)
    
    


def resultado():
    global atual

    print(atual)
    atual = (eval(atual))
    valor_visor.set(atual)

def apagar_ultimo_digito():
    global atual
    atual = atual[:-1]
    valor_visor.set(atual)
    
    


root = Tk()

root.geometry("305x475")
root.configure(background="#DCDCDC")
root.resizable(False, False)
root.title("Calculadora")

valor_visor = StringVar()

label_visor = Label(root, textvariable=valor_visor, anchor="e", font="Ivy 22")
label_visor.place(x=5, y=20, width=295, height=70)

bt_c = Button(root, text="C", command=apagar, font="Ivy 22").place(x= 5, y=100, width=70, height=70)
bt_del = Button(root, text="DEL", command=apagar_ultimo_digito, font="Ivy 22").place(x= 80, y=100, width=70, height=70)
bt_elevado = Button(root, text="**", command=lambda:calcular("**"), font="Ivy 22").place(x= 155, y=100, width=70, height=70)
bt_dividir = Button(root, text="/", background="#355473", foreground= "white", command=lambda:calcular("/"), font="Ivy 22").place(x= 230, y=100, width=70, height=70)

bt_7 = Button(root, text="7", command=lambda:calcular(7), font="Ivy 22").place(x= 5, y=175, width=70, height=70)
bt_8 = Button(root, text="8", command=lambda:calcular(8), font="Ivy 22").place(x= 80, y=175, width=70, height=70)
bt_9 = Button(root, text="9", command=lambda:calcular(9), font="Ivy 22").place(x= 155, y=175, width=70, height=70)
bt_vezes = Button(root, text="*", background="#355473", foreground= "white", command=lambda:calcular("*"), font="Ivy 22").place(x= 230, y=175, width=70, height=70)

bt_4 = Button(root, text="4", command=lambda:calcular(4), font="Ivy 22").place(x= 5, y=250, width=70, height=70)
bt_5 = Button(root, text="5", command=lambda:calcular(5), font="Ivy 22").place(x= 80, y=250, width=70, height=70)
bt_6 = Button(root, text="6", command=lambda:calcular(6), font="Ivy 22").place(x= 155, y=250, width=70, height=70)
bt_menos = Button(root, text="-", background="#355473", foreground= "white", command=lambda:calcular("-"), font="Ivy 22").place(x= 230, y=250, width=70, height=70)

bt_1 = Button(root, text="1", command=lambda:calcular(1), font="Ivy 22").place(x= 5, y=325, width=70, height=70)
bt_2 = Button(root, text="2", command=lambda:calcular(2), font="Ivy 22").place(x= 80, y=325, width=70, height=70)
bt_3 = Button(root, text="3", command=lambda:calcular(3), font="Ivy 22").place(x= 155, y=325, width=70, height=70)
bt_mais = Button(root, text="+",background="#355473", foreground= "white", command=lambda:(calcular("+")), font="Ivy 22").place(x= 230, y=325, width=70, height=70)

bt_0 = Button(root, text="0", command=lambda:calcular(0), font="Ivy 22").place(x= 5, y=400, width=145, height=70)
bt_ponto = Button(root, text=".", command=lambda:calcular("."), font="Ivy 22").place(x= 155, y=400, width=70, height=70)
bt_igual = Button(root, text="=",background="#355473", foreground= "white", command=resultado, font="Ivy 22").place(x= 230, y=400, width=70, height=70)




root.mainloop()
from tkinter import*
#Janela:
Janela = Tk()
LT = Janela.winfo_screenwidth()
AT = Janela.winfo_screenheight()
l = 420
a = 420
x = int(LT/2 - l/2)
y = int(AT/2 - a/2)
Janela.geometry(f"{l}x{a}+{x}+{y}")
Janela.mainloop()
#*******************************************

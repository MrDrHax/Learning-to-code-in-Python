# esta es una prueba, pero si sirve estaremos corriendo en moneys

# okay aqui van las notas...
# tk.Label(master, text="First Name").grid(row=0)
# tk es la base...
# Label crea texto, master es en que superficie se escribe, y text es el texto que incluye. 
# .grid es para darle el lugar de linea (0 va primero, 1 despues y asi) al parecer se escribe de izquierda a derecha

# txtFild = tk.Entry(master).grid(row=0, column=1)
# Entry significa que es un coso donde metes 1 linea de texto (solamente)
# Nuevamente .grid es para alineacion. column es para darle la posicion en el x axis (que venga despues del texto)
# Puedes utilizar txtField.get() para sacar el str de lo que hicieron input
# si quieres borrar el input, usa: .delete(0, tk.END) (0 siendo la cantidad de digitos que quedan, tk,END es donde termina, estilo de donde a donde borra. tk.End es el final)
# para insertar un default, .insert(10, "Miller") (no se que es el 10 lol)

# tk.Button(master, 
          # text='Show', command=show_entry_fields).grid(row=3, 
          #                                              column=1, 
          #                                              sticky=tk.W, 
          #                                              pady=4)
# para hacer un botton. no sirve como objeto al parecer?
# text es el lugar donde pones lo que sale en el boton (su texto)
# command es donde pones el comando que corra (un def)

# master.mainloop() hace el mainloop de SOLAMENTE la pantalla master, en caso de querer varias pantallas, usar tk.mainloop()

# para usar ScrolledText tienes que usar from tkinter.scrolledtext import ScrolledText
# scrolled text es un cuadro de texto que puedes scrollear

import tkinter as tk
from tkinter.scrolledtext import ScrolledText

class tkinterMain():
    def __init__(self, end, run, change, cashtostr, saveIntoChash):
        
        self.runCode = run
        self.changeId = change
        self.cashToString = cashtostr
        self.updateCash = saveIntoChash

        self.commentString = ''

        self.tkInterscreen = tk.Tk()

        self.tkInterscreen.protocol("WM_DELETE_WINDOW", end)

        self.instructionset = ScrolledText(self.tkInterscreen, height = 10)
        self.instructionset.grid(row=0, column=1, columnspan=3)

        self.editor = ScrolledText(self.tkInterscreen)
        self.editor.grid(row=1, column=1, sticky="news", columnspan=3)

        self.nextButton = tk.Button(self.tkInterscreen, text = 'Next', command = self.changeTo1 )
        self.previousButton = tk.Button(self.tkInterscreen, text = 'Previous', command = self.changeToPrevious )
        self.playButton = tk.Button(self.tkInterscreen, text = 'Run!', command = self.runThemCodes )
        self.resetButton = tk.Button(self.tkInterscreen, text = 'Reset', command = self.changeTo0 )
        self.changeLvlButton = tk.Button(self.tkInterscreen, text = 'Change amount', command = self.getAndChangeToInput)
        self.IDchooser = tk.Entry(self.tkInterscreen)

        self.nextButton.grid(row=3, column=1, sticky="w")
        self.previousButton.grid(row=3, column=0, sticky="e")
        self.playButton.grid(row=3, column=2, sticky="e")

        self.resetButton.grid(row=4, column=2, sticky="e")
        self.changeLvlButton.grid(row=4, column=0, sticky="e")

        self.IDchooser.grid(row=4, column=1, sticky="w")
        self.IDchooser.insert(10, "+ or - amount")

        self.tkInterscreen.columnconfigure(0, weight=1)
        self.tkInterscreen.columnconfigure(1, weight=1)

        self.loadFromCash()

        #self.tkInterscreen.after(10, self.outsideLoop())

        #self.tkInterscreen.mainloop()

    def changeTo1(self):
        self.saveToChash()

        print('changing to:', 1)
        try:
            self.changeId()
        except Exception as e:
            print('error changing to ID from tkinter', e)

        self.loadFromCash()
    
    def changeToPrevious(self):
        self.saveToChash()

        print('changing to:', -1)
        try:
            self.changeId(-1)
        except Exception as e:
            print('error changing to ID from tkinter', e)

        self.loadFromCash()

    def changeTo0(self):
        self.saveToChash()

        print('changing to:', 0)
        try:
            self.changeId(0)
        except Exception as e:
            print('error changing to ID from tkinter', e)

    def updateSelf(self):
        self.tkInterscreen.update()

    def getAndChangeToInput(self):
        self.saveToChash()

        try:
            toChange = int(self.IDchooser.get())
            self.changeId(toChange)
            self.IDchooser.delete(0, tk.END)
            self.IDchooser.insert(10, "+ or - amount")
        except:
            print('enter only numbers please...')

        self.loadFromCash()

    def saveToChash(self):
        # construct from both comment and get text
        toSend = self.commentString + self.editor.get('0.0', tk.END)

        # send to cash
        self.updateCash(toSend)

    def loadFromCash(self):
        self.instructionset.configure(state='normal')
        self.editor.delete('0.0', tk.END)
        self.instructionset.delete('0.0', tk.END)

        returnation = self.cashToString()

        commenting = False
        commentStr = []
        editStr = []
        for i in returnation:
            if i == "'''":
                if commenting:
                    commenting = False
                    commentStr.append(i)
                else:
                    commenting = True
                    commentStr.append(i)
            
            elif commenting:
                commentStr.append(i)
            else:
                editStr.append(i)

        outCommentStr = ''
        for i in commentStr:
            outCommentStr = outCommentStr + i  + '\n'

        outEditStr = ''
        for i in editStr:
            outEditStr = outEditStr + i  + '\n'

        self.instructionset.insert('0.0', outCommentStr)
        self.commentString = outCommentStr

        self.editor.insert('0.0', outEditStr)

        self.instructionset.configure(state='disabled')

    def runThemCodes(self):
        print('running code!')
        self.saveToChash()
        self.runCode(False, self.editor.get('0.0', tk.END))

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

def show_entry_fields():
    print(text.get(index1="0.0",index2=tk.END))

master = tk.Tk()

text = ScrolledText(master)
text.grid(row=1)# tiene que estar despues para que pueda acceder al objeto text

tk.Button(master, 
          text='previous', 
          command=master.quit).grid(row=3, 
                                    column=0, 
                                    sticky=tk.W, 
                                    pady=4)
tk.Button(master, 
          text='next', 
          command=master.quit).grid(row=3, 
                                    column=0, 
                                    sticky=tk.W, 
                                    pady=30)
tk.Button(master, 
          text='Play', command=show_entry_fields).grid(row=3, 
                                                       column=0, 
                                                       sticky=tk.E, 
                                                       pady=4)

tk.mainloop()

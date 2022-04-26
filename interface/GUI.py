from tkinter import *
from tkinter import ttk
import tkinter as tk
from click import command
from analisis.lexico import Analisisis_Lexico

BG_GRAY = "#ABB2B9"
BG_COLOR = "#36648B"
TEXT_COLOR = "#EAECEE"
CONT_COLOR = "#A0522D"

FONT = "Helvetica 14"
FONT_BOLD = "Helvetica 13 bold"


class GUI():
    
    def __init__(self) -> None:
        self.raiz = Tk()
        self._setup_main_window()
    
    def run(self) -> None:
        self.raiz.mainloop()
        
    def _setup_main_window(self):
        self.raiz.title("La Liga Bot")
        self.raiz.geometry("750x500")
        self.raiz.rowconfigure(0, weight=1)
        self.raiz.columnconfigure(0, weight=1)
        
        mainframe = ttk.Frame(self.raiz)
        mainframe.grid(row=0, column=0, sticky=NSEW)
        mainframe.rowconfigure(1, weight=1)
        #mainframe.columnconfigure(0, weight=1)
        
        #?Cuerpo
        bodyFrame = ttk.Frame(mainframe)
        bodyFrame.grid(row=1, column=1, sticky=NSEW)
        bodyFrame.columnconfigure(1, weight=2)
        bodyFrame.rowconfigure(1, weight=1)

        
        # TODO: Cuerpo
        #! Caja de Texto 
        self.bodyText = tk.Text(bodyFrame, width=20, height=2, bg=BG_GRAY, fg=TEXT_COLOR, font= FONT, padx=5,pady=5)
        self.bodyText.grid(row=1, column=1, sticky=NSEW)
        self.bodyText.configure(cursor="arrow", state=DISABLED)
        
        # Pie de pagina
        footFrame = ttk.Frame(mainframe, borderwidth=5, relief="ridge")
        footFrame.grid(row=2, column=1, sticky=EW)
        footFrame.columnconfigure(1, weight=1)
        
        self.msgEntry = tk.Entry(footFrame, bg="#2C3E50",
                                 fg=TEXT_COLOR, font=FONT)
        self.msgEntry.place(relwidth=0.74, relheight=0.06,
                            rely=0.008, relx=0.011)
        self.msgEntry.focus()
        self.msgEntry.bind("<Return>")
        self.msgEntry.grid(row=1, column=1, sticky=NSEW)

        # Pie send button
        sendButton = tk.Button(footFrame, text="Enviar", font=FONT_BOLD, bg=BG_GRAY,
                               command=lambda: self._on_enter_pressed(None))
        sendButton.grid(row=1, column=2, sticky=NSEW)

    def _on_enter_pressed(self, event):
        msg = self.msgEntry.get()
        self._insert_message(msg, "Intro")
        
    def _insert_message(self, msg, sender):
        if not msg:
            return

        self.msgEntry.delete(0, END)
        msg1 = f"{sender}: {msg}\n\n"
        self.bodyText.configure(state=NORMAL)
        self.bodyText.insert(END, msg1)
        self.bodyText.configure(state=DISABLED)

        if msg == 'ADIOS':
            respuesta = 'ADIOS'
            bot_name = "Julián"
            msg2 = f"{bot_name}: {respuesta}\n\n"
            self.bodyText.configure(state=NORMAL)
            self.bodyText.insert(END, msg2)
            self.bodyText.configure(state=DISABLED)

            self.bodyText.see(END)
        else:
            bot_name = "Julián"
            respuesta = self.readInfo(msg)
            msg2 = f"{bot_name}: {respuesta}\n\n"
            self.bodyText.configure(state=NORMAL)
            self.bodyText.insert(END, msg2)
            self.bodyText.configure(state=DISABLED)

            self.bodyText.see(END)

        if respuesta == 'ADIOS':
            self.raiz.destroy()

    def readInfo(self,msg):
        if msg != '':
            self.analisis_lex = Analisisis_Lexico()
            cadena = self.analisis_lex.entrada(msg)
            return cadena
import tkinter as tk
from tkinter import ttk
from googletrans import Translator

class TranslatorApp:
    def _init_(self, master):
        self.master = master
        self.master.title("Language Translator")
        self.master.geometry("400x200")
        
        self.langs=["English","French"]
        self.lang_codes={"English":"en","French":"fr"}
        
        self.label1=ttk.Label(self.master,text="Enter text to translate:")
        self.label1.grid(row=0,column=0,padx=5,pady=5)
        
        self.textbox1=tk.Text(self.master,height=4)
        self.textbox1.grid(row=1,column=0,padx=5,pady=5)
        
        self.label2=ttk.Label(self.master,text="Choose source lang")
        self.label2.grid(row=2,column=0,padx=5,pady=5)
        
        self.source_lang=ttk.Combobox(self.master,values=self.langs,state="readonly")
        self.source_lang.current(0)
        self.source_lang.grid(row=3,column=0,padx=5,pady=5)
        
        self.label3=ttk.Label(self.master,text="Choose dest lang")
        self.label3.grid(row=4,column=0,padx=5,pady=5)
        
        self.dest_lang=ttk.Combobox(self.master,values=self.langs,state="readonly")
        self.dest_lang.current(1)
        self.dest_lang.grid(row=5,column=0,padx=5,pady=5)
        
        self.button1=ttk.Button(self.master,text="Translate",command=self.translate)
        self.button1.grid(row=6,column=0,padx=5,pady=5)
        
        self.label4=ttk.Label(self.master,text="Translation")
        self.label4.grid(row=7,column=0,padx=5,pady=5)
        
        self.textbox2=tk.Text(self.master,height=4,state="disabled")
        self.textbox2.grid(row=8,column=0,padx=5,pady=5)

    def translate(self):
        translator=Translator()
        text=self.textbox1.get("1.0",tk.END)
        src_lang=self.lang_codes[self.source_lang.get()]
        dest_lang=self.lang_codes[self.dest_lang.get()]
        translation=translator.translate(text,src=src_lang,dest=dest_lang)
        self.textbox2.config(state="normal")
        self.textbox2.delete("1.0",tk.END)
        self.textbox2.insert(tk.END,translation.text)
        self.textbox2.config(state="disabled")

if _name_ == "_main_":
    root=tk.Tk()
    app=TranslatorApp(root)
    root.mainloop()

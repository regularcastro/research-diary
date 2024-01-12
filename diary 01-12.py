import tkinter as tk
from tkinter import messagebox
from datetime import datetime
import sys
import os


class VirtualDiary:
    def __init__(self, master):
        self.master = master
        self.current_time = datetime.now().strftime("%m-%d")
        self.master.title(f"Diário {os.path.basename(os.getcwd())} {self.current_time}")
        self.master.geometry("400x400")
        #self.master.iconbitmap("graphite.ico")

        self.create_widgets()

    def create_widgets(self):
        self.text_entry = tk.Text(self.master, wrap=tk.WORD, height=15, width=40)
        self.text_entry.pack(pady=10)

        save_button = tk.Button(self.master, text="Registrar", command=self.save_entry)
        save_button.pack()

    def save_entry(self):
        entry_text = self.text_entry.get("1.0", tk.END).strip()
        if entry_text:
            
            file_name = f"Diário {os.path.basename(os.getcwd())} {self.current_time}.txt"

            with open(file_name, "w") as file:
                file.write(entry_text)              

            messagebox.showinfo("Info","Registro salvo.")
            self.text_entry.delete("1.0", tk.END)
            sys.exit()
            
        else:
            messagebox.showwarning("Info","Registro vazio!")
            

def main():
    root = tk.Tk()
    app = VirtualDiary(root)
    root.mainloop()

if __name__ == "__main__":
    main()
